#!/usr/bin/env python

import rospy
from vitarana_drone.msg import *
from vitarana_drone import *
from sensor_msgs.msg import *
from std_msgs.msg import *
import math
import numpy as np
import pandas as pd
import tf


# Function to convert Latitude to X
def lat_to_x(input_latitude):
    return 110692.0702932625 * (input_latitude - 19)

# Function to convert Longitude to Y
def long_to_y(input_longitude):
    return -105292.0089353767 * (input_longitude - 72)

# Function to convert X to Latitude
def x_to_lat(input_x):
    return ((input_x/110692.0702932625) + 19)

def y_to_long(input_y):
    return ((-input_y/105292.0089353767) + 72)
    # if you use this for control, you may have to change the relevant pitch   direction because of the sign

# Function to convert Y to Longitude
def dist((xk,yk),(xm,ym)):
    return (((xk - xm)**2)+ ((yk - ym)**2))**0.5
# Selects nearest drone Orientation and assigns its nearest range finder to detect obstacles
def select_yaw_range_index(nx_yaw, cur_yaw):
    yaw_diff = nx_yaw - cur_yaw
    if yaw_diff>math.pi:
        yaw_diff -= 2*math.pi
    if yaw_diff<-math.pi:
        yaw_diff += 2*math.pi
    if yaw_diff>-math.pi/4 and yaw_diff<=math.pi/4:
        return (nx_yaw, 0)
    elif yaw_diff>math.pi/4 and yaw_diff<=3*math.pi/4:
        return (cur_yaw + (yaw_diff - math.pi/2), 3)
    elif yaw_diff>-3*math.pi/4 and yaw_diff<=-math.pi/4:
        return (cur_yaw + (yaw_diff + math.pi/2), 1)
    elif yaw_diff>3*math.pi/4 or yaw_diff<=-3*math.pi/4:
        if yaw_diff<0:
            return (cur_yaw + (yaw_diff + math.pi), 2)
        else:
            return (cur_yaw + (yaw_diff - math.pi), 2)
    else:
        print "Malfunctioning in Select Yaw and Range Index"*20

class path_finder():

    # Initialise everything
    def __init__(self):
        rospy.init_node('mnspd') #Initialise rosnode
        self.sample_time = 0.06                                           # This is the sample time in which planning runs

        self.drone_location_xy=np.array([0.0,0.0,0.0])                    # Stores the Drone location in X, Y and altitude
        self.target_location_xy=np.array([1.0,1.0,1.0])                   # Stores the Target location in X, Y and altitude
        self.setpoint_cmd_xy = np.array([0.0, 0.0])
        self.ranges =np.array([0.0,0.0,0.0,0.0])                          # Stores the ranges got from the range_finder_top [front, right, back, left]
        self.drone_orientation_euler =np.array([0.0, 0.0, 0.0])           # Stores the Drone orientation in Euler form
        self.yaw=0.0                                                      # Stores the Angle made by the line connecting the Set Point Location and the drone Location with North, to set the Yaw to point towards the Target Location
        self.visited_setpoints = []                                       # Stores the Visited Locations while performing path planning
        self.mnspd_active=False
        self.scanning_zone=1                                 # Checks which scanning section is to be executed
        self.fill = 0
        self.package_picked = False
        self.target_distance = 0.0
        self.target_yaw = 0.0
        self.tolerance = (0.5, 24, 11, 0.1, 0.01,3, 16)                          # Tolerance in meter (Gazebo error , range finder limit, stop dist b/w drone and obstacle, x and y in m, yaw error,  visited point tolerance, no of accessible point taken by sensors) 
        self.range_index=0
        self.point_yaw = 0.0
        # Stores the [Obstuction Distance, True the obstruction range is grtter than Threshold value, Next point in (X,Y) in this direction, Distance of Target from the Next Point in this direction (SAY A), Difference betwwen the (Distance between Target Location and Drone Location) and distance 'A' at previous index ]
        self.sensor_data=pd.DataFrame({'Sensor Distance': [0.0]*self.tolerance[6] , 'Accessablity': [False]*self.tolerance[6],'Location': [(0.0,0.0)]*self.tolerance[6],'Distance': [0.0]*self.tolerance[6],'Significant Distance': [0.0]*self.tolerance[6]})
        self.mnspd_setpoint_cmd=NavSatFix() 
        self.mnspd_visited_position = NavSatFix()                              # Variable of NavSatFix, Stores the next Setpoint to Publish
        self.mnspd_visited_position.latitude = 0.0
        self.mnspd_visited_position.longitude = 0.0
        self.mnspd_visited_position.altitude =  0.0
        
        self.mnspd_yaw_pub = rospy.Publisher('/mnspd_yaw', Float32, queue_size=1)                   # Publish the Yaw to point the Drone toward the Target Loction
        self.mnspd_setpoint_pub = rospy.Publisher('/mnspd_setpoint', NavSatFix, queue_size=1)       # Publish the Next Location that the Drone should move
        self.mnspd_active_pub = rospy.Publisher('/mnspd_active', Bool , queue_size=1)
        self.mnspd_visited_position_pub = rospy.Publisher('/mnspd_visited', NavSatFix , queue_size=1)
 
        rospy.Subscriber('/edrone/gps', NavSatFix, self.drone_location_callback)# Subscribe to get the Current Drone Location published by the gps
        rospy.Subscriber('/target_loc', NavSatFix, self.target_callback)# Subbscribe to get the Destination Location Published by position_controller
        rospy.Subscriber('/edrone/range_finder_top', LaserScan, self.range_callback)# Subscribe to get the ranges from from range_finder_top
        rospy.Subscriber('/edrone/imu/data', Imu, self.imu_callback)# Subscribe to get the Drone Orientation published by the imu

    def imu_callback(self, msg):
        # Converting quaternion to euler angles
        (self.drone_orientation_euler[1], self.drone_orientation_euler[0], self.drone_orientation_euler[2]) = np.array(tf.transformations.euler_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]))
    #Gets Drone location
    def drone_location_callback(self, msg):
        self.drone_location_xy = np.array([lat_to_x(msg.latitude), long_to_y(msg.longitude), msg.altitude])

    # Callback function for Destination Location from position_controller
    def target_callback(self, msg):
        self.target_location_xy = np.array([msg.latitude, msg.longitude, msg.altitude])

    # Callback function for ranges from range_finder_top
    def range_callback(self, msg):
        m = np.array([msg.ranges[4]]+list(msg.ranges[1:4]))
        self.ranges = np.where(m > 0.5, m, self.ranges)


    # Gets a location before 
    def get_stop_xy(self):
        self.setpoint_cmd_xy[0] = -(self.ranges[self.range_index]-self.tolerance[2])*math.sin(self.target_yaw - self.range_index*math.pi/2)+self.drone_location_xy[0]
        self.setpoint_cmd_xy[1] = (self.ranges[self.range_index]-self.tolerance[2])*math.cos(self.target_yaw - self.range_index*math.pi/2)+self.drone_location_xy[1]
        self.visited_setpoints.append((self.setpoint_cmd_xy[0],self.setpoint_cmd_xy[1],self.drone_location_xy[2]))
        self.mnspd_visited_position.latitude = self.setpoint_cmd_xy[0]
        self.mnspd_visited_position.longitude = self.setpoint_cmd_xy[1]
        self.mnspd_visited_position.altitude =  self.drone_location_xy[2]
        return (self.setpoint_cmd_xy[0], self.setpoint_cmd_xy[1],self.drone_location_xy[2])

    # Checks if setpoint is reached
    def is_setpoint_set(self,location):
        if (abs(self.drone_location_xy[0]-location[0])< self.tolerance[3] and abs(self.drone_location_xy[1]-location[1])< self.tolerance[3]) :
            return True
        return False

    # Checks if yaw is set
    def is_yaw_set(self,yaw):
        if(abs(self.drone_orientation_euler[2]- yaw)<self.tolerance[4]):
            return True
        return False

    # Function to check if the direction is possible or not according to the ranges of Obstruction and and set True or False in self.sensor_data
    def sensor_dist(self,fill):
        self.sensor_data['Sensor Distance'][fill::4] = self.ranges
        self.sensor_data['Accessablity'][fill::4] = self.ranges > self.tolerance[1]



    # Gets all possible locations the drone can go to
    def get_location_data (self):

        x = (-10*np.sin((self.yaw + math.pi/2) - (self.sensor_data['Location'].index * (math.pi/8)))) + self.setpoint_cmd_xy[0]
        y = (10*np.cos((self.yaw + math.pi/2) - (self.sensor_data['Location'].index * (math.pi/8)))) + self.setpoint_cmd_xy[1]
        self.sensor_data['Location'] = [(x[i],y[i]) for i in range(16)]
        self.sensor_data['Distance'] = self.sensor_data['Location'].apply( lambda (x,y) : dist((self.target_location_xy[0],self.target_location_xy[1]),(x,y)))
        self.sensor_data['Significant Distance'] = self.sensor_data['Distance'] - self.target_distance

    #Chooses the most appropriate location
    def choose_location(self, near_miss=False, visited = False):
        self.get_location_data()

        for ind in list(self.sensor_data.sort_values('Significant Distance').index):
                    
            nxt = (ind + 1) if ind < (self.tolerance[6]-1) else 0
            prv = (ind - 1) if ind > 0 else (self.tolerance[6]-1)
                    
            if(self.sensor_data["Accessablity"][ind] and ((self.sensor_data["Accessablity"][nxt] and self.sensor_data["Accessablity"][prv]) or near_miss)):
                        
                point_visited=False

                for visited in self.visited_setpoints:
                    if(abs(visited[0]-self.sensor_data["Location"][ind][0])<self.tolerance[5] and abs(visited[1]-self.sensor_data["Location"][ind][1])<self.tolerance[5]):
                                    
                        point_visited=True
                        break

                if( (not point_visited )or  visited ):
                    print "Index Chosen : " , ind

                    pr = (self.range_index+1) if self.range_index<3 else 0
                    if(ind == pr*4):
                        self.mnspd_active=False
                        self.setpoint_cmd_xy =  np.array([0.0, 0.0])
                        return True
                                
                    
                    self.visited_setpoints.append(self.sensor_data["Location"][ind])
                    self.setpoint_cmd_xy = self.sensor_data["Location"][ind]
                    self.mnspd_visited_position.latitude = self.setpoint_cmd_xy[0]
                    self.mnspd_visited_position.longitude = self.setpoint_cmd_xy[1]
                    self.mnspd_visited_position.altitude =  self.drone_location_xy[2]
                    
                    return True

        return False


        
    # Function to check if the direction is possible or not according to the ranges of Obstruction and and set True or False in self.sensor_data
    def planning(self):


        self.target_distance = dist((self.target_location_xy[0],self.target_location_xy[1]),(self.drone_location_xy[0],self.drone_location_xy[1]))
        self.target_yaw =  np.sign(self.drone_location_xy[0]-self.target_location_xy[0])*math.acos((self.target_location_xy[1]-self.drone_location_xy[1])/self.target_distance)
        self.target_yaw, self.range_index = select_yaw_range_index(self.target_yaw, self.drone_orientation_euler[2])
        self.yaw = self.target_yaw



        # Checks if package is not picked and orientation is not too much to detect ground as an obstacle and yaw is set towards the direction it is moving
        if(abs(self.drone_orientation_euler[1])<0.1 and abs(self.drone_orientation_euler[0])<0.1 and self.target_distance > self.tolerance[1] and not self.mnspd_active and self.is_yaw_set(yaw=self.target_yaw)):
            # If there is NO Obstuction in front of the drone in the Threshold limit (self.tolerance[1] m) and The Target Location is before the obstruction and the pitch and roll are not to high (if the pitch and roll are high it detects the ground and consider it as obstruction) and Drone has Horizontal movement
            if(self.ranges[self.range_index] > self.tolerance[1] ) :
                self.mnspd_active=False
                

            # If there is an obstruction in front of drone and the pitch and roll are not high and distance of object from the drone is gretter than threshold( self.tolerance[1] m)
            elif(self.ranges[self.range_index]> self.tolerance[0]and self.ranges[self.range_index]<=self.tolerance[1]):
                print "obstracle detected"
                print self.ranges
                self.point_yaw = self.target_yaw

                self.mnspd_active=True
                (self.mnspd_setpoint_cmd.latitude,self.mnspd_setpoint_cmd.longitude,self.mnspd_setpoint_cmd.altitude) = self.get_stop_xy()
                
        # If the setpoint is reached 
        if self.mnspd_active and self.is_setpoint_set(self.setpoint_cmd_xy):

            #Fill the data with reqired info 
            if(self.scanning_zone==1 ) : 
                self.sensor_dist(fill = self.fill)
                self.scanning_zone=2
            #Change yaw to 22.5 degree and get data again
            elif(self.scanning_zone==2):
                self.yaw=(self.point_yaw-((self.fill+1)*(math.pi/8)) )if self.fill<3 else self.target_yaw
                if self.yaw<-math.pi and (self.drone_orientation_euler[2]>0 and self.drone_orientation_euler[2]<math.pi):
                    self.yaw = 2*math.pi + self.yaw 
                if self.is_yaw_set(self.yaw):
                    self.fill+=1 if self.fill<4 else 0
                    self.scanning_zone=1 if self.fill<4 else 3

                    if self.fill==4:
                        self.yaw = self.target_yaw
                        self.point_yaw = self.target_yaw

            #If data is collected, choose setpoint and move
            elif (self.scanning_zone==3):
                self.yaw = self.target_yaw
                self.point_yaw = self.target_yaw
                if(self.is_yaw_set(self.yaw)):
                    #Do not choose alredy choosen points and move with safe distance from obstacle
                    if self.choose_location():
                        self.mnspd_setpoint_cmd.latitude = self.setpoint_cmd_xy[0]
                        self.mnspd_setpoint_cmd.longitude = self.setpoint_cmd_xy[1]
                        self.mnspd_setpoint_cmd.altitude = self.drone_location_xy[2]
                        self.fill = 0
                        self.scanning_zone = 1
                    #Do not choose alredy choosen points and move really close to the obstacle
                    elif self.choose_location(near_miss=True) :
                        self.mnspd_setpoint_cmd.latitude = self.setpoint_cmd_xy[0]
                        self.mnspd_setpoint_cmd.longitude = self.setpoint_cmd_xy[1]
                        self.mnspd_setpoint_cmd.altitude = self.drone_location_xy[2]
                        self.fill = 0
                        self.scanning_zone = 1
                    #can Choose alredy choosen points and move with safe distance from obstacle
                    elif self.choose_location(visited = True):
                        self.mnspd_setpoint_cmd.latitude = self.setpoint_cmd_xy[0]
                        self.mnspd_setpoint_cmd.longitude = self.setpoint_cmd_xy[1]
                        self.mnspd_setpoint_cmd.altitude = self.drone_location_xy[2]
                        self.fill = 0
                        self.scanning_zone = 1
                    #can Choose alredy choosen points and move really close to the obstacle
                    elif self.choose_location(near_miss=True , visited = True):
                        self.mnspd_setpoint_cmd.latitude = self.setpoint_cmd_xy[0]
                        self.mnspd_setpoint_cmd.longitude = self.setpoint_cmd_xy[1]
                        self.mnspd_setpoint_cmd.altitude = self.drone_location_xy[2]
                        self.fill = 0
                        self.scanning_zone = 1

                    else :
                        print "All paths blocaked !!!!"
        #If package is not picked send 0.0
        if(not self.package_picked):
            self.mnspd_visited_position.latitude=0.0
            self.mnspd_visited_position.longitude=0.0
            self.mnspd_visited_position.altitude=0.0
        self.mnspd_visited_position_pub.publish(self.mnspd_visited_position)
        self.mnspd_yaw_pub.publish(self.yaw)                      # Publish Yaw
        self.mnspd_active_pub.publish(self.mnspd_active)          # Publish if mnspd is planning path
        self.mnspd_setpoint_pub.publish(self.mnspd_setpoint_cmd)  # Publish next set point
        
        




   
        


if __name__ == '__main__':

    path_obj = path_finder()
    r = rospy.Rate(1/path_obj.sample_time)  # specify rate in Hz based upon your desired PID sampling time, i.e. if desired sample time is 33ms specify rate as 30Hz
    while not rospy.is_shutdown():
        path_obj.planning()
        r.sleep()
    
                
                

            
