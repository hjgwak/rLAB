import sys

table = open(sys.argv[1], 'r')

first = True
for line in table.readlines() :
	line = line.rstrip('\r\n').replace('\t', ',')
	if first :
		print "cluster," + line
	else :
		print line
	first = False

table.close()
