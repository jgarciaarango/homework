# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()
import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description = 'Get the kmer counts in a fasta file for a given size of k')
parser.add_argument('file', type = str, metavar = '<path>', help= 'fasta file')
parser.add_argument('-k', required = False, type=int, default=2, metavar ='<int>', help='Optional argument for size of k [%(default)i]')
arg = parser.parse_args()

filename = arg.file
k = arg.k

nts ={}

nts['A'] = 0 
nts['T'] = 0 
nts['C'] = 0 
nts['G'] = 0 

total = 0
nt2 = {}
for name, seq in mcb185.read_fasta(filename):
	for i in range(len(seq)-k+1):
		kmer = seq[i:i+k]
		if kmer not in nt2: 
			nt2[kmer]=0
		nt2[kmer]+= 1
kkmer = list(nt2.keys())
kkmer.sort()
sortedkmer = {i: nt2[i] for i in kkmer}
print(sortedkmer)





"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
