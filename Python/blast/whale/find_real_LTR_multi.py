import os, sys, glob

__author__ = "hjgwak"
__version__ = "1.0.1"

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

# main

if len(sys.argv) != 4 :
	print "python find_real_LTR_multi.py [length perc] [identity] [m0.parse dir]"
	exit()

if float(sys.argv[1]) > 1.0 or float(sys.argv[2]) > 1.0 :
	print "threshold range error [0.0 to 1.0]"
	exit()

files = glob.glob(makeDirForm(sys.argv[-1]) + "*.parse")

for parse in files :
	os.system("python ~/Python/blast/whale/find_real_LTR.py " + sys.argv[1] + " " + sys.argv[2] + " " + parse + " > " + getFileName(parse) + ".ltr")

os.system("find ./*.ltr -empty -type f -delete")
