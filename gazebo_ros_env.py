import numpy as np
import time
import sys
import rospy as ros
import math as M
from gazebo_msgs.srv import GetJointProperties
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import ApplyJointEffort


def check_service(service_provider, com_message):

	ros.wait_for_service(service_provider)
	service = ros.ServiceProxy(service_provider,GetJointProperties)
	return service

def get_next_state():

	service = check_service('/gazebo/get_joint_properties', GetJointProperties)
	_pos = []
	for i in range(6):
		message = service("joint"+ str(i+1))
		_pos.append(message.position)
	return _pos
	
def calculate_dist():

	service = check_service('/gazebo/get_model_state', GetModelState)
	object_pos = service('unit_box', link)
        gripper_hand_pos = service('griber_robot', link5)

	pos_graper_hand = gripper_hand_pos.pose.position
	pos_object = object_pos.pose.position
	
	x_ = pow(pos_graper_hand.x - pos_object.x, 2)
	y_ = pow(pos_graper_hand.y - pos_object.y, 2)
	z_ = pow(pos_graper_hand.z - pos_object.z, 2)
	dis = M.sqrt(x_+y_+z_)
	return dis

def perform_action(joints):

	service = check_service('/gazebo/apply_joint_effort',ApplyJointEffort)
	for i in range(6):
		service('joint'+str(i+1), joints[i], rospy.Time(), rospy.Duration(10))
		rospy.sleep(0.5)
	
def ApplyForceOnJoint(self, action):

	forces = [0.0,0.0,0.0,0.0,0.0,0.0]
	# if action = 1 mean increasing
	if action:
		for i in range(6):
			forces[i] += 5
	else:
		for i in range(6):
			forces[i] -= 5
	

	s_ = get_next_state()  # next state
	dis = calculate()

    # reward function
	if dist == 0:
		reward = 10
		done = True
		s_ = 'terminal'
	else:
		reward = -2
		done = False

	return s_, reward, done

