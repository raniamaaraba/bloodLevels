# Activity Python 13: Task 2
# File: HW13p_1_task2_maarabrn.py 
# Date:    26 11 2023
# By:      Rania Maaraba
# Section: 21
# Team:    355
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# The program randomly calculates blood pressure and categorises them
# based on the systolic levels between normal, hypotenstion, or hypertention.
# The number of trials is determined by user input

import random, math

# user inputs the number of trials
N = int(input('Enter the number of simulations: '))
H = 0
N_m = 0
H_y = 0

# randomly generate numbers based on the trials
for i in range (N):
    flip = random.randint(65,140)
    if flip > 90:
        H = H + 1
    elif 90 <= flip < 120:
        N_m = N_m + 1
    else:
        H_y = H_y + 1
    
# print final calulations
print("The number of Hypotension scenarios ", H)
print("The number of Normal blood pressure ", N_m)
print("The number of Hypertension scenarios ", H_y)
