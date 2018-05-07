"""
Reinforcement learning maze example.

Red rectangle:          explorer.
Black rectangles:       hells       [reward = -1].
Yellow bin circle:      paradise    [reward = +1].
All other states:       ground      [reward = 0].

This script is the main part which controls the update method of this example.
The RL is in RL_brain.py.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/
"""

from gazebo_ros_env import handle
from RL_brain import QLearningTable


def update():
    for episode in range(100):
        # initial observation
        observation = 

        while True:
            # RL choose action based on observation
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = handle.ApplyForceOnJoint(action)

            # RL learn from this transition
            RL.learn(str(observation), action, reward, str(observation_))

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break

    # end of game
    print('Model_ready')
    

if __name__ == "__main__":
    Model = handle()
    RL = QLearningTable(actions=list(range(Model.n_actions)))
    update()
