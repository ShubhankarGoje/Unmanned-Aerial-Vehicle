#!/usr/bin/env python


'''
This is a boiler plate script that contains an example on how to subscribe a rostopic containing camera frames 
and store it into an OpenCV image to use it further for image processing tasks.
Use this code snippet in your code or you can also continue adding your code in the same file
'''


from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import *
import cv2
import numpy as np
import rospy
from std_msgs.msg import Float32
from pyzbar.pyzbar import decode

class image_proc():

	# Initialise everything
	def __init__(self):
		rospy.init_node('barcode_test') #Initialise rosnode 

		self.delivary_location = NavSatFix()
		
		self.image_sub = rospy.Subscriber("/edrone/camera/image_raw", Image, self.image_callback) #Subscribing to the camera topic
		self.loc_pub = rospy.Publisher('/delivary_loc', NavSatFix, queue_size=1)     # Publishes the delivary location got from QR code
		
		self.img = np.empty([])      # This will contain your image frame from camera
		self.bridge = CvBridge()


	# Callback function of amera topic
	def image_callback(self, data):
		try:
			self.img = self.bridge.imgmsg_to_cv2(data, "bgr8") # Converting the image to OpenCV standard image
			str_loc=decode(self.img)     # Decoded output from QR code
		except CvBridgeError as e:
			print(e)
			return
		if(len(str_loc)!= 0):
			position=str_loc[0].data.split(',')

			self.delivary_location.latitude = float(position[0])     # Latitude of dilevary location
			self.delivary_location.longitude = float(position[1])     # Longitude of dilevary location
			self.delivary_location.altitude = float(position[2])     # altitude of dilevary location
			self.loc_pub.publish(self.delivary_location)       # Publish Location
		

if __name__ == '__main__':
	image_proc_obj = image_proc()
	rospy.spin()