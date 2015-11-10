###########################################################
# python filter.py [options] [sim file directory] [emboss output directory]
# options :
#     -T (float)   : Threshold of difference [default 2.0]
###########################################################

import sys, os, glob

def printUSAGE() :
	print """
###########################################################
# python filter.py [options] [sim file directory] [emboss output directory]
# options :
#     -T    : Threshold of difference [default 2.0]
###########################################################
"""

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def checkValidation(_list, cur, th) :
	res = True
	for item in _list :
		if item + th < cur or item - th > cur :
			res = False
			break
	return res

# main

if len(sys.argv) < 3 or len(sys.argv) > 5 :
	printUSAGE()
	exit()

threshold = 2.0

options = sys.argv[1:-2]

idx = 0
while idx < len(options) :
	try :
		if options[idx] == "-T" :
			threshold = float(options[idx + 1])
	except IndexError :
		print "Lack of options!"
		printUSAGE()
		exit()
	else :
		idx += 2

sims = glob.glob(makeDirForm(sys.argv[-2]) + "*.sim")

res_list = []
for sim in sims :
	_file = open(sim, 'r')
	identity_list = []
	near = True
	for line in _file.readlines() :
		print line
		comp = line.split('\t')
		if comp[0] == comp[1] :
			continue
		identity_list.append(float(comp[2]))
		if checkValidation(identity_list, float(comp[2]), threshold) == False :
			near = False
			break
	if near and len(identity_list) > 1 :
		res_list.append(".".join(getFileName(sim).split('.')[:-1]))
	_file.close()

for res in res_list :
	os.system("cp " + makeDirForm(sys.argv[-1]) + res + " " + makeDirForm(sys.argv[-2]) + res + ".sim ./")
