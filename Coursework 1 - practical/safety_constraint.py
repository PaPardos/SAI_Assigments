# TO BE COMPLETED (lines 18 and 22)

"""
Actions:
0: noop
1: open
2: close
"""

class SafetyConstraint:
    def __init__(self, env):
        self.env = env
        self.last_change_timestep = -2  # Initialize to allow immediate first change
        self.below_10 = False

    def reset(self):
        self.last_change_timestep = -2
        self.below_10 = False

    def apply(self, state, valve_open, action, timestep):
        constrained_action = action

        # Check that the level is below 10
        if state < 10:
            self.below_10 = True

        # The agent can change the valve setting only if it was changed at least 2 timesteps ago
        if (timestep - self.last_change_timestep < 2 and
                ((action == 1 and not valve_open) or (action == 2 and valve_open))):
            constrained_action = 0

        # If the level has ever been below 10, then the agent can close the valve only if the water level is at least 50
        elif self.below_10 and action == 2 and state < 50:
            constrained_action = 0

        # Do not allow the tank to overflow: opening the valve or keeping it open
        # is not allowed if the level is at least []
        elif valve_open and state >= 91:
            constrained_action = 2

        # Do not allow the tank to deplete: closing the valve or keeping it closed
        # is not allowed if the level is at most []
        elif not valve_open and state <= 7:
            constrained_action = 1

        if (constrained_action == 1 and not valve_open) or (constrained_action == 2 and valve_open):
            self.last_change_timestep = timestep

        return constrained_action