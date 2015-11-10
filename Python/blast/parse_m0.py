import sys

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def parseStrand(strand) :
	if strand == "Plus" :
		return '+'
	else :
		return '-'

# main

if len(sys.argv) != 2:
	print "python parse_m0.py blast_output.m0"
	exit()

_file = open(sys.argv[1], 'r')

query = ""
db = ""
identity = ""
length = ""
cover = ""

for line in _file.readlines() :
	line = line.rstrip('\r\n')
	if line.startswith("Query=") :
		query = line.split(' ')[1]
	elif line.startswith(">") :
		db = line.split(' ')[1]
	elif line.startswith(" Identities") :
		identity = line.split(' ')[4][1:-2]
		cover = line.split(' ')[3].split('/')[1]
	elif line.startswith("Length=") :
		length = line.split('=')[1]
	elif line.startswith(" Strand") :
		strand_info = line.split('=')[1].split('/')
		strand = (parseStrand(strand_info[0]), parseStrand(strand_info[1]))
		print query + "\t" + db + "\t" + length + "\t" + cover + "\t" + identity + "\t" + strand[0] + "\t" + strand[1]

_file.close()
