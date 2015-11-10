import sys

fasta = open(sys.argv[1], 'r')

cnt = 0

for line in fasta.readlines() :
	if line[0] == ">" :
		cnt += 1

print cnt

fasta.close()
