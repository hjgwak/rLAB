###########################################################################
# python emboss_parse_dir.py file_format file_directory
# output : file_name.parse
###########################################################################

import sys, os, glob

__author__ = "hjgwak"
__version__ = "1.0.1"

def printUSAGE() :
	print """
###########################################################################
# python emboss_parse_dir.py file_format file_directory
# output : file_name.parse
###########################################################################
"""

def makeDirFormat(string) :
	if (string[-1] != '/') :
		string += '/'
	return string

def getFileName(path) :
	return path.split('/')[-1]

# main

if len(sys.argv) != 3 or sys.argv[-1] == '-h' :
	printUSAGE()
	exit(0)

_files = glob.glob(makeDirFormat(sys.argv[2]) + "*." + sys.argv[1])

for _file in _files :
	os.system("python ~/Python/emboss/emboss_parse.py " + _file + " > " + getFileName(_file) + ".parse")
