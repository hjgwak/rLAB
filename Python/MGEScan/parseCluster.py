#########################################################################
# Input cmd : python parseCluster.py [fasta directory] [MGEScan output] #
# Output :                                                              #
#    file_name = [cluster#]                                             #
#    sequence_head = sequence number                                    #
#    format =                                                           #
#        .all : all sequence from first ltr start to second ltr end     #
#        .first : first ltr sequence                                    #
#        .second : second ltr sequence                                  #
#        .domain : domain sequence                                      #
#########################################################################

__author__ = "hjgwak"
__version__ = "1.0.2"

import sys, os

def openOutput(prev, output, fmt) :
	common_name = 'cluster' + prev[:prev.find('-')]
	for i in range(4) :
		if output[i] != None :
			output[i].close()
			output[i] = None
	output[fmt['all']] = open(common_name + '.all', 'w')
	output[fmt['first']] = open(common_name + '.first', 'w')
	output[fmt['second']] = open(common_name + '.second', 'w')
	output[fmt['domain']] = open(common_name + '.domain', 'w')

	return output

def getSeqName(seq) :
	split = seq.split('_')
	split = split[:-1]
	return '_'.join(split)

def seqFileOpen(seq_name, directory) :
	seq_file = open(directory + seq_name, 'r')
	return seq_file

def writeSeq(sequence, start, end, head, target_file) :
	target_file.write(head + '\n')
	sub_seq = sequence[start: end]
	while len(sub_seq) >= 100 :
		target_file.write(sub_seq[:100] + '\n')
		sub_seq = sub_seq[100:]
	if len(sub_seq) != 0 :
		target_file.write(sub_seq + '\n')

def makeDir(name) :
	if (name in os.listdir('.')) == False :
		os.mkdir(name)

# main

if len(sys.argv) != 3 :
	print "python pareseCluster.py [fasta directory] [MGEScan output]"
	print "Your input : python " + ' '.join(sys.argv)
	exit(1)

# output[0] : all, output[1] : first, output[2] : second, output[3] : domain
fmt = {'all' : 0, 'first' : 1, 'second' : 2, 'domain' : 3}
output = [None, None, None, None]

mge_scan = open(sys.argv[2], 'r')
mge_line = mge_scan.readline()
prev = ""
prev_cluster = False

while mge_line :
	if mge_line.find('----------') != -1 :
		prev = mge_line
		prev_cluster = True
		mge_line = mge_scan.readline()
		continue
	else :
		if prev_cluster :
			output = openOutput(prev, output, fmt)
		
		mge_split = mge_line.split('\t')
		seq_name = getSeqName(mge_split[0])
		head = '>' + mge_split[0]
		seq_file = seqFileOpen(seq_name, sys.argv[1])
		seq_lines = seq_file.readlines()
		sequence = ""
		for seq in seq_lines[1:] :
			sequence += seq[:-1]
		seq_file.close()

		writeSeq(sequence, int(mge_split[1]), int(mge_split[4]), head, output[fmt['all']])
		writeSeq(sequence, int(mge_split[1]), int(mge_split[2]), head, output[fmt['first']])
		writeSeq(sequence, int(mge_split[3]), int(mge_split[4]), head, output[fmt['second']])
		writeSeq(sequence, int(mge_split[2])+1, int(mge_split[3])-1, head, output[fmt['domain']])

		prev_cluster = False
		prev = mge_line
		mge_line = mge_scan.readline()

mge_scan.close()
for i in range(4) :
	if output[i] != None :
		output[i].close()

makeDir("all")
makeDir("domain")
makeDir("second")
makeDir("first")
os.system("mv *.first first/")
os.system("mv *.second second/")
os.system("mv *.domain domain/")
os.system("mv *.all all/")
