import gazebo_ros_env as handle
from RL_brain import QLearningTable

def update():
    for episode in range(100):
        # initial observation
        observation = handle.get_next_state()

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
   
    RL = QLearningTable(actions=list(range(2))
    update()
