# Do NOT modify this file
# This file contains a very rough (and slightly modified) implementation of the WaterTank environment

import numpy as np

"""
Actions:
0: noop
1: open
2: close
"""

class WaterTankEnv:
    def __init__(self, max_level=101, level=50, valve_open=False):
        self.max_level = max_level
        self.level = level
        self.valve_open = valve_open

    def get_valve_open(self):
        return self.valve_open

    def reset(self, level=50, valve_open=False):
        self.level = level
        self.valve_open = valve_open
        return self.level

    def step(self, action):
        assert action in list(range(3)), f"Invalid action: {action}"

        if action == 1:
            self.valve_open = True
        elif action == 2:
            self.valve_open = False

        if self.valve_open:
            self.level = min(self.level + np.random.randint(1, 4), self.max_level + 1)
        else:
            self.level = max(self.level - np.random.randint(0, 3), 0)

        reward = -1e5 if self.level == 0 or self.level == self.max_level + 1 else 1
        failed = self.level == 0 or self.level == self.max_level
        return self.level, reward, failed