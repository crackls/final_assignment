#! /usr/bin/env python

import rospy
import actionlib

from final_assignment.srv import Goal
from move_base_msgs.msg import *


def robotCallBack(request):

	"""
	Callback for the service Goal. It will take the goal the user entered and then it will move the
	robot towards the objetive if possible
	
	Arg:   
		request (Goal): Goal service information 
	"""
	

	pub = rospy.Publisher("/move_base", MoveBaseActionGoal, queue_size = 10)

	goal = MoveBaseGoal()
    	
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.pose.orientation.w = 1
	goal.target_pose.pose.position.x = request.x
	goal.target_pose.pose.position.y = request.y
  	
	pub.publish(goal)

    	
def node():

	"""
	Main function to run the node
	"""

	rospy.init_node('Autocontrol')
	
	service = rospy.Service('goal', Goal, robotCallBack)
	
	rospy.spin()


if __name__=="__main__":
	node()
	
	
	
	
	
	
	
	
	
	
	
