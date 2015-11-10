import sys, os

__author__ = "hjgwak"
__version__ = "1.0,1"

def printUSAGE() :
	print """
###########################################################
# python split_parsed_sam.py [options] [parseed sam file]
# options :
#     -Sa	:	Do sort after split (for each result files)
#     -Sb	:	Do sort before split (for original sam file)
#     -Q	: 	Quiet, Do not print anything in stderr
# output : Directory named sam file name, reference_name.parse
###########################################################
"""

def getFileName(path) :
	return path.split('/')[-1].split('.')[0]

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit()

if len(sys.argv) < 2 :
	printUSAGE()
	exit()

quiet = False
if '-Q' in sys.argv :
	quiet = True

parse = ""
temp = False
if '-Sb' in sys.argv :
	os.system("sort " + sys.argv[-1] + " -k 3 -o temp.out")
	temp = True
	parse = open("temp.out", 'r')
else :
	parse = open(sys.argv[-1], 'r')

dir_name = getFileName(sys.argv[-1]) + '/'
os.mkdir(dir_name)

reference = ""
out_f = ""
first = True
for line in parse.readlines() :
	line = line.rstrip('\r\n')
	ref = line.split('\t')[2]
	if ref != reference :
		if not first :
			out_f.close()
			if '-Sa' in sys.argv :
				if not quiet :
					print >> sys.stderr, "sorting " + ref
				os.system("sort " + dir_name + reference + ".parse -k 4n -o " + dir_name + reference + ".sort")
		if not quiet :
			print >> sys.stderr, "split " + ref + " from file"
		out_f = open(dir_name + ref + ".parse", 'w')
		first = False
		reference = ref
	out_f.write(line + "\n")

out_f.close()
if '-Sa' in sys.argv :
	if not quiet :
		print >> sys.stderr, "sorting " + reference
	os.system("sort " + dir_name + reference + ".parse -k 4n -o " + dir_name + reference + ".sort")

parse.close()
if temp :
	os.system("rm temp.out")
