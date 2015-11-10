import sys, os, glob

__author__ = "hjgwak"
__version__ = "1.0.1"

def printUSAGE() :
	print """
###########################################################
# python reverse_fasta_dir.py {-reverse/-minus} [fasta_dir]
###########################################################
"""

def makeDirForm(path) :
	if path[-1] != '/' :
		path += '/'
	return path

def getFileName(path) :
	return path.split('/')[-1]

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit(-1)

fastas = glob.glob(makeDirForm(sys.argv[-1]) + "*")

for fasta in fastas :
	os.system("python ~/Python/toolkit/reverse_fasta.py " + sys.argv[-2] + " " + fasta + " > " + getFileName(fasta))
