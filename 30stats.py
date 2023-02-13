# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

count = 0
mean = 0 
summation = 0
sumsquare = 0
dataset =[]
for i in sys.argv[1:]:
	summation += float(i)
	dataset.append(float(i))

count = len(sys.argv)-1
minimum = min(sys.argv)
maximum = max(sys.argv)
mean = summation/count
dataset.sort()

for j in range(count):
	currentnum = dataset[j]
	sumsquare += ((currentnum - mean)**2)
if count % 2 == 0: 
	median1 = dataset[count//2]
	median2 = dataset[count//2-1]
	median = (median1 + median2)/2
else:
	median = dataset[count//2]
stddev = (sumsquare/count)**0.5
print('Count:', count)
print ('Minimum:',float(minimum)) 
print('Maximum:',float(maximum))
print('Mean',f'{mean:.3f}')
print('Std. dev:',f'{stddev:.3f}')
print('Median:', f'{median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
