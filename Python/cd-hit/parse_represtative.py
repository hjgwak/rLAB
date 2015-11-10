import sys

__author__ = "hjgwak"
__version__ = "1.0.2"

def makeSeqHash(argv) :
	fasta = open(argv, 'r')
	prev = ""
	seq = ""

	dic = {}
	for line in fasta.readlines() :
		line = line.rstrip('\r\n')
		if line[0] == '>' :
			if prev != "" :
				dic[prev] = seq
				seq = ""
			prev = line
		else :
			seq += line
	if seq != "" :
		dic[prev] = seq
	fasta.close()

	return dic

# main

if len(sys.argv) < 3 :
	print """
python parse_representative.py [options] [fasta file] [cd-hit output]
options :
    -SM    :    print additional information of singleton/multiple
"""
	exit()

seqs = makeSeqHash(sys.argv[-2])

cdhit = open(sys.argv[-1], 'r')

SM = False
if "-SM" in sys.argv :
	SM = True

cnt = 0
representative = ""

for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == '>' :
		if representative != "" :
			key = representative
			if key[-1] == 'S' or key[-1] == 'M' :
				key = key[:-1]
			if SM :
				if cnt == 1 :
					representative += 'S'
				else :
					representative += 'M'
			print representative
			print seqs[key]
		representative = ""
		cnt = 0
	else :
		cnt += 1
		if line.split(' ')[2] == '*' :
			representative = line.split(' ')[1][:-3]

if representative != "" :
	key = representative
	if key[-1] == 'S' or key[-1] == 'M' :
		key = key[:-1]
	if SM :
		if cnt == 1 :
			representative += 'S'
		else :
			representative += 'M'
	print representative
	print seqs[key]

cdhit.close()
