import sys

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

if '-h' in sys.argv or len(sys.argv) < 3 :
	print "python parsePrimer.py [fna file] [primer output]"
	exit(0)

seqs = readSeqsFromFile(sys.argv[-2])

primer = open(sys.argv[-1], 'r')

seq_id = ""
for line in primer.readlines() :
	line = line.rstrip('\r\n')
	if line.startswith('SEQUENCE_ID=') :
		seq_id = line.split('=')[1]
	elif line.startswith('PRIMER_PAIR_NUM_RETURNED=') :
		if line.split('=')[1] == '0' :
			del seqs[seq_id]
primer.close()

keys = seqs.keys()
keys.sort()
for key in keys :
	print ">" + key
	print seqs[key]
