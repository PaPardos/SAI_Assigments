# Do NOT modify this file
# You can run this script to test that your implemented PPAM respects the safety constraint.

# We will also run this script to test your implementation:
# if it passes all tests, and you implemented a PPAM correctly in ppam.py, you will get a full grade.

import numpy as np
import random

from WaterTankEnv import WaterTankEnv
from ql_agent import QLAgent
from ppam import PurePastActionMask
from safety_constraint import SafetyConstraint

def test_constraint_and_ppam(level=50, valve_open=False):
    env = WaterTankEnv()
    agent = QLAgent(env)
    safety_constraint = SafetyConstraint(env)
    ppam = PurePastActionMask(env)

    for episode in range(10):
        timestep = 0
        state = env.reset(level=level, valve_open=valve_open)
        safety_constraint.reset()
        ppam.reset()

        while timestep < 10000:
            action = agent.choose_action(state)
            valve_open = env.get_valve_open()

            safety_constraint_action = safety_constraint.apply(state, valve_open, action, timestep)
            ppam_action = ppam.apply(state, valve_open, action, timestep)

            if safety_constraint_action != ppam_action:
                print(f"Mismatch: Shield action {safety_constraint_action}, PPAM action {ppam_action}, Test failed\n")
                return

            next_state, reward, failed = env.step(ppam_action)

            if failed:
                print("Tank either depleted or overflowed. Test failed.")
                return

            agent.update_q_table(state, safety_constraint_action, reward, next_state)
            state = next_state
            timestep += 1

    print("Test passed: the PPAM constrains the RL agent according to the safety constraints.")
    return

if __name__ == "__main__":
    np.random.seed(0)
    random.seed(0)

    test_constraint_and_ppam()
    test_constraint_and_ppam(level=70, valve_open=True)
    test_constraint_and_ppam(level=95, valve_open=True)
    test_constraint_and_ppam(level=5, valve_open=False)
    test_constraint_and_ppam(level=30, valve_open=False)