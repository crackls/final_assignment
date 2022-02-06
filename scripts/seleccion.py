#! /usr/bin/env python

import rospy
import os

from final_assignment.srv import Goal	


def select():

	"""
	Function that shows on the console the 4 options/modalities the user can choose:
		(1) Autonomous driving
		(2) Free driving
		(3) Assisted driving
		(0) exit
	
	Returns:
		selection (int): the user selection, 1, 2, 3 or 0
		
	"""
	
	print ("Select one of the following choices:")
	print ("\t(1) - Autonomous driving")
	print ("\t(2) - Free driving")
	print ("\t(3) - Assisted driving")
	print ("\t(0) - exit")
	
	selection = input("Enter numbers 1, 2, 3 or 0: ")
	return selection


def node():

	"""
	Main function to run the node. It will run a node acording to the user's input 
		
	"""

	rospy.init_node('Choose_your_fighter')
	
	while True:
		s = select()
	
		if s == 1:
			print ("You have selected option 1, autonomous driving")
			
			print ("Select the goal (x, y) you want to reach")
			x = float(input("\tx: "))
			y = float(input("\ty: "))
			rospy.wait_for_service('goal')
			goals = rospy.ServiceProxy('goal', Goal)
			goals(x, y)
    			
			os.system("roslaunch final_assignment autodrive.launch")
			
		elif s == 2:
			print ("You have selected option 2, free driving")
			
			os.system("roslaunch final_assignment freedrive.launch")

		elif s == 3:
			print ("You have selected option 3, assisted driving")
			
			os.system("roslaunch final_assignment assdrive.launch")
			
		elif s == 0:
			break

		else:
			print ("Wrong input, please enter a valid input (1, 2 or 3)")
			

if __name__=="__main__":
	node()
