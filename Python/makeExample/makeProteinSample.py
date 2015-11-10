##################################################################################
# Input Commad : python makeProteinSample.py [Options] <Core Values>             #
# Core Values :                                                                  #
#     -pt, protein file           : MULTI_FASTA file that has protein seq.       #
#     -num, number of proteins    : Number of proteins for making samples        #
#     -r, random seq.             : Length of random seq. that will merge both   #
#                                   right and left side of protein               #
# Options :                                                                      #
#     -s, start position          : start with #th protein in file(Default is 0) #
#     -o, output                  : write result in this file(Default is stdout) #
#     -h, help                    : print usage                                  #
# Output : MULTI_FASTA file                                                      #
##################################################################################

import sys, random, hj_toolkit

def printUSAGE() :
	print """
##################################################################################
# Input Commad : python makeProteinSample.py [Options] <Core Values>             #
# Core Values :                                                                  #
#     -pt, protein file           : MULTI_FASTA file that has protein seq.       #
#     -num, number of proteins    : Number of proteins for making samples        #
#     -r, random seq.             : Length of random seq. that will merge both   #
#                                   right and left side of protein               #
# Options :                                                                      #
#     -s, start position          : start with #th protein in file(Default is 0) #
#     -o, output                  : write result in this file(Default is stdout) #
#     -h, help                    : print usage                                  #
# Output : MULTI_FASTA file                                                      #
##################################################################################
"""

def checkValidArgument(argv) :
	if argv.has_key('-pt') == False or argv.has_key('-num') == False or argv.has_key('-r') == False :
		print "\nCore values are missed, check your command!"
		print hj_toolkit.makeCMD(sys.argv)
		exit(1)
	elif len(argv) == 4 and argv.has_key('-s') == False and argv.has_key('-o') == False :
		print "\nUnknown options, check your command!"
		print hj_toolkit.makeCMD(sys.argv)
		exit(1)
	elif len(argv) == 5 and (argv.has_key('-s') == False or argv.has_key('-o') == False) :
		print "\nUnknown options, check your command!"
		print hj_toolkit.makeCMD(sys.argv)
		exit(1)

def writeString(string) :
	while len(string) > 100 :
		print string[:100]
		string = string[100:]
	if len(string) != 0 :
		print string

def makeRandomSeq(length) :
	nucleotides = ['A', 'G', 'T', 'C']
	seq = ""
	for i in range(length) :
		seq += random.choice(nucleotides)
	return seq

def makeSequences(pt_file, argv) :
	skip = 0
	if argv.has_key('-s') :
		skip = int(argv['-s'])
	
	line = pt_file.readline()
	seq_cnt = 0
	while seq_cnt < skip :
		line = pt_file.readline()
		if line[0] == '>' :
			seq_cnt += 1

	for i in range(int(argv['-num'])) :
		pt_name = line
		seq = makeRandomSeq(int(argv['-r']))
		line = pt_file.readline()
		while line != "" and line[0] != '>' :
			seq += line[:-1]
			line = pt_file.readline()
		seq += makeRandomSeq(int(argv['-r']))
		print pt_name[:-1]
		writeString(seq)

#Main part of program

if len(sys.argv) != 1 and sys.argv[1] == '-h' :
	printUSAGE()
	exit(1)
elif len(sys.argv) < 4 :
	print "Too short arguments! check your command!"
	print "\n" + hj_toolkit.makeCMD(sys.argv)
	exit(1)
elif len(sys.argv) > 6 :
	print "Too long arguments! check your commad!"
	print "\n" + hj_toolkit.makeCMD(sys.argv)
	exit(1)

argv = hj_toolkit.parseArgument(sys.argv)
checkValidArgument(argv)

pt_file = open(argv['-pt'], "r")
if argv.has_key('-o') :
	sys.stdout = open(argv['-o'], "w")

makeSequences(pt_file, argv)

pt_file.close()
