##########################################################################
# command : python mgeScanForm.py [cdhit cluster file] [MGEScan output]  #
##########################################################################

__author__ = "hjgwak"
__version__ = "1.0.4"

import sys

def printUSAGE() :
	print """
##########################################################################
# command : python mgeScanForm.py [cdhit cluster file] [MGEScan output]  #
##########################################################################
"""

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def makeHash(_file) :
	res = {}
	mge = open(_file, "r")
	
	for line in mge.readlines() :
		line = line.rstrip('\r\n')
		if line[1:] != "----------" :
			split = line.split('\t')
			res[split[0]] = line
	mge.close()
	return res


if len(sys.argv) != 3 :
	printUSAGE()
	exit(0)

out = open(getFileName(sys.argv[1]) + ".ltrout", "w")
mge = makeHash(sys.argv[2])

cdhit = open(sys.argv[1], "r")

cnt = 0;

for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == ">" :
		cnt += 1
		out.write(str(cnt) + "----------\n")
	else :
		split = line.split(' ')
		key = split[1][1:-3]
		if key[-1] == 'S' or key[-1] == 'M' :
			key = key[:-1]
		re = mge[key].split('\t')
		if split[2][0] == '*' :
			re.append(split[2])
		else :
			comp = split[3].split('/')
#			re[5] = comp[1]
			re.append(comp[2])
			re.append(comp[3])
			re.append(comp[1])
		out.write('\t'.join(re) + '\n')

out.close()
cdhit.close()
