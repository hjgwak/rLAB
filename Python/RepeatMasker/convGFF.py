import sys

if len(sys.argv) < 3 :
	print "python convGFF.py [original fasta file] [GFF file]"
	exit()
	
fasta = open(sys.argv[1], "r")
gff = open(sys.argv[2], "r")
out = open("out.gff", "w")

dic = {}
fasta_line = fasta.readline()
while fasta_line :
	if fasta_line[0] == ">" :
		dic[fasta_line.split(' ')[0][1:]] = fasta_line.split(' ')[-5]
	fasta_line = fasta.readline()
fasta.close()

for i in range(3) :
	gff_line = gff.readline()
	print >>out, gff_line[:-1]

gff_line = gff.readline()
while gff_line :
	split = gff_line.split('\t')
	split[0] = dic[split[0]]
	res = '\t'.join(split)
	print >>out, res[:-1]
	gff_line = gff.readline()
gff.close()
out.close()
