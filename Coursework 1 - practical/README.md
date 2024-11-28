# Logics for Safe AI - Practical Assignment 1

## Introduction

In this assignment, you will implement a pure-past action mask (as we have seen in the lecture) that constrains an RL agent in a modified version of the WaterTank domain from the original paper on shields.

In this version of WaterTank, the tank has again a maximum capacity of at most 100 liters. When the valve is open, the water level increases between 1 litre and 4 liters; when the valve is closed, the water level either does not decrease, or it can decrease up to 3 liters (as in the original domain, the change in the water level is a discrete number).

## Safety Constraints

1. The water tank should never be depleted or overflow, i.e., the water level should never reach 0 or exceed 100;
2. Whenever the valve setting is changed, the agent must wait at least 2 timesteps before changing it again;
3. If the water level is below 10, then from that point onward the agent is allowed to close the valve only if the water level is at least 50.

## Assignment

You must:

1. Complete the implementation of the `safety_constraint.py` file by filling out the if-statements at lines 27 and 32;
2. Provide the PPLTL formulas for each of the safety constraints above (you can do this in the `.pdf` file containing the answers to the rest of the assignment's questions).
3. Implement a pure-past action mask that enforces the safety constraints above (you can do this in the `ppam.py` file).


## Testing and Evaluation

You can test your implementation by running the `test.py` file. This file will run 5 separate tests and output whether they were passed or not.

We will use the same script to test your implementation, so make sure to NOT modify it.

### Grading

This part of the assignment will be graded as follows:
1. 0.5 points for correctly implementing the safety constraints ((1) in the Assignment section); 
2. 0.5 point for giving the correct PPAM's PPLTL formulas ((2) in the Assignment section);
3. 2 points for correctly implementing the pure-past action mask ((3) in the Assignment section).


## Submission

You can submit your coursework by compressing it into a `.zip` archive (containing also the `.pdf` with your answers to the rest of the coursework) and uploading it on Blackboard.