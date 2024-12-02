# TO BE IMPLEMENTED
# Hint: keep it simple: use a dictionary to store and update the truth values of the PPAM's formulas.

class PurePastActionMask:
    def __init__(self, env):
        self.beforelast = -1
        self.ever_below_10 = False

    def reset(self):
        self.beforelast = -1
        self.ever_below_10 = False

    def apply(self, state, valve_open, action, timestep):
        # valve_open is either Y closed or Y open
        forced_action = action

        if state < 10:
            self.ever_below_10 = True

        if action == 1: #want to open
            if state <= 91:
                if valve_open == False and self.beforelast == True: #does not hold that Y closed -> YYclosed
                    forced_action = 0
            else:
                forced_action = 2
        elif action == 2: #want to close
            if state >= 7:
                if not self.ever_below_10:
                    if valve_open == True and self.beforelast == False: #does not hold that Y open -> YYopen
                        forced_action = 1
                else:
                    if (valve_open == True and self.beforelast == False) or state < 50: #does not hold that Y open -> YYopen AND P(level < 10) -> level >= 50
                        forced_action = 0
            else:
                forced_action = 1
        else:
            if state <= 7 and not valve_open:
                forced_action = 1
            elif state >= 91 and valve_open:
                forced_action = 2

        
        self.beforelast = valve_open
        return forced_action