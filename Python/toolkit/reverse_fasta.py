import sys

__author__ = "hjgwak"
__version__ = "1.0.1"

def printUSAGE() :
	print """
###########################################################
# python reverse_fasta.py {-reverse/-minus} fasta_file
#     -reverse	:	print reverse complement seq (e.g. AGTC -> TCAG)
#     -minus	:	print minus seq (e.g. AGTC -> CTGA)
# output : reverse complement fasta file
###########################################################
"""

def makeSeqHash(fasta) :
	fasta_f = open(fasta, 'r')
	res = {}

	first = True
	seq = ""
	name = ""
	for line in fasta_f.readlines() :
		line = line.rstrip('\r\n')
		if line[0] == ">" :
			if not first :
				res[name] = seq
			first = False
			name = line[1:]
			seq = ""
		else :
			seq += line
	res[name] = seq

	fasta_f.close()
	return res

def makeReverseComplement(seq) :
	seq = seq.upper()
	res_seq = ""
	watson_crick_pair = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
	for amino_acid in seq :
		if amino_acid in watson_crick_pair :
			res_seq += watson_crick_pair[amino_acid]
		else :
			res_seq += amino_acid

	return res_seq

def makeMinusSeq(seq) :
	return seq[::-1]

# main

ori_fasta = makeSeqHash(sys.argv[-1])
res_fasta = {}

if "-reverse" in sys.argv :
	for name in ori_fasta :
		res_fasta[name] = makeReverseComplement(ori_fasta[name])
elif "-minus" in sys.argv :
	for name in ori_fasta :
		res_fasta[name] = makeMinusSeq(ori_fasta[name])
else :
	print "wrong input options!"
	exit(-1)

for name in res_fasta :
	print '>' + name
	print res_fasta[name]
