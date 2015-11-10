import sys

if len(sys.argv) != 3 :
	print "python toGFF.py [output file] [sequence directory]"
	exit()

_file = open(sys.argv[1], 'r')
line = _file.readline()

print "##gff-version 3"

seq_file = None;
scaffold_name = "";
while line :
	if line[:5] == "-----" :
		seq_file = open(sys.argv[2] + line[5:-6], 'r')
		scaffold_name = seq_file.readline().split(' ')[8][:-1]
		seq_file.close()
	else :
		split = line.split('\t')
		out = scaffold_name + '\tMER\tLTR\t' + split[1] + '\t' + str(int(split[2]) + int(split[4])) + '\t'
		out += split[8] + '\t+\t.\tTYPE=' + split[0] + "; Similarity=" + split[7] + ";"
		print out
	line = _file.readline()

_file.close()
