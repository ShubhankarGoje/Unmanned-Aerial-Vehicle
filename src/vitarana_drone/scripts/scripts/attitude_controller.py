#!/usr/bin/env python
'''
This python file runs a ROS-node of name attitude_control which controls the roll pitch and yaw angles of the eDrone.
This node publishes and subsribes the following topics:
        PUBLICATIONS            SUBSCRIPTIONS
        /roll_error             /pid_tuning_altitude
        /pitch_error            /pid_tuning_pitch
        /yaw_error              /pid_tuning_roll
        /edrone/pwm             /edrone/imu/data
        /get_yaw                /edrone/drone_command
                                /set_yaw
'''

from vitarana_drone.msg import *
from pid_tune.msg import PidTune
from sensor_msgs.msg import Imu
from std_msgs.msg import *
import rospy
import tf
import numpy as np

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

class Edrone():

    """docstring for Edrone"""
    def __init__(self):
        rospy.init_node('attitude_controller')  # initializing ros node with name drone_control

        # This corresponds to your current orientation of eDrone converted in euler angles form.
        # [r,p,y]
        self.drone_orientation_euler = np.array([0.0, 0.0, 0.0])
        
        # This is the setpoint that will be received from the drone_command in the range from 1000 to 2000
        # [r_setpoint, p_setpoint, y_setpoint]
        self.setpoint_cmd = np.array([1500.0,1500.0, 1500.0])
        
        # The setpoint of orientation in euler angles at which you want to stabilize the drone
        # [r_setpoint, p_psetpoint, y_setpoint]
        self.setpoint_euler = np.array([0.0,0.0,0.0])

        # Declaring pwm_cmd of message type prop_speed and initializing values
        self.pwm_cmd = prop_speed()
        self.pwm_cmd.prop1 = 0.0
        self.pwm_cmd.prop2 = 0.0
        self.pwm_cmd.prop3 = 0.0
        self.pwm_cmd.prop4 = 0.0

        self.min_max_value_prop = (0, 1024)  # min and max values to propellers
        self.min_max_value_pid = (-10, 10) # min and max value to clamp from pid

        self.throttle_q=1000.0
        self.throttle_e=0.0

        self.last_input = np.array([0.0,0.0,0.0])  #Stores the last Input to the PID to calculate the derivative term
 
        self.Kpid = np.array([[31.2, 31.2, 500],[0, 0, 0],[148, 148, 230]])
        self.ProIntDer = np.array([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]) # The Proportional output from PID

        # # This is the sample time in which you need to run pid. Choose any time which you seem fit. Remember the stimulation step time is 50 ms
        self.sample_time = 0.06  # in seconds

        self.mnspd_active = False

        self.pwm_pub = rospy.Publisher('/edrone/pwm', prop_speed, queue_size=1)
        self.roll_error_pub = rospy.Publisher('/roll_error', Float32, queue_size=1)
        self.pitch_error_pub = rospy.Publisher('/pitch_error', Float32, queue_size=1)
        self.yaw_error_pub = rospy.Publisher('/yaw_error', Float32, queue_size=1)
        
        rospy.Subscriber('/drone_command', edrone_cmd, self.drone_command_callback)
        rospy.Subscriber('/edrone/imu/data', Imu, self.imu_callback)
        # rospy.Subscriber('/pid_tuning_roll', PidTune, self.roll_set_pid)
        # rospy.Subscriber('/pid_tuning_pitch', PidTune, self.pitch_set_pid)
        # rospy.Subscriber('/pid_tuning_yaw', PidTune, self.yaw_set_pid)


    def imu_callback(self, msg):
        # Converting quaternion to euler angles
        (self.drone_orientation_euler[1], self.drone_orientation_euler[0], self.drone_orientation_euler[2]) = np.array(tf.transformations.euler_from_quaternion([msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w]))

    def drone_command_callback(self, msg):
        self.setpoint_cmd[0] = msg.rcRoll
        self.setpoint_cmd[1] = msg.rcPitch
        self.setpoint_cmd[2] = msg.rcYaw
        self.throttle_q = msg.rcThrottle
           

        
    def pitch_set_pid(self, pitch):
        self.Kpid[0][0] = pitch.Kp * 0.06
        self.Kpid[1][0] = pitch.Ki * 0.0008
        self.Kpid[2][0] = pitch.Kd * 0.3
    def roll_set_pid(self, roll):
        self.Kpid[0][1] = roll.Kp * 0.06
        self.Kpid[1][1] = roll.Ki * 0.0008
        self.Kpid[2][1] = roll.Kd * 0.3
    def yaw_set_pid(self, yaw):
        self.Kpid[0][2] = yaw.Kp * 1
        self.Kpid[1][2] = yaw.Ki * 0.01
        self.Kpid[2][2] = yaw.Kd * 1

    def pid(self):
        
        # Convertng the range from 1000 to 2000 in the range of -10 degree to 10 degree for roll axis
        self.setpoint_euler[0:2] = self.setpoint_cmd[0:2] * 0.02 - 30
        self.setpoint_euler[2] = self.setpoint_cmd[2]
        
        error = np.array([0.0,0.0,0.0])
        d_input = np.array([0.0,0.0,0.0])
        output = np.array([0.0,0.0,0.0])

        # Calculating the error term of Control System.
        error = self.setpoint_euler - self.drone_orientation_euler

        #Calculating the defferental input
        # d_input = self.drone_orientation_euler - (self.last_input if self.last_input is not 0 else self.drone_orientation_euler)
        d_input = self.drone_orientation_euler - np.where(self.last_input==0,self.drone_orientation_euler,self.last_input)

        #Proportional term is directly proportional to error of Control system, hence p=Kp*error
        self.ProIntDer[0] = np.multiply(self.Kpid[0], error)

        # Integral term keeps on adding to itself to reduce/remove steady state error hence I=I+ Ki*error
        self.ProIntDer[1] += np.multiply(self.Kpid[1], error)

        # calmping the Integral term so that it doesnt keep on incresing indefinately 
        self.ProIntDer[1] = clamp(self.ProIntDer[1], (-0.0001, 0.301))

        # Calculating the derivative term that controls overshoot and slows the drone down when it is about to reach the desired position
        # As it reduces the P and I terms, it is negative
        self.ProIntDer[2] = np.multiply(-self.Kpid[2], d_input)

        #Calulating the summation od P,I and the D terms  
        output = self.ProIntDer[0]+self.ProIntDer[1]+self.ProIntDer[2]

        #Clmaping the output of pid
        output = np.array(clamp(output, (self.min_max_value_pid[0], self.min_max_value_pid[1])))

        #saving current input for feedback 
        self.last_input = np.array([self.drone_orientation_euler[0],self.drone_orientation_euler[1],self.drone_orientation_euler[2]])


        
        #converting the output -10 deg to 10 deg TO 1000 to 2000
        output = (output+30)/0.02

        # Converting the range of 1000 to 2000 to 0 to 1024 for throttle 
        self.throttle_e=self.throttle_q*1024/1000-1024
        output = 512-(output*1024/1000-1024)
        
        #setting propeller speed so that it adjests roll pitch yaw and throttel
        
        self.pwm_cmd.prop1 = self.throttle_e+(output[0]/4)-(output[1]/4)+(output[2]/1)
        self.pwm_cmd.prop2 = self.throttle_e+(output[0]/4)+(output[1]/4)-(output[2]/1)
        self.pwm_cmd.prop3 = self.throttle_e-(output[0]/4)+(output[1]/4)+(output[2]/1)
        self.pwm_cmd.prop4 = self.throttle_e-(output[0]/4)-(output[1]/4)-(output[2]/1)

        #Clamping propeller speed to the givin limits and rounding it as pwm are whole numbers
        [self.pwm_cmd.prop1,self.pwm_cmd.prop2,self.pwm_cmd.prop3,self.pwm_cmd.prop4] = list(map(round,clamp([self.pwm_cmd.prop1,self.pwm_cmd.prop2,self.pwm_cmd.prop3,self.pwm_cmd.prop4],(self.min_max_value_prop[0], self.min_max_value_prop[1]))))

        # Publishing Values for pwm and plotjuggler
        self.pwm_pub.publish(self.pwm_cmd)
        self.roll_error_pub.publish(error[0])
        self.pitch_error_pub.publish(error[1])
        self.yaw_error_pub.publish(error[2])
        
        
if __name__ == '__main__':

    e_drone = Edrone()
    r = rospy.Rate(1/e_drone.sample_time)  # specify rate in Hz based upon your desired PID sampling time, i.e. if desired sample time is 33ms specify rate as 30Hz
    while not rospy.is_shutdown():
        e_drone.pid()
        r.sleep()