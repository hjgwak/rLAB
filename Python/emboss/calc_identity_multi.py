###########################################################
# python calc_identity_multi.py [emboss output directory]
# Input format : *.needle | *.water
# Output format : *.sim
###########################################################

import sys, os, glob

def printUSAGE() :
	print """
###########################################################
# python calc_identity_multi.py [emboss output directory]
# Input format : *.needle | *.water
# Output format : *.sim
###########################################################
"""

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

# main

if len(sys.argv) != 2 :
	printUSAGE()
	exit()

files = glob.glob(makeDirForm(sys.argv[1]) + "*")

for _file in files :
	os.system("python ~/Python/emboss/calc_identity.py " + _file + " > " + getFileName(_file) + ".sim")
