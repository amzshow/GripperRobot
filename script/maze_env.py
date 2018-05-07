"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the environment part of this example. The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""


import numpy as np
import time
import sys


def ApplyForceOnJoint(self, action):

	# if action = 1 mean increasing
       if action:
       # else action = 0  mean deacreasing
       else:
	# do something

	# get the position of new thetas of each joint

        s_ = self.canvas.coords(self.rect)  # next state

	#here we measure the the distance between the obstacle and joint hand

        # reward function
        if s_ == : # zero difference
            reward = 10
            done = True
            s_ = 'terminal'
        elif s_ : # check the last cordinate and if distance is less than the past increase the reward
            reward = 2
            done = True
            s_ = 'terminal'
        else:
            reward = -2
            done = False

        return s_, reward, done

