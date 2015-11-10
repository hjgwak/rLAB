###########################################################
# python make_cdhitdb.py [cluster file directory]
# Input : A set of fasta files
# Output : A set of blastdb files
###########################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import sys, os, glob

def printUSAGE() :
	print """
###########################################################
# python make_cdhitdb.py [cluster file directory]
# Input : A set of fasta files
# Output : A set of blastdb files
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

cdhits = glob.glob(makeDirForm(sys.argv[1]) + "*")

for cdhit in cdhits :
	os.system("makeblastdb -in " + cdhit + " -input_type fasta -dbtype nucl -out " + getFileName(cdhit))
