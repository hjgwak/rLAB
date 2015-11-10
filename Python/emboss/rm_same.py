import sys

if len(sys.argv) != 2 :
	print "python rm_same.py [sim file]"
	exit()

_file = open(sys.argv[1], 'r')

for line in _file.readlines() :
	line = line.rstrip('\r\n')
	comp = line.split('\t')
	if comp[2] == "100.00" :
		continue
	print line
