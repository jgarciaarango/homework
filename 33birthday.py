# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list
import sys
import random 

count = 0 
dayrange = [0] * int(sys.argv[1])
birthdays = []
simulations = 100
#Runs a set number of simulations
for i in range(simulations):
#Create a list with random birthdays 
	for j in range(int(sys.argv[2])):
		day = random.randint(0,int(sys.argv[1])-1)
		birthdays.append(day)
#Check if any birthdays are the same 
	for k in range(len(birthdays)):
		currentbday = birthdays[k]
		check = birthdays.count(currentbday)
		if check > 1:
			count += 1
			break
	birthdays = []
probability = (count)
print(f'{count/simulations:.3}')
"""
python3 33birthday.py 365 23
0.571
"""

