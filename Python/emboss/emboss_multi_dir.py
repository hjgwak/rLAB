###################################################################
# python needle_multi_dir.py [options] fasta directory program
# options :
#     -gapopen     : 10.0 default
#     -gapextend   : 0.5 default
#     -endopen     : 10.0 defualt
#     -endextend   : 0.5 default
# program : required
#     needle
#     water
# ouput : [each file name].needle
###################################################################

__author__ = "hjgwak"
__version__ = "1.0.3"

import sys, os, glob

def printUSAGE() :
	print """
###################################################################
# python needle_multi_dir.py [options] fasta directory program
# options :
#     -gapopen     : 10.0 default
#     -gapextend   : 0.5 default
#     -endopen     : 10.0 defualt
#     -endextend   : 0.5 default
# program : required
#     needle
#     water
# ouput : [each file name].needle
###################################################################
"""

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

# main

if len(sys.argv) < 3 or len(sys.argv) > 7 or sys.argv[-1] == "-h" :
	printUSAGE()
	exit(0)

files = glob.glob(makeDirForm(sys.argv[-2]) + "*")

options = sys.argv[1:-2]

gapopen = '10.0'
gapextend = '0.5'
endopen = '10.0'
endextend = '0.5'

for option in options :
	detail = option.split("=")
	if detail[0] == "-gapopen" :
		gapopen = detail[1]
	elif detail[0] == "-gapextend" :
		gapextend = detail[1]
	elif detail[0] == "-endopen" :
		endopen = detail[1]
	elif detail[0] == "-endextend" :
		endextend = detail[1]
	else :
		print "Wrong Option!!"
		printUSAGE()
		exit(1)

prog = ""
if sys.argv[-1] == 'needle' :
	prog = "~/EMBOSS-6.6.0/emboss/needle "
elif sys.argv[-1] == 'water' :
	prog = "~/EMBOSS-6.6.0/emboss/water "
else :
	print "Wrong Program!!"
	printUSAGE()
	exit(2)

for _file in files :
	cmd = prog + "-asequence " + _file + " -bsequence " + _file + " -gapopen " + gapopen + " -gapextend " + gapextend + " -outfile " + getFileName(_file) + "." + sys.argv[-1]
	if sys.argv[-1] == 'needle' :
		cmd += " -endopen " + endopen + " -endextend " + endextend
	os.system(cmd)
