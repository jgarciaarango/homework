# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input
import sys
import math

dataset =[]
values = []
sum = 0
for i in sys.argv[1:]:
	dataset.append(float(i))
	
for j in range(len(dataset)):
	currentnum = dataset[j] 
	currentcalc = currentnum * (math.log2(currentnum))
	sum += currentcalc
	values.append(currentcalc)
	

print(f'{sum*-1:.4}')
	
	

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
