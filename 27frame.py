# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA

# Variation: try coding this with a single loop and nested loops

# Note: use 0-based indexing for position and frame (biology uses 1-based)
position = 0
frame = -1
dna = 'ATGGCCTTT'

for i in range(len(dna)):
	position += 1 
	frame += 1
	nt = dna[i]
	if frame >= 3:
		frame = 0
		print(f'{position-1} {frame} {nt}')
	else:
		print(f'{position-1} {frame} {nt}')
	

"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
