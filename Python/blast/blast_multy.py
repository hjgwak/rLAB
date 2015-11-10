###########################################################
#
# python blastn_multi.py [options] -db db_dir -query query_dir
#
# options : same in blastn
#
###########################################################

import sys, os, glob

def printUSAGE() :
	print """
###########################################################
#
# python blastn_multi.py [options] -db db_dir -query query_dir
#
# options : same in blastn
#
###########################################################
"""

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def checkSignValidation(list4) :
	db_dir = ""
	query_dir = ""
	db_ok = False
	query_ok = False

	for idx in [0, 2] :
		if list4[idx] == "-db" :
			db_dir = list4[idx+1]
			db_ok = True
		elif list4[idx] == "-query" :
			query_dir = list4[idx+1]
			query_ok = True
	
	if not (db_ok and query_ok) :
		print "missing required options!"
		printUSAGE()
		exit()

	return (db_dir, query_dir)

# main

if len(sys.argv) < 3 :
	printUSAGE()
	exit()

fmt = '0'
options = sys.argv[1:-4]
_dir = checkSignValidation(sys.argv[-4:])

idx = 0
while idx < len(options) :
	if (options[idx] == '-outfmt') :
		fmt = options[idx+1]
		break

queries = glob.glob(makeDirForm(_dir[1]) + "*")

for query in queries :
	os.system("blastn -db " + makeDirForm(_dir[0]) + getFileName(query) + " -query " + query + " -out " + getFileName(query) + ".m" + fmt + " " + " ".join(options))
