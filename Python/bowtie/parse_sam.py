###########################################################
# python parse_sam.py [options] [bowtie output]
# options :
#     -NM	#	: Threshold of NM value (defualt 0)
###########################################################

import sys

__author__ = "hjgwak"
__version__ = "1.0.2"

def printUSAGE() :
	print """
###########################################################
# python parse_sam.py [options] [bowtie output]
# options :
#     -NM	#	: Threshold of NM value (defualt 0)
#     -out	str	: out file (default stdout)
###########################################################
"""

def parseOpts(options) :
	res = {"-NM" : '0', "-out" : "stdout"}
	idx = 0
	while idx < len(options) :
		if options[idx] in res :
			res[options[idx]] = options[idx+1]
		idx += 2

	return res

def findNM(field) :
	res = -1
	for item in field :
		if item.startswith("NM") :
			res = int(item.split(':')[-1])
			break

	return res

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit()

if len(sys.argv) < 2 :
	printUSAGE()
	exit()

sam = open(sys.argv[-1], 'r')
options = sys.argv[1:-1]

Threshold = parseOpts(options)

w_f = False
if Threshold["-out"] != "stdout" :
	sys.stdout = open(Threshold["-out"], 'w')
	w_f = True

for line in sam.readlines() :
	line = line.rstrip('\r\n')
	split = line.split('\t')

	if line[0] == '@' :
		continue

	if split[2] == '*' :
		continue
	# 0x4 flag means 'segment unmapped'
	if int(split[1]) & 0x4 :
		continue
	NM = findNM(split)
	if NM != -1 and NM <= int(Threshold["-NM"]) :
		print "\t".join(split[:9] + split[11:])

sam.close()
if w_f :
	sys.stdout.close()
