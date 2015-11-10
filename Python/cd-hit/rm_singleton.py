import sys

def writeCluster(clstr, name) :
	print name
	for item in clstr :
		print item

# main

if len(sys.argv) != 2 or sys.argv[1] == '-h' :
	print "python rm_singleton.py [cdhit_clstr file]"
	exit()

cdhit = open(sys.argv[1], 'r')

clstr = []
name = ""
for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == '>' :
		if len(clstr) > 1 :
			writeCluster(clstr, name)
		name = line
		clstr = []
	else :
		clstr.append(line)
if len(clstr) > 1 :
	writeCluster(clstr, name)

cdhit.close()
