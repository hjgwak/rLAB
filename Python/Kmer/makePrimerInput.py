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

def makeReverseComplement(seq) :
	comple = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G', 'N' : 'N'}
	reverse = seq[::-1]
	#complement
	complement = ""
	for char in reverse :
		complement += comple[char]

	return complement

# main

if len(sys.argv) != 2 :
	print "python makePrimerInput.py [fna file]"
	exit(-1)

seqs = readSeqsFromFile(sys.argv[-1])

keys = seqs.keys()
for key in keys :
	print "SEQUENCE_ID=" + key
	print "SEQUENCE_TEMPLATE=" + seqs[key]
	print "SEQUENCE_PRIMER=" + seqs[key][:20]
#	print "SEQUENCE_PRIMER_REVCOMP=" + seqs[key][-20:]
	print "SEQUENCE_PRIMER_REVCOMP=" + makeReverseComplement(seqs[key][-20:])
	print "PRIMER_TASK=pick_detection_primers"
	print "PRIMER_PICK_LEFT_PRIMER=1"
#	print "PRIMER_PICK_INTERNAL_OLIGO=0"
	print "PRIMER_PICK_RIGHT_PRIMER=1"
	print "PRIMER_OPT_SIZE=20"
	print "PRIMER_MIN_SIZE=20"
	print "PRIMER_MAX_SIZE=20"
#	print "PRIMER_MAX_NS_ACCEPTED=1"
	print "PRIMER_PRODUCT_SIZE_RANGE=150-200"
	print "P3_FILE_FLAG=0"
	print "PRIMER_EXPLAIN_FLAG=1"
	print "PRIMER_THERMODYNAMIC_PARAMETERS_PATH=/program/primer3-2.3.6/src/primer3_config/"
	print "="
