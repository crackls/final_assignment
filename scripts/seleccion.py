#! /usr/bin/env python

import rospy
import os

from final_assignment.srv import Goal, GoalRequest


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

	# Init the node
	rospy.init_node('Choose_your_fighter')
	
	a = True
	
	while (a == True):
		s = int(select())
	
		if s == 1:
			os.system("clear")
			print ("============================================================")
			print ("You have selected option 1, autonomous driving")
			
			print ("Select the goal (x, y) you want to reach")
			x = float(input("\tx: "))
			y = float(input("\ty: "))
			
			# waits for the server to be active
			rospy.wait_for_service('goal')
			# calls the server
			goal = rospy.ServiceProxy('goal', Goal)
			goal(x, y)

			a = False
			
		elif s == 2:
			os.system("clear")
			print ("============================================================")
			print ("You have selected option 2, free driving")			
			os.system("roslaunch final_assignment freedrive.launch")
			a = False

		elif s == 3:
			os.system("clear")
			print ("============================================================")
			print ("You have selected option 3, assisted driving")			
			os.system("roslaunch final_assignment assdrive.launch")
			a = False
			
		elif s == 0:
			a = False

		else:
			print ("Wrong input, please enter a valid input (1, 2 or 3)")
			

if __name__=="__main__":
	node()
