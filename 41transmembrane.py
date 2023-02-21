# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane
# Find if theres a signal peptide in the first 30 aa if not then stop 
import mcb185
import sys
	
def getkd(sequence):
	aa = ('ACDEFGHIKLMNPQRSTVWY')
	kd = [1.8, 2.5,-3.5,-3.5,2.8,-0.4,-3.2,4.5,-3.9,3.8,1.9,-3.5,-1.6,-3.5,-4.5,-0.8,-0.7,4.2,-0.9,-1.3]
	kdlist = 0
	for i in range(len(sequence)):
		currentaa = sequence[i]
		for j in range(len(aa)):
			if currentaa == aa[j]: 
				kdlist += kd[j] 
	return kdlist/len(sequence)
def hydrophobic(seq, w, t):
	for i in range(len(seq)- w + 1):
		window = seq[i:i+w]
		kd = getkd(window)
		if kd > t and 'P' not in window: return True
	return False

for name, seq, in mcb185.read_fasta(sys.argv[1]):
	nterm = seq[0:30]
	cterm = seq[30:]
	if hydrophobic(nterm, 8, 2.5) and hydrophobic(cterm, 11, 2.0):
		print(name)
"""
	

  
def checkalphahelix(sequence):
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
	
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
