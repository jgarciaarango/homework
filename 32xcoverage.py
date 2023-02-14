# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below
import sys 
import random 

genome = int(sys.argv[1])
readnum = int(sys.argv[2])
readlen = int(sys.argv[3])

coverage = [0]*genome
for i in range(0,readnum):
	start = random.randint(0, genome - readlen)
	for j in range(start, start + readlen):
		coverage[j]+=1
#get rid of undersampled regions takes of the first and last 10 percent of genome
coverage_no_ends = coverage[(0+(genome//90)):(genome-(genome//90))]
		
print(min(coverage_no_ends),max(coverage_no_ends),f'{sum(coverage_no_ends)/len(coverage_no_ends):0.7}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
