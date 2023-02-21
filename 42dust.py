# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)
import sys 
import math 
import mcb185 
def entropy(val):
	assert(math.isclose(1.0,sum(val)))
	ent = 0
	for p in val:
		if p != 0:
			ent += p * math.log2(p)
	return ent*-1 
def ntentropy(seq):
	A = seq.count('A')/len(seq)
	T = seq.count('T')/len(seq)
	C = seq.count('C')/len(seq)
	G = seq.count('G')/len(seq)
	shannon = entropy([A, C, T, G])
	return shannon 
window = int(sys.argv[2])
threshold = float(sys.argv[3])
for name, seq, in mcb185.read_fasta(sys.argv[1]):
	seqlist = list(seq)
	for i in range(len(seq)-window+1):
		ent = ntentropy(seq[i:i+window])
		if ent < threshold:
			seqlist[i] ='N'
	seq = ''.join(seqlist)
	print(seq)
"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
