#! /usr/bin/env python

import rospy
import actionlib

from final_assignment.srv import *
from move_base_msgs.msg import *
from actionlib_msgs.msg import *


def robotCallBack(request):

	"""
	Callback for the service Goal. It will take the goal the user entered and then it will move the
	robot towards the objetive if possible
	
	Arg:   
		request (Goal): Goal service information 
	"""
	
	x = request.x
	y = request.y
	
	client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
	client.wait_for_server()
	goal = MoveBaseGoal()
	
	goal.target_pose.header.frame_id = 'map'
	goal.target_pose.pose.orientation.w = 1
	goal.target_pose.pose.position.x = x
	goal.target_pose.pose.position.y = y
	
	client.send_goal(goal)
	
    	
def node():

	"""
	Main function to run the node
	"""

	rospy.init_node('Autocontrol')
	
	service = rospy.Service('goal', Goal, robotCallBack)
	
	rospy.spin()


if __name__=="__main__":
	node()
	
	
	
	
	
	
	
	
	
	
	
