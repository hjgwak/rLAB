#############################################################
# Input : python ltr_sim.py [parseMGE dir] [MGEScan output] #
# Notice : You can do preprocessing using 'parseCluster.py' #
# Align Options :
#     -gapopen    float   : gap open penalty 1.0 to 100.0 (default 10.0)
#     -gapextend  float   : gap extend penalty 0.0 to 10.0 (default 0.5)
#     -endopen    float   : end open penalty 1.0 to 100.0 (default 10.0)
#     -endextend  float   : end extend penalty 0.0 to 10.0 (default 0.5)
# Output : res.ltrout
#############################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import sys, os

def printUSAGE() :
	print """
#############################################################################
# Input : python ltr_sim.py [align options] [parseMGE dir] [MGEScan output]
# Notice : You can do preprocessing using 'parseCluster.py'
# Align Options :
#     -gapopen    float   : gap open penalty 1.0 to 100.0 (default 10.0)
#     -gapextend  float   : gap extend penalty 0.0 to 10.0 (default 0.5)
#     -endopen    float   : end open penalty 1.0 to 100.0 (default 10.0)
#     -endextend  float   : end extend penalty 0.0 to 10.0 (default 0.5)
# Output : res.ltrout
#############################################################################
"""

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def parseOption(opts) :
	opt = {"-gapopen" : "10.0", "-gapextend" : "0.5", "-endopen" : "10.0", "-endextend" : "0.5"}
	idx = 0
	while idx < len(opts) :
		opt[opts[idx]] = opts[idx+1]
		idx += 2
	
	return opt

def makeHash(name) :
	res = {}
	fasta = open(name, "r")

	name = ""
	seq = ""
	for line in fasta.readlines() :
		line = line.rstrip("\r\n")
		if line[0] == ">" :
			if name != "" and seq != "" :
				res[name] = seq
			name = line[1:]
			seq = ""
		else :
			seq += line
	if name != "" and seq != "" :
		res[name] = seq

	fasta.close()

	return res

def makeFastaFile(file_name, name, seq) :
	fasta = open(file_name, "w")
	fasta.write(">" + name + "\n")
	fasta.write(seq)
	fasta.close()

def runEMBOSS(options) :
	cmd = "~/EMBOSS-6.6.0/emboss/needle -asequence ltr_sim_temp/first.fa -bsequence ltr_sim_temp/second.fa "
	cmd += "-gapopen " + options["-gapopen"] + " -gapextend " + options["-gapextend"] + " -outfile ltr_sim_temp/needle.out "
	cmd += "-endopen " + options["-endopen"] + " -endextend " + options["-endextend"]
	os.system(cmd)

def getSim() :
	needle = open("ltr_sim_temp/needle.out", 'r')
	line = needle.readline()
	while line :
		if "Identity" in line :
			break
		line = needle.readline()
	line = line.rstrip('\r\n')
	needle.close()
	return line.split(' ')[-1][1:-1]

# main

if "-h" in sys.argv or "-help" in sys.argv :
	printUSAGE()
	exit(0)

if len(sys.argv) > 11 or len (sys.argv) < 3 :
	printUSAGE()
	exit(-1)

if ("ltr_sim_temp" in os.listdir('.')) == False :
	os.mkdir("ltr_sim_temp")

mge = open(sys.argv[-1], "r")
options = parseOption(sys.argv[1:-2])

clstr_num = "0"
first_dic = {}
second_dic = {}

sys.stdout = open("res.ltrout", 'w')

for line in mge.readlines() :
	line = line.rstrip('\r\n')
	if line[-10:] == "----------" :
		clstr_num = line[:-10]
		first_dic = makeHash(makeDirForm(sys.argv[-2]) + "first/cluster" + clstr_num + ".first")
		second_dic = makeHash(makeDirForm(sys.argv[-2]) + "second/cluster" + clstr_num + ".second")
		print line
	else :
		split = line.split("\t")
		makeFastaFile("ltr_sim_temp/first.fa", split[0], first_dic[split[0]])
		makeFastaFile("ltr_sim_temp/second.fa", split[0], second_dic[split[0]])
		runEMBOSS(options)
		split.append(getSim())
		print "\t".join(split)

sys.stdout.close()
mge.close()
