# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
import math
dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'
gc_count = 0.0
for i in range(len(dna)):
	nt = dna[i]
	if nt == 'G':
		gc_count += 1
	elif nt == 'C':
		gc_count += 1
		
ncount = len(dna)
percentgc = gc_count/ncount
#print(percentgc)
print (f'{percentgc:.2f}')

	

"""
python3 24gc.py
0.42
"""
