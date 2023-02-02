# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
antiparallel = ''
for i in range(len(dna)):
	nt = dna[i] 
	if nt == 'A' :
		antiparallel += 'T'
	elif nt == 'T':
		antiparallel += 'A'
	elif nt == 'G':
		antiparallel += 'C'
	else:
		antiparallel += 'G' 
print(antiparallel[::-1])

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
