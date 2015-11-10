###########################################################
# python muscle_multi.py [muscle options] <input dir>
# Option :
#    -diags	                Find diagonals (faster for similar sequences)
#    -maxiters	<n>         Maximum number of iterations (integer, default 15)
#    -maxhours	<h>         Maximum time to iterate in hours (default no limit)
#    -html                  Write output in HTML format (default FASTA)
#    -msf                   Write output in GCG MSF format (default FASTA)
#    -clw                   Write output in CLUSTALW format (default FASTA)
#    -clwstrict             As -clw, with 'CLUSTAL W (1.81)' header
#    -log[a]	<logfile>   Log to file (append if -loga, overwrite if -log)
#    -quiet                 Do not write progress messages to strerr
#    -version               Display version information and exit
#    -h[elp]                Display USAGE and exit
# Automaric optoins :
#    -in     all files in <input dir>
#    -out    [input file name].muscle
###########################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import sys, os, glob

def printUSAGE() :
	print """
###########################################################
# python muscle_multi.py [muscle options] <input dir>
# Option :
#    -diags	                Find diagonals (faster for similar sequences)
#    -maxiters	<n>         Maximum number of iterations (integer, default 15)
#    -maxhours	<h>         Maximum time to iterate in hours (default no limit)
#    -html                  Write output in HTML format (default FASTA)
#    -msf                   Write output in GCG MSF format (default FASTA)
#    -clw                   Write output in CLUSTALW format (default FASTA)
#    -clwstrict             As -clw, with 'CLUSTAL W (1.81)' header
#    -log[a]	<logfile>   Log to file (append if -loga, overwrite if -log)
#    -quiet                 Do not write progress messages to strerr
#    -version               Display version information and exit
#    -h[elp]                Display USAGE and exit
# Automaric optoins :
#    -in     all files in <input dir>
#    -out    [input file name].muscle
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

if len(sys.argv) < 2 or len(sys.argv) > 9 :
	printUSAGE()
	exit(0)

if "-h" in sys.argv or "-help" in sys.argv :
	printUSAGE()
	exit(0)

inputs = glob.glob(makeDirForm(sys.argv[-1]) + "*")
options = " ".join(sys.argv[1:-1])

for fasta in inputs :
	cmd = "/program/muscle3.8.31_i86linux64 -in " + fasta + " -out " + getFileName(fasta) + ".muscle " + options
	os.system(cmd)
