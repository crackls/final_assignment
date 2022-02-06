#! /usr/bin/env python

import rospy

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan


dist_min = 0.5
""" float: Threshold for the control of the linear distance """

vel = Twist(Vector3(0, 0, 0), Vector3(0, 0, 0))
""" Twist: Initializing global variable vel"""

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
	
	dist_l = 1000
	dist_f = 1000
	dist_r = 1000
	i = 0
	
	for d in vision:
		if i <= 240:
			if d < dist_l:
				dist_l = d
				
		elif i <= 480:
			if d < dist_f:
				dist_f = d
		
		else:
			if d < dist_r:
				dist_r = d
		i = i + 1

	dist = [dist_l, dist_f, dist_r]
	
	return dist
	
	
def velCallBack(msg):

	"""
	Callback of the topic cmdVel. It will take the value published on cmVel and put it into the global variable 
	vel, so it can be modified based on the laserScan's ouputs
	
	Arg:
		msg (Twist): contains all the information regarding the topic cmdVel
		
	"""

	global vel
	vel = msg


def laserScanCallBack(msg):

	"""
	Callback of the topic LaserScan. It sets the velocity of the robot to 0 whenever the robot is about to crash
	into some obstacles
	
	Arg:   
		msg (LaserScan): has all the information about LaseScan topic
		
	"""
	global vel
	
	pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
	
	dist = view(msg.ranges)
	
	if dist[0] < dist_min:
		if vel.angular.z < 0:		# if turning left
			vel.angular.z = 0	# stop turning left
	
	if dist[1] < dist_min:
		if vel.linear.x > 0:		# if going foward
			vel.linear.x = 0	# stop going forward
	
	if dist[2] < dist_min:
		if vel.angular.z > 0:		# if turning right
			vel.angular.z = 0	# stop turning right
	
	pub.publish(vel)
	

def node():

	"""
	Main function to run the node
		
	"""
	
	# Init the node
	rospy.init_node('Ayuda')
	
	# Subscribe to cmdVel topic
	rospy.Subscriber("/cmd_vel", Twist, velCallBack)
	
	# subscribe to laserScan topic
	rospy.Subscriber("/scan", LaserScan, laserScanCallBack)
	
	rospy.spin()


if __name__=="__main__":
	node()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
