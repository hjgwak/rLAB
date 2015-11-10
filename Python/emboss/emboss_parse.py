#########################################################################
# python emboss_parse.py file_name
#    format : needle | water
# output :
#    seq1_name    seq2_name    identity    similarity    align_length
#########################################################################

import sys

def printUSAGE() :
	print """
#########################################################################
# python emboss_parse.py file_name
#    format : needle | water
# output :
#    seq1_name    seq2_name    identity    similarity    align_length
#########################################################################
"""

# main

if len(sys.argv) != 2 or sys.argv[-1] == '-h' :
	printUSAGE()
	exit(0)

_file = open(sys.argv[1], 'r')

line = _file.readline()

seq1 = ""
seq2 = ""
length = ""
identity = ""
similarity = ""

print 'asequence\tbsequence\tidentity\tsimilarity\talign_length\n'

while line :
	line = line.rstrip('\n')

	if line.startswith('# 1:') :
		seq1 = line.split(': ')[1]
	elif line.startswith('# 2:') :
		seq2 = line.split(': ')[1]
	elif line.startswith('# Identity:') :
		temp = line.split(' ')
		for item in temp :
			if item.startswith('(') :
				identity = item[1:-1]
	elif line.startswith('# Similarity') :
		temp = line.split(' ')
		for item in temp :
			if item.startswith('(') :
				similarity = item[1:-1]
	elif line.startswith('# Length:') :
		length = line.split(': ')[1]
	elif line.startswith('# Score:') :
		print seq1 + "\t" + seq2 + "\t" + identity + "\t" + similarity + "\t" + length

	line = _file.readline()
