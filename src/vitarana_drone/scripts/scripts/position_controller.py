#!/usr/bin/env python
'''
This python file runs a ROS-node of name attitude_control which controls the roll pitch and yaw angles of the eDrone.
This node publishes and subsribes the following topics:
        PUBLICATIONS            SUBSCRIPTIONS
        /roll_error             /pid_tuning_altitude
        /pitch_error            /pid_tuning_pitch
        /yaw_error              /pid_tuning_roll
        /drone_command          /edrone/imu/data
        /get_yaw                /delivary_loc
        /bott_rang              /set_yaw
        /target_loc             /edrone/gps
        /package_no             /edrone/gripper_check
        /package_picked         /edrone/marker_data
                                /mnspd_active
                                /mnspd_setpoint
                                /mnspd_yaw
                                /mnspd_visited
'''

# [A1,A2,A3,B1,B2,B3,C1,C2,C3]
# package = [[18.9998102845, 72.000142461, 16.757981], [18.9998238356062, 72.000142461, 16.757981], [18.9998373867124, 72.000142461, 16.757981], [18.9998102845, 72.00012821490463, 16.757981], [18.9998238356062, 72.00012821490463, 16.757981], [18.9998373867124, 72.00012821490463, 16.757981], [18.9998102845, 72.00011396880927, 16.757981], [18.9998238356062, 72.00011396880927, 16.757981], [18.9998373867124, 72.00011396880927, 16.757981]]
# [X1,X2,X3,Y1,Y2,Y3,Z1,Z2,Z3]
# return = [[18.9999367615, 72.000142461, 16.757981], [18.9999503126062, 72.000142461, 16.757981], [18.9999638637124, 72.000142461, 16.757981], [18.9999367615, 72.00012821490463, 16.757981], [18.9999503126062, 72.00012821490463, 16.757981], [18.9999638637124, 72.00012821490463, 16.757981], [18.9999367615, 72.00011396880927, 16.757981], [18.9999503126062, 72.00011396880927, 16.757981], [18.9999638637124, 72.00011396880927, 16.757981]]


from vitarana_drone.msg import *
from vitarana_drone.srv import Gripper
from pid_tune.msg import PidTune
from sensor_msgs.msg import *
from std_msgs.msg import *
import rospy
import tf
import math
import numpy as np
from vitarana_drone import *
import csv 
import pickle
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =7)

# Clamp the values passed in the list to the minimum and maximum in the tuple
def clamp(value_list, limits):
    return_list = []
    lower, upper = limits
    for value in value_list:
        if value is None:
            return_list.append(None)
        elif upper is not None and value > upper:
            return_list.append(upper)
        elif lower is not None and value < lower:
            return_list.append(lower)
        else:
            return_list.append(value)
    return return_list

# Convert Latitude to X in meters for Carteasian cordinate system
def lat_to_x(input_latitude):
    return 110692.0702932625 * (input_latitude - 19)

# Convert Longitude to Y in meters for Carteasian cordinate system
def long_to_y(input_longitude):
    return -105292.0089353767 * (input_longitude - 72)

# Convert X in meters to Latitude for Geographic cordinate system
def x_to_lat(input_x):
    return ((input_x/110692.0702932625) + 19)

# Convert Y in meters to Longitude for Geographic cordinate system
def y_to_long(input_y):
    return ((-input_y/105292.0089353767) + 72)

# Convert Yaw to 0 to 2pi
def yaw_to_all_positive(yaw):
    if yaw<0:
        yaw = 2*math.pi + yaw
    return yaw

# Select the yaw to the have the nearest range sensor pointing towards target Location
def select_yaw(nx_yaw, cur_yaw):
    yaw_diff = nx_yaw - cur_yaw
    if yaw_diff>math.pi:
        yaw_diff -= 2*math.pi
    if yaw_diff<-math.pi:
        yaw_diff += 2*math.pi
    if yaw_diff>-math.pi/4 and yaw_diff<=math.pi/4:
        return nx_yaw
    elif yaw_diff>math.pi/4 and yaw_diff<=3*math.pi/4:
        return cur_yaw + (yaw_diff - math.pi/2)
    elif yaw_diff>-3*math.pi/4 and yaw_diff<=-math.pi/4:
        return cur_yaw + (yaw_diff + math.pi/2)
    elif yaw_diff>3*math.pi/4 or yaw_diff<=-3*math.pi/4:
        if yaw_diff<0:
            return cur_yaw + (yaw_diff + math.pi)
        else:
            return cur_yaw + (yaw_diff - math.pi)
    else:
        print "Malfunctioning in Select Yaw"*20








class Position():

    """docstring for Edrone"""
    def __init__(self):
        rospy.init_node('position_controller')                                                     # initializing ros node with name drone_control

        self.drone_orientation_euler = np.array([0.0, 0.0, 0.0])                                   # This corresponds to your current orientation of eDrone converted in euler angles form

        self.height=0.0                                                                            # Store the previous setpoint altitude for further use



        self.setpoint_cmd_xy = np.array([0.0, 0.0,10])                                             # Stores the Setpoint location in Carteasian cordinate system (x in meters, y in meters, altitude)
        self.setpoint_cmd_gcs = np.array([19.0, 72.0,10])                                          # Stores the Setpoint location in Geographic cordinate system (Latitude, Longitude, altitude)
        self.next_setpoint_gcs = np.array([19.0, 72.0,10])                                         # Stores the Next Setpoint location in Geographic cordinate system (Latitude, Longitude, altitude)
        self.next_setpoint_xy = np.array([0.0, 0.0,10])                                            # Stores the Next Setpoint location in Carteasian cordinate system (x in meters, y in meters, altitude)
        



        self.start_loc_gcs = [0.0, 0.0,0.0]                                                        # Stores the Starting Loaction where the Drone Starts in Geographic cordinate system (Latitude, Longitude, altitude)
        self.drone_location_xy = np.array([0.0, 0.0, 0.0])                                         # Stores the Drone location in Carteasian cordinate system (x in meters, y in meters, altitude)
        self.drone_location_gcs = np.array([0.0, 0.0, 0.0])                                        # Stores the Drone location in Geographic cordinate system (Latitude, Longitude, altitude)
        self.qr_gcs = np.array([0.0, 0.0, 0.0])                                                    # Stores the Delivary Loaction from QR of the packae in Geographic cordinate system (Latitude, Longitude, altitude)
        self.marker_data = np.array([0.0,0.0,0.0])                                                 # Stores the data published by Detect Marker (Building id, x distance in meters, y distance in meters)


        self.error_gcs = np.array([0.0,0.0,0.0])                                                   # Stores the Error or Difference in Setpoint and Drone Location in Carteasian cordinate system (x in meters, y in meters, altitude)
        self.error_xy = np.array([0.0,0.0,0.0])                                                    # Stores the Error or Difference in Setpoint and Drone Location in Geographic cordinate system (Latitude, Longitude, altitude)
        self.next_error_xy = np.array([0.0,0.0,0.0])                                               # Stores the Error or Difference in Next Setpoint and Setpoint Location in Carteasian cordinate system (x in meters, y in meters, altitude)

        self.drone_zone = 0                                                                        # Stores the drone zone for execution of specific task in that drone zone
        self.package_picked=False
        
        self.marker_detected=False

        self.min_max_value_pid=(-500,500)                                                          # Stores the minimum value and maximum value at which PID should be clamped
        self.tolerance = (0.05,0.05,0.001,0.01)                                                       # Stores the Tolerence in meters to consider before taking next action (Latittude, Longitude, Altitude, Yaw)


        self.mnspd_setpoint_gcs = np.array([19.0, 72.0,0.0])                                       # Stores the Setpoints from "mnspd.py" node (Path Planning)
        self.mnspd_active = False                                                                  # Stores True when Obtruction is detected and Path Planning in Running
        self.mnspd_yaw = 0.0                                                                       # Stores the yaw given by the Path planning algorithm (mnspd)
        self.mnspd_visited_stack= []                                                               # Stores the Visited Setpints during Pathplanning Algorithm for future use.
        self.temp_pop_storeage=[]                                                                  # Stores the Temporary Visited Setpints during Pathplanning Algorithm for future use.

        self.position_cmd = edrone_cmd()                                                           # Variables of edrone command to set Throttle Roll Pitch and Yaw
        self.position_cmd.rcThrottle = 1500
        self.position_cmd.rcRoll = 1500
        self.position_cmd.rcPitch = 1500
        self.position_cmd.rcYaw = 0.0

        self.last_input = np.array([0.0,0.0,0.0])                                                  # Stores the last Input to the PID to calculate the derivative term
        self.Kpid = np.array([[0.23, 0.23, 540],[0.0, 0.0, 45],[14250000, 14250000, 9030]])        # Stores The values of Kp, Ki, Kd for (Roll, Pitch, Altitude)
        self.loaded_model = pickle.load(open("/home/shubhankargoje/catkin_ws/src/vitarana_drone/scripts/height_pid_regression.sav", 'rb'))
        self.ProIntDer = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])                     # The Proportional output from PID

        # Stores the Package Location
        self.package_locations_gcs=((18.9999864489 ,71.9999430161,8.44099749139),(19.0000135529,71.9999430161,8.44099749139),(19.000000305457803, 71.99995746199254, 8.44099749139))
        self.package_id=0                                                                          # Stores the index of current package to deliver

        self.csv_delivary_location_gcs = []                                                        # Stroes the Delivery Location of respective packages
        # Reading CSV ile and saving the location
        with open('/home/shubhankargoje/catkin_ws/src/vitarana_drone/scripts/manifest.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.csv_delivary_location_gcs.append([float(row[1]),float(row[2]),float(row[3])])

            self.csv_delivary_location_gcs = tuple(self.csv_delivary_location_gcs)

        # # This is the sample time in which you need to run pid. Choose any time which you seem fit. Remember the stimulation step time is 50 ms
        self.sample_time = 0.06  # in seconds

        self.position_pub = rospy.Publisher('/drone_command', edrone_cmd, queue_size=1)            # Publishes the setting throttle, Roll, pitch, yaw
        self.lat_error_pub = rospy.Publisher('/lat_error', Float32, queue_size=1)                  # Publishes the Lattude error
        self.lng_error_pub = rospy.Publisher('/lng_error', Float32, queue_size=1)                  # Publishes the Longitude error
        self.alt_error_pub = rospy.Publisher('/alt_error', Float32, queue_size=1)                  # Publishes the Altitude error
        self.bottom_range_pub = rospy.Publisher('/bott_rang', Float32, queue_size=1)               # Publishes the distance between the drone to the Delivery building height
        self.tar_loc_pub = rospy.Publisher('/target_loc', NavSatFix, queue_size=1)                 # Publishes the Next Setpoints
        self.package_id_pub = rospy.Publisher('/package_no', Int8, queue_size=1)                   # Publishes the Package Number of current package to deliver
        self.package_picked_pub = rospy.Publisher('/package_picked', Bool , queue_size=1)          # Publishes the Package picked variable

        rospy.Subscriber('/edrone/gps', NavSatFix, self.drone_location_callback)                   # Subscribes for the Drone Location
        rospy.Subscriber('/edrone/imu/data', Imu, self.imu_callback)                               # Subscribes for the Drone Oreintation
        rospy.Subscriber('/delivary_loc', NavSatFix, self.qr_scanner_callback)                     # Subscribes for the Delivery location from QR detect
        rospy.Subscriber('/edrone/gripper_check', String, self.gripper_check_callback)             # Subscribes for checking if the Parcel to pick is in Visinity
        rospy.Subscriber('/edrone/marker_data', MarkerData, self.marker_data_callback)             # Subscribes for Building id, X error nd Y error n meters from "detect_marker_cascade" 
        rospy.Subscriber('/mnspd_active', Bool , self.mnspd_active_callback)                       # Subscribes for checking if Obtruction is detected and Path planning is active
        rospy.Subscriber('/mnspd_setpoint', NavSatFix, self.mnspd_setpoint_callback)               # Subscribes for Setpoints from Path Planning 
        rospy.Subscriber('/mnspd_yaw', Float32, self.mnspd_yaw_callback)                           # Subscribes for Yaw orientation from Path Planning
        rospy.Subscriber('/mnspd_visited', NavSatFix , self.mnspd_visited_callback)                # Subscribes for the Visited Location During Path Planning
        self.act_grip = rospy.ServiceProxy('edrone/activate_gripper', Gripper)                     # Subscribes for the Gripper Service
        rospy.Subscriber('/pid_tuning_roll', PidTune, self.lat_set_pid)                            # Subscribes for Latitude Tunning Values from pid_tune
        rospy.Subscriber('/pid_tuning_pitch', PidTune, self.lng_set_pid)                           # Subscribes for Longitude Tunning Values from pid_tune
        rospy.Subscriber('/pid_tuning_yaw', PidTune, self.alt_set_pid)                             # Subscribes for Altitude Tunning Values from pid_tune








    # Callback function for Drone Orientation
    def imu_callback(self, msg):
        # Converting quaternion to euler angles
        (self.drone_orientation_euler[1], self.drone_orientation_euler[0], self.drone_orientation_euler[2]) = np.array(tf.transformations.euler_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]))

    # Callback function for Drone Location
    def drone_location_callback(self, msg):
        self.drone_location_gcs = np.array([msg.latitude, msg.longitude, msg.altitude])
        self.drone_location_xy = np.array([lat_to_x(msg.latitude), long_to_y(msg.longitude), msg.altitude])

    # Callback function for Latitude Tunning Values from pid_tune
    def lat_set_pid(self, lat):
        # self.Kpid[0][0] = lat.Kp * 0.001  # This is just for an example. You can change the ratio/fraction value accordingly
        # self.Kpid[1][0] = lat.Ki * 0.0001
        # self.Kpid[2][0] = lat.Kd * 10000

        # self.Kpid[0][1] = lat.Kp * 0.001 # This is just for an example. You can change the ratio/fraction value accordingly
        # self.Kpid[1][1] = lat.Ki * 0.0001
        # self.Kpid[2][1] = lat.Kd * 10000
        if lat.Kd>1000:
            self.setpoint_cmd_gcs[2]=lat.Kp
        else :
            self.setpoint_cmd_gcs[2]=10

    # Callback function for Longitude Tunning Values from pid_tune
    def lng_set_pid(self, lng):
        self.Kpid[0][1] = lng.Kp * 1000  # This is just for an example. You can change the ratio/fraction value accordingly
        self.Kpid[1][1] = lng.Ki * 0.0008
        self.Kpid[2][1] = lng.Kd * 100

    # Callback function for altitude Tunning Values from pid_tune
    def alt_set_pid(self, alt):
        self.Kpid[0][2] = alt.Kp * 1  # This is just for an example. You can change the ratio/fraction value accordingly
        self.Kpid[1][2] = alt.Ki * 1
        self.Kpid[2][2] = alt.Kd * 10
        # if alt.Kd>1000:

        #     self.setpoint_cmd_gcs[0]=x_to_lat(alt.Kp)
        #     self.setpoint_cmd_gcs[1]=y_to_long(alt.Ki)
        # else :
        #     self.setpoint_cmd_gcs[0]=19
        #     self.setpoint_cmd_gcs[1]=72

    # Callback function for To check if Parcel in Vicinity and Pickable
    def gripper_check_callback(self, msg):
        self.object_pickable = msg.data

    # Callback function for Delivery locations from QR detect
    def qr_scanner_callback(self, msg):

        self.qr_gcs =np.array([msg.latitude, msg.longitude, msg.altitude])

    # Callback function for Building id, X error nd Y error n meters from "detect_marker_cascade" 
    def marker_data_callback(self,data):
        self.marker_data[0]=data.marker_id
        self.marker_data[1]=data.err_x_m
        self.marker_data[2]=data.err_y_m 

    # Callback function for checking if Obtruction is detected and Path planning is active
    def mnspd_active_callback(self, msg):
        self.mnspd_active=msg.data

    # Callback function for Setpoints from Path Planning 
    def mnspd_setpoint_callback(self, msg):
        self.mnspd_setpoint_gcs = np.array([x_to_lat(msg.latitude),y_to_long( msg.longitude), msg.altitude])

    # Callback function for Yaw orientation from Path Planning
    def mnspd_yaw_callback(self,msg):
        self.mnspd_yaw= msg.data

    # Callback function for the Visited Location During Path Planning
    def mnspd_visited_callback(self, msg):
        if (msg.latitude != 0.0) and (msg.longitude != 0.0) :
            if not ([x_to_lat(msg.latitude),y_to_long( msg.longitude)] in self.mnspd_visited_stack) :
                self.mnspd_visited_stack.append([x_to_lat(msg.latitude),y_to_long( msg.longitude)])







    # Function to get the initial location of drone
    def get_start_pos(self):
        print("Start")
        i=1
        while True:
            i+=1
            self.start_loc_gcs = self.drone_location_gcs+0.0000000001
                    
            if( self.start_loc_gcs[0] > 1 and self.start_loc_gcs[1] > 1):
                self.setpoint_cmd_gcs = self.start_loc_gcs
                self.height = self.start_loc_gcs[2]
                self.next_setpoint_gcs = np.array(self.package_locations_gcs[self.package_id])
                self.start_loc_gcs=tuple(self.start_loc_gcs)
                break

    # Function to change the setpoint height and check if that height is reached (Returns True when reached)
    def change_height(self, height ,tolerance=0.07):
        self.setpoint_cmd_gcs[2] = height
        if(abs(self.drone_location_gcs[2]-height)<tolerance):
            return True
        return False

    # Function to calculate Roll and pitch values to travel in straight line
    def roll_pitch(self, nxloc):
        nx_dist=(((nxloc[0]-self.drone_location_xy[0])**2)+((nxloc[1]-self.drone_location_xy[1])**2))**0.5
        nx_yaw=-np.sign(nxloc[0]-self.drone_location_xy[0])*math.acos(((nxloc[1]-self.drone_location_xy[1])/nx_dist))

        nx_yaw = yaw_to_all_positive(nx_yaw)
        cr_yaw = yaw_to_all_positive(self.drone_orientation_euler[2])

        yaw_diff = abs(nx_yaw-cr_yaw)
        yaw_diff = abs(2*math.pi - yaw_diff) if yaw_diff>math.pi else yaw_diff
        yaw_diff = abs(math.pi - yaw_diff) if yaw_diff>math.pi/2 else yaw_diff

        if nx_dist>3 and yaw_diff<self.tolerance[3]:
            self.position_cmd.rcRoll = 1500
        elif nx_dist>3 and abs(math.pi/2 - yaw_diff)<self.tolerance[3]:
            self.position_cmd.rcPitch = 1500

    # Function to Change setpoint loaction and check if the loaction is reached (Returns True when reached)
    def change_location(self,location):
        self.setpoint_cmd_gcs[:2]=location[:2]
        self.roll_pitch((lat_to_x(location[0]),long_to_y(location[1])))       
        if(abs(lat_to_x(location[0])- self.drone_location_xy[0])<self.tolerance[0] and abs(long_to_y(location[1])- self.drone_location_xy[1])<self.tolerance[1]):
            return True
        return False

    # Function to change the setpoint yaw and check if the setpoint is reached (Return True when Reached)
    def change_yaw(self,yaw=0.0):
        if abs(self.next_error_xy[0])<1 and abs(self.next_error_xy[1])<1 :
            return True
        if not self.mnspd_active:
            yaw = select_yaw(yaw, self.drone_orientation_euler[2])
        self.position_cmd.rcYaw = yaw
        if(abs(self.drone_orientation_euler[2]-yaw) < self.tolerance[3]):
            return True
        return False

    # Function to Activate gripper if parcel in vicinity and Deactive gripper
    def gripper_controller(self):
        if(self.object_pickable=="True" or self.package_picked):  
            try: 
                self.package_picked= self.act_grip(not self.package_picked).result
                return True
            except rospy.ServiceException as exc:
                print("Service did not process self.zero_alt= self.drone_location[2]request: " + str(exc))
        return False

    # Function to the location of marker in Geographic Coordiante System
    def marker_detect(self):
        self.marker_detected=True
        return (x_to_lat(math.cos(self.drone_orientation_euler[2])*self.marker_data[1]-math.sin(self.drone_orientation_euler[2])*self.marker_data[2]+self.drone_location_xy[0]),y_to_long(math.cos(self.drone_orientation_euler[2])*self.marker_data[2]+math.sin(self.drone_orientation_euler[2])*self.marker_data[1]+self.drone_location_xy[1]))   








    def pid(self):
        self.setpoint_cmd_xy[0] =  lat_to_x(self.setpoint_cmd_gcs[0])
        self.setpoint_cmd_xy[1] =  long_to_y(self.setpoint_cmd_gcs[1])
        self.setpoint_cmd_xy[2] =  self.setpoint_cmd_gcs[2]

        self.next_setpoint_xy[0] =  lat_to_x(self.next_setpoint_gcs[0])
        self.next_setpoint_xy[1] =  long_to_y(self.next_setpoint_gcs[1])
        self.next_setpoint_xy[2] =  self.next_setpoint_gcs[2]
        
        # Convertng the range from 1000 to 2000 in the range of -10 degree to 10 degree for roll axis
        d_input = np.array([0.0,0.0,0.0])
        output = np.array([0.0,0.0,0.0])


        pmch = abs(self.setpoint_cmd_xy[2]-self.height)
        
        # self.Kpid[0][2] =self.loaded_model.predict(poly_reg.fit_transform([[pmch]]))[0]
        # if self.drone_zone==2: self.Kpid[0][2] *= 0.40
        
        # Calculating the error term of Control System.
        self.error_xy = self.setpoint_cmd_xy - self.drone_location_xy
        self.error_gcs = self.setpoint_cmd_gcs - self.drone_location_gcs
        self.next_error_xy = self.next_setpoint_xy - self.drone_location_xy

        self.error_gcs [:2] = 500/(1+np.exp(clamp(-20000*self.error_gcs [:2],(-50,50))))-250

        # Calculating the defferental input
        # d_input = self.drone_orientation_euler - (self.last_input if self.last_input is not 0 else self.drone_orientation_euler)
        d_input = self.drone_location_gcs - np.where(self.last_input==0,self.drone_location_gcs,self.last_input)

        #Proportional term is directly proportional to error of Control system, hence p=Kp*error
        self.ProIntDer[0] = np.multiply(self.Kpid[0], self.error_gcs)

        # Integral term keeps on adding to itself to reduce/remove steady state error hence I=I+ Ki*error
        self.ProIntDer[1] += np.multiply(self.Kpid[1], self.error_gcs)

        # calmping the Integral term so that it doesnt keep on incresing indefinately 
        # self.ProIntDer[1][:2] = clamp(self.ProIntDer[1][:2], (-3, 3))
        self.ProIntDer[1][2:] = clamp(self.ProIntDer[1][2:], (-10, 10))

        # Calculating the derivative term that controls overshoot and slows the drone down when it is about to reach the desired position
        # As it reduces the P and I terms, it is negative
        self.ProIntDer[2] = np.multiply(-self.Kpid[2], d_input)

        #Calulating the summation od P,I and the D terms  
        output = self.ProIntDer[0]+self.ProIntDer[1]+self.ProIntDer[2]

        #Clmaping the output of pid
        output = np.array(clamp(output, (self.min_max_value_pid[0], self.min_max_value_pid[1])))
        output[:2] = np.array(clamp(output[:2], (-25, 25)))
        # #saving current input for feedback 
        self.last_input = np.array([self.drone_location_gcs[0],self.drone_location_gcs[1],self.drone_location_gcs[2]])


        # Calculate Yaw for Next setpoint
        next_dist=((self.next_error_xy[0]**2)+(self.next_error_xy[1]**2))**0.5
        next_yaw=0
        if next_dist!=0:
            next_yaw=-np.sign(self.next_error_xy[0])*math.acos((self.next_error_xy[1]/next_dist))#np.sign(self.next_error_xy[0])*

        # Calculate Yaw for setpoint
        dist=((self.error_xy[0]**2)+(self.error_xy[1]**2))**0.5
        set_yaw=0
        if dist!=0:
            set_yaw=np.sign(self.error_xy[0])*math.acos((self.error_xy[1]/dist))
        beta = abs(self.drone_orientation_euler[2]-set_yaw)

        # set the pitch and roll value to publish from attitude controller
        pitch =1500 + (((math.cos(self.drone_orientation_euler[2])*output[1])+(math.sin(self.drone_orientation_euler[2])*output[0])))
        roll =1500 + (((math.cos(self.drone_orientation_euler[2])*output[0])-(math.sin(self.drone_orientation_euler[2])*output[1])))

        self.position_cmd.rcThrottle =1500 + output[2]
        self.position_cmd.rcPitch = pitch
        self.position_cmd.rcRoll = roll


        # Zone to set the Take off height and wait till it is reached
        if(self.drone_zone==0):
            if self.change_height(max(self.height,self.next_setpoint_gcs[2])+(10 )):#if self.package_picked else 2
                if (not self.package_picked) and self.mnspd_visited_stack:
                    self.temp_pop_storeage = self.mnspd_visited_stack.pop()
                self.drone_zone=1

        # Zone to set the yaw toward the target and when set change the setpoint location also take input from path planning if obstruction detected (This in when taveling towards warehouse)
        elif(self.drone_zone==1 and  self.package_picked):
            if self.change_yaw(yaw= self.drone_orientation_euler[2] if self.marker_detected else (self.mnspd_yaw if self.mnspd_active else next_yaw)):
                if self.change_location(self.mnspd_setpoint_gcs if self.mnspd_active else self.next_setpoint_gcs):
                    if(not self.mnspd_active):
                        self.drone_zone=3 
                        if self.package_id  == len(self.package_locations_gcs) :
                            self.drone_zone=-1

        # Zone to set the yaw toward the target and when set change the setpoint location also take input from path planning if obstruction detected (This is when travelling towards destination building loaction)
        elif (self.drone_zone==1 and  not self.package_picked):
            if self.change_yaw(next_yaw):
                if self.change_location((self.temp_pop_storeage) if (self.mnspd_visited_stack) else self.next_setpoint_gcs ):
                    if (self.mnspd_visited_stack):
                        self.temp_pop_storeage = self.mnspd_visited_stack.pop()
                    if((not self.mnspd_active) and self.next_error_xy[0] < self.tolerance[0] and self.next_error_xy[1] < self.tolerance[1]):
                        self.drone_zone=2
                        if self.package_id  == len(self.package_locations_gcs) :
                            self.drone_zone=-1

        # set height for landing and when set activate or deactive gripper
        elif(self.drone_zone==2):
            if self.change_height(height=self.next_setpoint_gcs[2],tolerance=0.37):
                if self.gripper_controller() :
                # Get deleviry location from qr detect when feature gets available elese from csv_deleivery_location
                    self.height = self.setpoint_cmd_gcs[2]
                    if ( self.package_picked==False and self.marker_detected):
                        self.package_id+=1
                        self.marker_detected=False
                    if self.package_id < len(self.package_locations_gcs) :
                        self.next_setpoint_gcs = np.array(self.csv_delivary_location_gcs[self.package_id]) if self.package_picked else np.array(self.package_locations_gcs[self.package_id])
                    else :
                        self.next_setpoint_gcs = np.array( self.start_loc_gcs )
                    self.drone_zone=0

        # Zone to detect marker and take the location of maker
        elif self.drone_zone==3:

            if self.marker_detected==False:
                if self.drone_orientation_euler[0] < 0.01 and self.drone_orientation_euler[1] < 0.01:
                    (self.next_setpoint_gcs[0], self.next_setpoint_gcs[1]) = self.marker_detect()
                    self.drone_zone=1
            else:
                self.drone_zone=2

        # Zone to set the last landing height after all task is done and stop the drone
        elif self.drone_zone==-1:
            if self.change_height(height=self.next_setpoint_gcs[2]):
                print"Shut Down Everything"





        # Publish the altidude Distance beyween the drone and delivary building
        if self.package_id<len(self.package_locations_gcs):
            self.package_id_pub.publish(self.package_id)
            self.bottom_range_pub.publish((self.drone_location_gcs[2] - self.csv_delivary_location_gcs[self.package_id][2]))

        # Publish values for attidude contrller node (Throttle, picth, roll, yaw)
        self.position_pub.publish(self.position_cmd)

        # publish Error values for Plotjuggler
        self.lat_error_pub.publish(self.error_xy[0])
        self.lng_error_pub.publish(self.error_xy[1])
        self.alt_error_pub.publish(self.error_gcs[2])
        self.package_picked_pub.publish(self.package_picked)
        # Publish the next setpoint for path planning (mnspd) node
        tar_loc =NavSatFix()
        (tar_loc.latitude, tar_loc.longitude, tar_loc.altitude) = (self.next_setpoint_xy[0], self.next_setpoint_xy[1], self.next_setpoint_xy[2])
        self.tar_loc_pub.publish(tar_loc)
        
        
if __name__ == '__main__':

    position = Position()
    r = rospy.Rate(1/position.sample_time)
    position.get_start_pos() # Get the starting loaction 

    while not rospy.is_shutdown():
        position.pid()
        r.sleep()
