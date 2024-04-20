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

from vitarana_drone.msg import *
from vitarana_drone.srv import Gripper
from pid_tune.msg import PidTune
from sensor_msgs.msg import *
from std_msgs.msg import *
import rospy
import tf
import math
import numpy as np
import pandas as pd
from vitarana_drone import *
import csv 

folder_path = "/home/shubhankargoje/catkin_ws/src/vitarana_drone/scripts/"

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

def findNextBatch(packageTypeNotEmpty, deliv, retu):
    if packageTypeNotEmpty=="return":
        alone_ret_profit = []
        for i in range(len(retu)):
            alone_ret_profit.append((retu.iloc[i]["Name"], retu.iloc[i]["alone_profit"]/retu.iloc[i]["dist"]))
        alone_ret_profit.sort(key = lambda x: x[1])
        return alone_ret_profit[-1]
    elif packageTypeNotEmpty=="delivery":
        alone_del_piofit = []
        for i in range(len(deliv)):
            alone_del_piofit.append((deliv.iloc[i]["Name"], deliv.iloc[i]["alone_profit"]/deliv.iloc[i]["dist"]))
        alone_del_piofit.sort(key = lambda x: x[1])
        return alone_del_piofit[-1]
        
    del_ret_combination = []
    for i in range(len(deliv)):
        alone_del_ret_combination = []
        for j in range(len(retu)):
            del_ret_dist = (((retu.iloc[j]["m_pick_lat"] - deliv.iloc[i]["m_drop_lat"])**2) + ((retu.iloc[j]["m_pick_lng"] - deliv.iloc[i]["m_drop_lng"])**2))**0.5
            profit = (retu.iloc[j]["alone_profit"] + deliv.iloc[i]["alone_profit"])/(del_ret_dist + deliv.iloc[i]["dist"] + retu.iloc[j]["dist"])#
            alone_del_ret_combination.append((deliv.iloc[i]["Name"], retu.iloc[j]["Name"], profit))
        alone_del_ret_combination.sort(key = lambda x: x[2])
        del_ret_combination.append(alone_del_ret_combination[-1])
    del_ret_combination.sort(key = lambda x: x[2])
    return del_ret_combination[-1]

def putDataInFinal(pand, fin_df, schedule_manifest, a):
    fin_df.iloc[a] = [pand["Type"], pand["Name"], pand["pick_lat"], pand["pick_lng"], pand["pick_alt"], pand["drop_lat"], pand["drop_lng"], pand["drop_alt"]]
    schedule_manifest.iloc[a]["Type"] = fin_df.iloc[a]["Type"]
    if schedule_manifest.iloc[a]["Type"].strip().upper() == "DELIVERY":
        schedule_manifest.iloc[a]["Origin"] = fin_df.iloc[a]["Name"]
        schedule_manifest.iloc[a]["Destination"] = str(fin_df.iloc[a]["drop_lat"]) + ";" + str(fin_df.iloc[a]["drop_lng"]) + ";" + str(fin_df.iloc[a]["drop_alt"])
    elif schedule_manifest.iloc[a]["Type"].strip().upper() == "RETURN":
        schedule_manifest.iloc[a]["Origin"] = str(fin_df.iloc[a]["pick_lat"]) + ";" + str(fin_df.iloc[a]["pick_lng"]) + ";" + str(fin_df.iloc[a]["pick_alt"])
        schedule_manifest.iloc[a]["Destination"] = fin_df.iloc[a]["Name"]
    return fin_df, schedule_manifest

def find_pad_location(packType, name):
    lat, lng, alt = '', '', ''
    if packType == "DELIVERY"  :
        lat = x_to_lat(lat_to_x(18.9998102845) + ((ord(name[0])-65)*1.5))
        lng = y_to_long(long_to_y(72.000142461) - ((int(name[1])-1)*1.5))
        alt = 16.757981
    elif packType == "RETURN"  :
        lat = x_to_lat(lat_to_x(18.9999367615) + ((ord(name[0])-88)*1.5))
        lng = y_to_long(long_to_y(72.000142461) - ((int(name[1])-1)*1.5))
        alt = 16.757981
    return lat, lng, alt

def find_sequenced_location():
    manifest_df = pd.read_csv(folder_path + "bonus.csv")
    manifest_df.loc[len(manifest_df.index)] = manifest_df.columns

    locations_df = pd.DataFrame(columns = ["Type", "Name","pick_lat","pick_lng","pick_alt","drop_lat","drop_lng","drop_alt","m_pick_lat","m_pick_lng","m_drop_lat","m_drop_lng","dist","alone_profit"],index = list(range(len(manifest_df))))

    if len(manifest_df.columns)==3:
        manifest_df.columns = ["Type" , "Pick" , "Drop"]
        for pack_id in range(0,len(manifest_df)):
            locations_df.iloc[pack_id]["Type"] = manifest_df.iloc[pack_id]["Type"].strip().upper()
            if locations_df.iloc[pack_id]["Type"] == "DELIVERY"  :
                pk = manifest_df.iloc[pack_id]["Pick"].strip()
                dp = manifest_df.iloc[pack_id]["Drop"].strip().split(';')
                locations_df.iloc[pack_id]["Name"] = pk
                locations_df.iloc[pack_id]["pick_lat"], locations_df.iloc[pack_id]["pick_lng"], locations_df.iloc[pack_id]["pick_alt"] = find_pad_location(locations_df.iloc[pack_id]["Type"],locations_df.iloc[pack_id]["Name"])
                locations_df.iloc[pack_id]["drop_lat"], locations_df.iloc[pack_id]["drop_lng"], locations_df.iloc[pack_id]["drop_alt"] = float(dp[0]), float(dp[1]), float(dp[2])
            elif locations_df.iloc[pack_id]["Type"] == "RETURN"  :
                pk = manifest_df.iloc[pack_id]["Pick"].strip().split(';')
                dp = manifest_df.iloc[pack_id]["Drop"].strip()
                locations_df.iloc[pack_id]["Name"] = dp
                locations_df.iloc[pack_id]["pick_lat"], locations_df.iloc[pack_id]["pick_lng"], locations_df.iloc[pack_id]["pick_alt"] = float(pk[0]), float(pk[1]), float(pk[2])
                locations_df.iloc[pack_id]["drop_lat"], locations_df.iloc[pack_id]["drop_lng"], locations_df.iloc[pack_id]["drop_alt"] = find_pad_location(locations_df.iloc[pack_id]["Type"],locations_df.iloc[pack_id]["Name"])
        
            locations_df.iloc[pack_id]["m_pick_lat"], locations_df.iloc[pack_id]["m_pick_lng"] = lat_to_x(locations_df.iloc[pack_id]["pick_lat"]), long_to_y(locations_df.iloc[pack_id]["pick_lng"])
            locations_df.iloc[pack_id]["m_drop_lat"], locations_df.iloc[pack_id]["m_drop_lng"] = lat_to_x(locations_df.iloc[pack_id]["drop_lat"]), long_to_y(locations_df.iloc[pack_id]["drop_lng"])
    
            locations_df.iloc[pack_id]["dist"] = (((locations_df.iloc[pack_id]["m_drop_lat"] - locations_df.iloc[pack_id]["m_pick_lat"])**2) + ((locations_df.iloc[pack_id]["m_drop_lng"] - locations_df.iloc[pack_id]["m_pick_lng"])**2))**0.5
            locations_df.iloc[pack_id]["alone_profit"] = 5+(0.1*locations_df.iloc[pack_id]["dist"])
    
    else:
        manifest_df.columns = ["Type" , "Pick1" , "Pick2" , "Pick3" , "Pick4"]
        for pack_id in range(0,len(manifest_df)):
            locations_df.iloc[pack_id]["Type"] = manifest_df.iloc[pack_id]["Type"].strip().upper()
            if locations_df.iloc[pack_id]["Type"] == "DELIVERY"  :
                locations_df.iloc[pack_id]["Name"] = manifest_df.iloc[pack_id]["Pick1"]
                locations_df.iloc[pack_id]["pick_lat"], locations_df.iloc[pack_id]["pick_lng"], locations_df.iloc[pack_id]["pick_alt"] = find_pad_location(locations_df.iloc[pack_id]["Type"],locations_df.iloc[pack_id]["Name"])
                locations_df.iloc[pack_id]["drop_lat"], locations_df.iloc[pack_id]["drop_lng"], locations_df.iloc[pack_id]["drop_alt"] = float(manifest_df.iloc[pack_id]["Pick2"]), float(manifest_df.iloc[pack_id]["Pick3"]), float(manifest_df.iloc[pack_id]["Pick4"])
            elif locations_df.iloc[pack_id]["Type"] == "RETURN"  :
                locations_df.iloc[pack_id]["Name"] = manifest_df.iloc[pack_id]["Pick4"]
                locations_df.iloc[pack_id]["drop_lat"], locations_df.iloc[pack_id]["drop_lng"], locations_df.iloc[pack_id]["drop_alt"] = find_pad_location(locations_df.iloc[pack_id]["Type"],locations_df.iloc[pack_id]["Name"])
                locations_df.iloc[pack_id]["pick_lat"], locations_df.iloc[pack_id]["pick_lng"], locations_df.iloc[pack_id]["pick_alt"] = float(manifest_df.iloc[pack_id]["Pick1"]), float(manifest_df.iloc[pack_id]["Pick2"]), float(manifest_df.iloc[pack_id]["Pick3"])
                    
            locations_df.iloc[pack_id]["m_pick_lat"], locations_df.iloc[pack_id]["m_pick_lng"] = lat_to_x(locations_df.iloc[pack_id]["pick_lat"]), long_to_y(locations_df.iloc[pack_id]["pick_lng"])
            locations_df.iloc[pack_id]["m_drop_lat"], locations_df.iloc[pack_id]["m_drop_lng"] = lat_to_x(locations_df.iloc[pack_id]["drop_lat"]), long_to_y(locations_df.iloc[pack_id]["drop_lng"])
    
            locations_df.iloc[pack_id]["dist"] = (((locations_df.iloc[pack_id]["m_drop_lat"] - locations_df.iloc[pack_id]["m_pick_lat"])**2) + ((locations_df.iloc[pack_id]["m_drop_lng"] - locations_df.iloc[pack_id]["m_pick_lng"])**2))**0.5
            locations_df.iloc[pack_id]["alone_profit"] = 5+(0.1*locations_df.iloc[pack_id]["dist"])        
    
    deliv = locations_df.loc[locations_df["Type"]=="DELIVERY"]
    retu = locations_df.loc[locations_df["Type"]=="RETURN"]

    final_df = pd.DataFrame(columns = ["Type", "Name","pick_lat","pick_lng","pick_alt","drop_lat","drop_lng","drop_alt"],index = list(range(0,len(manifest_df))))
    schedule_manifest = pd.DataFrame(columns = ["Type", "Origin","Destination"], index = list(range(0,len(final_df))))

    itra = 0
    while (deliv.empty and retu.empty) != True:
        if deliv.empty:
            batch = findNextBatch("return", deliv, retu)
            final_df, schedule_manifest = putDataInFinal(retu.loc[locations_df["Name"]==batch[0]].iloc[0], final_df, schedule_manifest, itra)
            itra +=1
            retu = retu.loc[locations_df["Name"]!=batch[0]]
        elif retu.empty:
            batch = findNextBatch("delivery", deliv, retu)
            final_df, schedule_manifest = putDataInFinal(deliv.loc[locations_df["Name"]==batch[0]].iloc[0], final_df, schedule_manifest, itra)
            itra +=1
            deliv = deliv.loc[locations_df["Name"]!=batch[0]]
        else:
            batch = findNextBatch("both", deliv, retu)
            final_df, schedule_manifest = putDataInFinal(deliv.loc[locations_df["Name"]==batch[0]].iloc[0], final_df, schedule_manifest, itra)
            itra +=1
            final_df, schedule_manifest = putDataInFinal(retu.loc[locations_df["Name"]==batch[1]].iloc[0], final_df, schedule_manifest, itra)
            itra +=1
            deliv = deliv.loc[locations_df["Name"]!=batch[0]]
            retu = retu.loc[locations_df["Name"]!=batch[1]]
    
    schedule_manifest.to_csv(folder_path + "sequenced_manifest.csv", index=False)

    return final_df







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
        self.bottom_range = 0.0
        self.drone_zone = 0                                                                        # Stores the drone zone for execution of specific task in that drone zone
        self.package_picked=False
        
        self.marker_detected=False

        self.min_max_value_pid=(-500,500)                                                          # Stores the minimum value and maximum value at which PID should be clamped
        self.tolerance = (0.01,0.01,0.07,0.02)                                                       # Stores the Tolerence in meters to consider before taking next action (Latittude, Longitude, Altitude, Yaw)


        self.mnspd_setpoint_gcs = np.array([19.0, 72.0,0.0])                                       # Stores the Setpoints from "mnspd.py" node (Path Planning)
        self.mnspd_active = False                                                                  # Stores True when Obtruction is detected and Path Planning in Running
        self.mnspd_yaw = 0.0                                                                       # Stores the yaw given by the Path planning algorithm (mnspd)
        # self.mnspd_visited_stack= []                                                               # Stores the Visited Setpints during Pathplanning Algorithm for future use.
        # self.temp_pop_storeage=[]                                                                  # Stores the Temporary Visited Setpints during Pathplanning Algorithm for future use.

        self.position_cmd = edrone_cmd()                                                           # Variables of edrone command to set Throttle Roll Pitch and Yaw
        self.position_cmd.rcThrottle = 1500
        self.position_cmd.rcRoll = 1500
        self.position_cmd.rcPitch = 1500
        self.position_cmd.rcYaw = 0.0

        self.last_input = np.array([0.0,0.0,0.0])                                                  # Stores the last Input to the PID to calculate the derivative term
        self.Kpid = np.array([[0.295, 0.295, 480],[0.0, 0.0, 45],[16400000, 16400000, 9030]])        # Stores The values of Kp, Ki, Kd for (Roll, Pitch, Altitude)
        self.ProIntDer = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]])                     # The Proportional output from PID

        self.locations_df = find_sequenced_location()

        # # Stores the Package Location
        # self.package_locations_gcs=((18.9999864489 ,71.9999430161,8.44099749139),(19.0000135529,71.9999430161,8.44099749139),(19.000000305457803, 71.99995746199254, 8.44099749139))
        self.package_id=0                                                                          # Stores the index of current package to deliver

        # self.csv_delivary_location_gcs = []                                                        # Stroes the Delivery Location of respective packages
        # # Reading CSV ile and saving the location
        # with open('/home/shubhankargoje/catkin_ws/src/vitarana_drone/scripts/manifest.csv') as csv_file:
        #     csv_reader = csv.reader(csv_file, delimiter=',')
        #     line_count = 0
        #     for row in csv_reader:
        #         self.csv_delivary_location_gcs.append([float(row[1]),float(row[2]),float(row[3])])

        #     self.csv_delivary_location_gcs = tuple(self.csv_delivary_location_gcs)

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
        rospy.Subscriber('/edrone/range_finder_bottom', LaserScan, self.bottom_range_callback)             # Subscribe to get the ranges from from range_finde_bottom
        self.act_grip = rospy.ServiceProxy('edrone/activate_gripper', Gripper)                     # Subscribes for the Gripper Service
        rospy.Subscriber('/pid_tuning_roll', PidTune, self.lat_set_pid)                            # Subscribes for Latitude Tunning Values from pid_tune
        rospy.Subscriber('/pid_tuning_pitch', PidTune, self.lng_set_pid)                           # Subscribes for Longitude Tunning Values from pid_tune
        rospy.Subscriber('/pid_tuning_yaw', PidTune, self.alt_set_pid)                             # Subscribes for Altitude Tunning Values from pid_tune







    def bottom_range_callback(self, msg):
        
        self.bottom_range = msg.ranges[0]
        # if not self.package_picked:
            

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
        self.Kpid[0][0] = lat.Kp * 0.001  # This is just for an example. You can change the ratio/fraction value accordingly
        self.Kpid[1][0] = lat.Ki * 0.0001
        self.Kpid[2][0] = lat.Kd * 10000

        self.Kpid[0][1] = lat.Kp * 0.001 # This is just for an example. You can change the ratio/fraction value accordingly
        self.Kpid[1][1] = lat.Ki * 0.0001
        self.Kpid[2][1] = lat.Kd * 10000
        # if lat.Kd>1000:
        #     self.setpoint_cmd_gcs[2]=lat.Kp
        # else :
        #     self.setpoint_cmd_gcs[2]=10

    # Callback function for Longitude Tunning Values from pid_tune
    def lng_set_pid(self, lng):
        self.Kpid[0][1] = lng.Kp * 1000  # This is just for an example. You can change the ratio/fraction value accordingly
        self.Kpid[1][1] = lng.Ki * 0.0008
        self.Kpid[2][1] = lng.Kd * 100

    # Callback function for altitude Tunning Values from pid_tune
    def alt_set_pid(self, alt):
        # self.Kpid[0][2] = alt.Kp * 1  # This is just for an example. You can change the ratio/fraction value accordingly
        # self.Kpid[1][2] = alt.Ki * 1
        # self.Kpid[2][2] = alt.Kd * 10
        if alt.Kd>1000:

            self.setpoint_cmd_gcs[0]=x_to_lat(alt.Kp)
            self.setpoint_cmd_gcs[1]=y_to_long(alt.Ki)
        else :
            self.setpoint_cmd_gcs[0]=19
            self.setpoint_cmd_gcs[1]=72

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
                self.next_setpoint_gcs = np.array([self.locations_df.iloc[self.package_id]["pick_lat"],self.locations_df.iloc[self.package_id]["pick_lng"],self.locations_df.iloc[self.package_id]["pick_alt"]])
                self.start_loc_gcs=tuple(self.start_loc_gcs)
                break

    # Function to change the setpoint height and check if that height is reached (Returns True when reached)
    def change_height(self, height ,tolerance=0.07, landing = False):
        # self.setpoint_cmd_gcs[2] = height

        if (not landing) or (self.package_picked):
            self.setpoint_cmd_gcs[2] = height
            if(abs(self.drone_location_gcs[2]-height)<tolerance):
            
                return True
        else:
            if(self.object_pickable =="True"):
                return True
            self.setpoint_cmd_gcs[2] = self.drone_location_gcs[2] - self.bottom_range
            if self.bottom_range < tolerance :
                return True
        return False


    # Function to calculate Roll and pitch values to travel in straight line
    def roll_pitch(self, nxloc):
        nx_dist=(((nxloc[0]-self.drone_location_xy[0])**2)+((nxloc[1]-self.drone_location_xy[1])**2))**0.5
        nx_yaw=-np.sign(nxloc[0]-self.drone_location_xy[0])*math.acos(((nxloc[1]-self.drone_location_xy[1])/nx_dist))

        yaw_diff = nx_yaw - self.drone_orientation_euler[2]
        if yaw_diff>math.pi:
            yaw_diff -= 2*math.pi
        if yaw_diff<-math.pi:
            yaw_diff += 2*math.pi

        if yaw_diff<0:
            yaw_diff *= -1
        if yaw_diff>math.pi/2:
            yaw_diff = (math.pi - yaw_diff)

        if nx_dist>12 and yaw_diff<self.tolerance[3]:
            self.position_cmd.rcRoll = 1500
        elif nx_dist>12 and abs(math.pi/2 - yaw_diff)<self.tolerance[3]:
            self.position_cmd.rcPitch = 1500

        # if nx_dist>12 :#and yaw_diff<self.tolerance[3]
        #     self.position_cmd.rcRoll = (self.position_cmd.rcRoll -  1500)*math.sin(yaw_diff) + 1500
        #     self.position_cmd.rcPitch = (self.position_cmd.rcPitch - 1500)*math.cos(yaw_diff) +1500
        # elif nx_dist>12 and abs(math.pi/2 - yaw_diff)<self.tolerance[3]:
        # 	self.position_cmd.rcRoll = (self.position_cmd.rcRoll -  1500)*math.sin(yaw_diff) + 1500
        #     self.position_cmd.rcPitch = (self.position_cmd.rcPitch - 1500)*math.cos(yaw_diff) +1500

    # Function to Change setpoint loaction and check if the loaction is reached (Returns True when reached)
    def change_location(self,location,tolerance = 0.01):
        self.setpoint_cmd_gcs[:2]=location[:2]
        if(abs(lat_to_x(location[0])- self.drone_location_xy[0])< tolerance and abs(long_to_y(location[1])- self.drone_location_xy[1])<tolerance):
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

        self.roll_pitch(self.next_setpoint_xy[0:2])       


        # Zone to set the Take off height and wait till it is reached
        if(self.drone_zone==0):
            height = 10
            if(self.package_id == 0 ) and (not self.package_picked):
                height = 2
            elif ((self.locations_df.iloc[self.package_id-1]["Type"].lower().strip() == "return") and (self.locations_df.iloc[self.package_id]["Type"].lower().strip() == "delivery") and (not self.package_picked)) :
                height = 2
            if self.change_height(max(self.height,self.next_setpoint_gcs[2])+(height),tolerance=0.37):#if self.package_picked else 2
          
                self.drone_zone=1

        # Zone to set the yaw toward the target and when set change the setpoint location also take input from path planning if obstruction detected (This in when taveling towards warehouse)
        elif(self.drone_zone==1):
            yaw = self.drone_orientation_euler[2] if self.marker_detected else (self.mnspd_yaw if self.mnspd_active else next_yaw)
            if(self.package_id == 0 ) and (not self.package_picked):
                yaw = self.drone_orientation_euler[2]
                
            elif ((self.locations_df.iloc[self.package_id-1]["Type"].lower().strip() == "return") and (self.locations_df.iloc[self.package_id]["Type"].lower().strip() == "delivery") and (not self.package_picked)) :
                yaw = self.drone_orientation_euler[2]
            if self.change_yaw(yaw= yaw):
                if self.change_location(self.mnspd_setpoint_gcs if self.mnspd_active else self.next_setpoint_gcs, tolerance = (0.1 if (( self.marker_detected) or (not self.package_picked) or (self.locations_df.iloc[self.package_id]["Type"].lower().strip() == "return") or (self.mnspd_active)) else 0.05) ):#if ( self.package_picked and (self.locations_df.iloc[self.package_id]["Type"].lower().strip() == "delivary") ) else 0.06
                    if(not self.mnspd_active):
                        self.drone_zone=3 if  self.package_picked  else 2
                        if self.package_id  == len(self.locations_df) :
                            self.drone_zone=-1

        # set height for landing and when set activate or deactive gripper
        elif(self.drone_zone==2):
            if self.change_height(height=self.next_setpoint_gcs[2],tolerance=0.37, landing=True):
                if self.gripper_controller() :
                # Get deleviry location from qr detect when feature gets available elese from csv_deleivery_location
                    self.height = self.setpoint_cmd_gcs[2]
                    if ( self.package_picked==False and self.marker_detected):
                        self.package_id+=1
                        self.marker_detected=False
                    if self.package_id < len(self.locations_df) :
                        self.next_setpoint_gcs = np.array([self.locations_df.iloc[self.package_id]["drop_lat"],self.locations_df.iloc[self.package_id]["drop_lng"],self.locations_df.iloc[self.package_id]["drop_alt"]]) if self.package_picked else np.array([self.locations_df.iloc[self.package_id]["pick_lat"],self.locations_df.iloc[self.package_id]["pick_lng"],self.locations_df.iloc[self.package_id]["pick_alt"]])
                    else :
                        self.next_setpoint_gcs = np.array( self.start_loc_gcs )
                    self.drone_zone=0

        # Zone to detect marker and take the location of maker
        elif self.drone_zone==3:
            if self.locations_df.iloc[self.package_id]["Type"].lower().strip() == "return":
                self.marker_detected = True
            if self.marker_detected==False:
            	if self.change_height(height=self.next_setpoint_gcs[2] +10,tolerance=0.37, landing=True):
                	(self.next_setpoint_gcs[0], self.next_setpoint_gcs[1]) = self.marker_detect()
                	self.drone_zone=1
            else:
                self.drone_zone=2

        # Zone to set the last landing height after all task is done and stop the drone
        elif self.drone_zone==-1:
            if self.change_height(height=self.next_setpoint_gcs[2],tolerance=0.37, landing=True):
                print"Shut Down Everything"





        # Publish the altidude Distance beyween the drone and delivary building
        if self.package_id<len(self.locations_df):
            self.package_id_pub.publish(self.package_id)
            self.bottom_range_pub.publish((self.drone_location_gcs[2] - self.locations_df.iloc[self.package_id]["drop_alt"]))

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
