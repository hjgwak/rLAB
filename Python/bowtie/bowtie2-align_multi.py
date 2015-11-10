import sys, os, glob

__author__ = "hjgwak"
__version__ = "1.0.3"

def printUSAGE() :
	print """
###########################################################
# python bowtie2-align_multi.py [-U/-P] [-x option] [read dir] [options]
# Options :
#     [-U/-P]	:	-U : single-end alignment (read.fastaq)
#     				-P : paired-end alignment (read_1.fastaq, read_2.fastaq)
#     -quiet	:	Do not print error message in stderr
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

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit()

if len(sys.argv) < 4 :
	printUSAGE()	
	exit()

x = sys.argv[2]
quiet = False
if '-quiet' in sys.argv :
	quiet = True

if sys.argv[1] == '-U' :
	reads = glob.glob(makeDirForm(sys.argv[3]) + "*.fastq") + glob.glob(makeDirForm(sys.argv[3]) + "*.fq")
	
	for read in reads :
		read_name = getFileName(read)
		read_name = read_name[:read_name.find('.')]
		os.system("bowtie2 -x " + x + " -U " + read + " -S " + read_name + ".sam")
else :
	reads_1 = glob.glob(makeDirForm(sys.argv[3]) + "*_1.fastq") + glob.glob(makeDirForm(sys.argv[3]) + "*_1.fq")
	reads_2 = glob.glob(makeDirForm(sys.argv[3]) + "*_2.fastq") + glob.glob(makeDirForm(sys.argv[3]) + "*_2.fq")
	reads_1.sort()
	reads_2.sort()

	if len(reads_1) != len(reads_2) :
		if not quiet :
			print >> sys.stderr, "paired sequences does not match!"
		exit()

	i = 0
	while i < len(reads_1) :
		if not quiet :
			print >> sys.stderr, "bowtie2 starts with " + reads_1[i] + " and " + reads_2[i]
		read_name_1 = getFileName(reads_1[i])
		read_name_1 = read_name_1[:read_name_1.find('_')]
		read_name_2 = getFileName(reads_2[i])
		read_name_2 = read_name_2[:read_name_2.find('_')]

		if read_name_1 != read_name_2 :
			if not quiet :
				print >> stderr, "reads list doesn't sorted!"
				exit()

		cmd = "bowtie2 -x " + x + " -1 " + reads_1[i] + " -2 " + reads_2[i] + " -S " + read_name_1 + ".sam"
		if quiet :
			cmd += " --quiet"
		os.system(cmd)
		i += 1
