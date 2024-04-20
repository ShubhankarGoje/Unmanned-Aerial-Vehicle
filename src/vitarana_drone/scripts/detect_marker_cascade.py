#!/usr/bin/env python


'''
This is a boiler plate script that contains an example on how to subscribe a rostopic containing camera frames 
and store it into an OpenCV image to use it further for image processing tasks.
Use this code snippet in your code or you can also continue adding your code in the same file
'''


from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import *  
from vitarana_drone.msg import MarkerData
import cv2
import numpy as np
import rospy
import tf
from std_msgs.msg import *
from pyzbar.pyzbar import decode
from matplotlib import pyplot as plt
import math

# Focal lenght of Camera
focal_length = 200/(math.tan((1.3962634/2)))

# Loads Tranining data
logo_cascade = cv2.CascadeClassifier('/home/shubhankargoje/catkin_ws/src/vitarana_drone/scripts/data/cascade.xml')



class image_proc():

	# Initialise everything
	def __init__(self):
		rospy.init_node('maker_find') #Initialise rosnode 

		self.drone_location = [0.0, 0.0, 0.0]          # Stores Drone Location
		self.bottom_range=0.0                          # Stores The vertical distance betwen drone h and building
		# self.building_loc =       # Stores all the building 
		self.building_id = 0                           # Store Building id

		self.image_sub = rospy.Subscriber("/edrone/camera/image_raw", Image, self.image_callback) #Subscribing to the camera topic
		rospy.Subscriber('/edrone/gps', NavSatFix, self.drone_location_callback)       # Subscribing to the gps for drone Location
		rospy.Subscriber('/edrone/imu/data', Imu, self.imu_callback)                   # Subscribing to imu_dta for drone orientation
		rospy.Subscriber('/bott_rang', Float32, self.get_bottom_range)
		rospy.Subscriber('/package_no', Int8, self.package_no_callback)

		self.Marker_data_pub = rospy.Publisher('/edrone/marker_data', MarkerData, queue_size=1)        # Publishing Marker Data

		self.drone_orientation_quaternion=[0.0,0.0,0.0,0.0]                                            # Stores Drone Orientation in Quaternion form
		self.drone_orientation_euler=[0.0,0.0,0.0]                                                     # Stores Drone Orientation in Euler form
		self.img = np.empty([])                                                                        # Stores Images frame from the drone camera
		self.gray= np.empty([])                                                                        # This will contain GrayScale image frame from camera
		self.bridge = CvBridge()
		self.marker_data = MarkerData()                                                                # Stores MarkerData for publishing
		self.x_dis = 0.0                                                                               # Stores the x_err for calculation purpose
		self.y_dis = 0.0                                                                               # Stores the y_err for calculation purpose

	# Callback For imu data (Drone Orientation)
	def imu_callback(self, msg):
		self.drone_orientation_quaternion = [msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]
		(self.drone_orientation_euler[1], self.drone_orientation_euler[0], self.drone_orientation_euler[2]) = tf.transformations.euler_from_quaternion([self.drone_orientation_quaternion[0], self.drone_orientation_quaternion[1], self.drone_orientation_quaternion[2], self.drone_orientation_quaternion[3]])
	
	def package_no_callback(self, msg):
		self.building_id=msg.data 

	# Callback For Drone location
	def drone_location_callback(self, msg):
		self.drone_location = [msg.latitude, msg.longitude, msg.altitude]

	def get_bottom_range(self, msg):
		self.bottom_range=msg.data

	# Callback function of Camera topic
	def image_callback(self, data):

		self.img = self.bridge.imgmsg_to_cv2(data, "bgr8")                          # Converting the image to OpenCV standard image
		self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)                      # Converting Image to Gray Scale
		# self.bottom_range = self.drone_location[2] - self.building_loc[self.building_id][2]           # Calculate Bottom Range
		
		logo = logo_cascade.detectMultiScale(self.gray, scaleFactor=1.05)           # Detected marker coordinates

		# Check for Marker only if Drone is Stable 
		if(abs(self.drone_orientation_euler[1])<0.1 and abs(self.drone_orientation_euler[0])<0.1):
			for (x, y, w, h) in logo:
				cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 255, 0), 2)
				cv2.line(self.img, (((2*x)+w)/2,0), (((2*x)+w)/2,400), (0, 255, 0) , 2)
				cv2.line(self.img, (0,((2*y)+h)/2), (400,((2*y)+h)/2), (0, 255, 0) , 2)
				#calculate Coordinates of X and y in image
				cxp = ((2*x)+w)/2 - 200
				cyp = 200 - ((2*y)+h)/2
				
				
				# Calculate error x and y
				self.x_dis = cxp*self.bottom_range/focal_length 
				self.y_dis = cyp*self.bottom_range/focal_length
				
		cv2.imshow('image',self.img)
		cv2.waitKey(1)

	def marker_detect(self):

		# Store marker data Calculated for Publishing
		self.marker_data.err_x_m = self.x_dis
		self.marker_data.err_y_m = self.y_dis + 0.35
		self.marker_data.marker_id = self.building_id
		# print "marker id : ", self.marker_data.marker_id

		# Publish Marker Data
		self.Marker_data_pub.publish(self.marker_data)
		
		
	
		
if __name__ == '__main__':

    ip = image_proc()
    r = rospy.Rate(1)  # Sample rate is set as 1 Hz

    while not rospy.is_shutdown():
        ip.marker_detect()
        r.sleep()
    rospy.spin()

