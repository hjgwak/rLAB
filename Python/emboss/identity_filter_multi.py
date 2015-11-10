import sys, os, glob

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

# main

if len(sys.argv) != 3 :
	print "python identity_filter_multi.py [emboss output.sim dir] [threshold]"
	exit()

_files = glob.glob(makeDirForm(sys.argv[1]) + "*.sim")

for _file in _files :
	os.system("python ~/Python/emboss/identity_filter.py " + _file + " " + sys.argv[2] + " > " + getFileName(_file))
