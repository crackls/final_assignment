#! /usr/bin/env python

import rospy
import numpy

from geometry_msgs.msg import Twist   
from sensor_msgs.msg import LaserScan


dist_min = 0.5
max_ag = 720


def view(vision):

	"""
	Function that divides the space in front of the robot into three parts (left, front and right part) and gives
	minimun distance to an obstacle for each of those parts
	
	Arg: 
		vision (float): 721-aray vector that contains the distance from the robot to the obstacles in a range
				0-180º of the front part of the robot  
	
	Returns:
		dist (float): 3- aray vector that contains the minimun distance from the robot to the closer obstacle
			        for three regions of the space: left, frotn and right (respectively)
		
	"""
	
	dist = [min(vision(0:max_ag/3)), min(vision(max_ag/3:2*max_ag/3)), min(vision(2*max_ag/3:(max_ag+1)))]
	
	return dist
	
	
def callbback(msg):

	"""
	Callback of the topic cmdVel
	
	Arg:
		msg (Twist): contains all the information regarding the topic cmdVel
		
	"""
	
	if (msg.linear.x != 0):
		print("Robot moving")
	elif (msg.angular.z != 0):
		print("Robot turning")
	else
		print("Robot stopped")


def laserScanCallBack(msg):

	"""
	Callback of the topic LaserScan. It sets the velocity of the robot to 0 whenever the robot is about to crash
	into some obstacles
	
	Arg:   
		msg (LaserScan): has all the information about LaseScan topic
		
	"""
	
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
	
	vel = rospy.Subscriber("/cmd_vel", Twist, callBack)
	
	dist = view(msg.ranges)
	
	if dist[0] < dist_min:
		if vel.angular.z < 0:
			vel.angular.z = 0
	
	if dist[1] < dist_min:
		if vel.linear.x > 0:
			vel.linear.x = 0
	
	if dist[2] < dist_min:
		if vel.angular.z > 0:
			vel.angular.z = 0
	
	pub.publish(vel)
	

def node():

	"""
	Main function to run the node
		
	"""
	
	rospy.init_node('Ayuda')
	
	rospy.Subscriber("/scan", LaserScan, laserScanCallBack)
	
	rospy.spin()


if __name__=="__main__":
	node()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
