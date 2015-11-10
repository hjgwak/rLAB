import sys, os, glob

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

if len(sys.argv) != 2 :
	print "python parse_m0_multi.py m0_dir"
	exit()

_files = glob.glob(makeDirForm(sys.argv[1]) + "*.m0")

for _file in _files :
	os.system("python ~/Python/blast/parse_m0.py " + _file + " > " + getFileName(_file) + ".parse")
