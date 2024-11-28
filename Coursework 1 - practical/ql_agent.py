# Do NOT modify this file
# This file contains a simple implementation of a Q-learning agent

import numpy as np

"""
Actions:
0: noop
1: open
2: close
"""

class QLAgent:
    def __init__(self, env):
        self.env = env
        self.q_table = np.zeros((env.max_level + 1, 3))  # 3 actions: noop, open, close

    def choose_action(self, state):
        return np.argmax(self.q_table[state])

    def update_q_table(self, state, action, reward, next_state, alpha=0.1, gamma=0.99):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + gamma * self.q_table[next_state, best_next_action]
        self.q_table[state, action] += alpha * (td_target - self.q_table[state, action])