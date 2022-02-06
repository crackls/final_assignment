Research Track 1: final Assignment
================================

Here in this repository you can find the code for the third and final assignment of the course Research Track 1,
done by Carlos Ángel López de Rodas Serrano.

Please, make sure you are in the noetic branch.

The code simulates a software architecture for the control of a mobile robot in a enviroment. The robot will
execute one out of three possible behaviors depending on the user's input.


Running
----------------------
First run the simulation enviroment, the move_base package and the node Autocontrol with:
```bash
$ roslaunch final_assignment init.launch
```
Then, to execute the other nodes, just run:
```bash
$ rosrun final_assignment seleccion.py
```
This will execute the node Choose_your_fighter (associated to seleccion.py) and it will ask you to select between
the three possible behaviours of the robot:
* Autonomous driving: the user will enter a goal and the robot will automatically reach it
* Free driving: the user can freely drive the robot arround the enviroment
* Assisted driving: same as free driving but it won't let the user to crash into walls

## Code description
-----------------------------
There are three mains codes that composes the whole program:
* ``seleccion.py`` node: Choose_your_fighter
* ``va_solo.py`` node: Autocontrol
* ``mando_limitado.py`` node: Ayuda

### seleccion.py ###
Describes the node Choose_your_fighter. This node will ask the user to choose between the three options mentioned
before and it will run the other nodes when need (when selected by the user)
```
IF (user_input == 'Autonomous driving');
	intput(goal);
	wait_service;
	call_service(goal);
ESLEIF (user_input == 'Free driving');
	execute_node(teleop_twist_keyboard);
ELSEIF (user_input == 'Assisted driving');
	execute_node(teleop_twist_keyboard);
	execute_node(Ayuda);
ELSEIF (user_input == 'exit');
	exit;
ELSE; 
	wrong_answer;
	loop;
		
```
### va_solo.py ###
It is ran when the node Autocontrol is ran. It will get the request of the goal and via an action it will publish the
goal to the topic move_base so the robot can reach it (whenever it is possble)
```
init_action;
set_.target_pose._parameters;
get_goal_request;
send_goal;
```

### mando_limitado.py ###
It is ran when the node Ayuda is ran. It will let the user move the robot using the teleop_twist_keyboard node but it will
stot the robot whenever it is close to a wall
```
subscribe(/cm_vel)
subscribe(/scan)

IF (obstacles close to left):
	IF (robot turning left):
		vel = stop_turning;
IF (obstacles in front):
	IF (robot moving foward):
		vel = stop_going_foward;
IF (obstacles close to right):
	IF (robot turning right):
		vel = stop_turning;
publish(/cmd_vel, vel)
```

An important remark is thatthe second option, Free driving, only needs the node teleop_twist_keyboard to be executed
