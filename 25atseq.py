# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers
import random
length = 30 
at = ['A','T']
gc = ['G','C']
dna = ''
for i in range(length):
	n = random.random()
	if n >= 0.6 and n <= 1:
		nt = random.choice(gc)
		dna += nt
	else:
		nt = random.choice(at)
		dna += nt
at_count = 0
for i in range(len(dna)):
	nuc = dna[i]
	if nuc == 'A':
		at_count += 1
	elif nuc == 'T':
		at_count += 1
		
ncount = len(dna)
percentat = str(at_count/ncount)

print(len(dna),percentat,dna)


	


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
