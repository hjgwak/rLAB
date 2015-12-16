import sys

def printUSAGE() :
	print """
###########################################################
# python rmHighBlast [m6 output] [fna file]
###########################################################
"""

def readSeqsFromFile(fasta_n) :
	fasta_f = open(fasta_n, 'r')
	res = {}
	name = ""
	seq = ""
	for line in fasta_f.readlines() :
		line = line.rstrip()
		if line[0] == '>' :
			if name != "" and seq != "" :
				res[name] = seq
			name = line[1:]
			seq = ""
		else :
			seq += line
	if name != "" and seq != "" :
	 	res[name] = seq
	fasta_f.close()
	return res

# main

if len(sys.argv) != 3 :
	printUSAGE()
	exit(-1)

blast = open(sys.argv[-2], 'r')
seqs = readSeqsFromFile(sys.argv[-1])

for line in blast.readlines() :
	line = line.rstrip('\r\n')
	split = line.split('\t')
	if split[0] in seqs :
		del seqs[split[0]]

keys = seqs.keys()
keys.sort()
for key in keys :
	print '>' + key
	print seqs[key]

blast.close()
