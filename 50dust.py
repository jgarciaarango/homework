#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. the entropy of each window is centered (N's in the middle of windows)
# 2. has option and default value for window size
# 3. has option and default value for entropy threshold
# 4. has a switch for N-based or lowercase (soft) masking
# 5. works with uppercase or lowercase input files
# 6. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)
import argparse
import math 
import mcb185 
#Creating the different arguments 
parser = argparse.ArgumentParser(description = 'Entropy filtering on fasta')
parser.add_argument('file', type = str, metavar = '<path>', help= 'fasta file')
parser.add_argument('-w', required = False, type=int, default=11, metavar ='<int>', help ='optional interger argument [%(default)i]')
parser.add_argument('-t', required= False, type=float, default =1.4, metavar='<float>',help = 'optional float argument [%(default).3f]')
parser.add_argument('-s', action = 'store_true', help = 'lower-case masking')
arg = parser.parse_args() 
#function that calculates the shannon entropy value for a frequency distribution 
def entropy(val):
	assert(math.isclose(1.0,sum(val)))
	ent = 0
	for p in val:
		if p != 0:
			ent += p * math.log2(p)
	return ent*-1 
#Creates a ditribution for the frequency of basepairs and then returns the entropy value
#making sure the entropy function works with lowercase
def ntentropy(seq):
	A = seq.count('A')/len(seq)
	T = seq.count('T')/len(seq)
	C = seq.count('C')/len(seq)
	G = seq.count('G')/len(seq)
	shannon = entropy([A, T, C, G])
	return shannon 
#declare the arguments as variables 
file = arg.file
window = arg.w
threshold = arg.t
center = window//2
for name, seq, in mcb185.read_fasta(file):
	seq = seq.upper()
	seqlist = list(seq)
	for i in range(len(seq)-window+1):
		ent = ntentropy(seq[i:i+window])
		if ent < threshold:
			if arg.s: seqlist[i+center] = seqlist[i+center].lower()
			else: seqlist[i] ='N'
	seq = ''.join(seqlist)
	print(f'>{name}')
	for j in range(0, len(seq), 60): 
		print(seq[j: j+60])
"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""
