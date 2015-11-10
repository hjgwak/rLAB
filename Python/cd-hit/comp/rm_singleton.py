import sys

def printClstr(clstr) :
	for item in clstr :
		print item

# main

if len(sys.argv) != 2 or sys.argv[1] == '-h' :
	print "python rm_singleton.py [cd-hit output]"
	exit()

cdhit = open(sys.argv[1], 'r')

num = 0
flag = False
clstr = []

for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == '>' :
		if flag :
			if len(clstr) == 1 and clstr[0].split(' ')[1][:-3][-1] == 'S' :
				clstr = []	
				continue
			print ">Cluster " + str(num)
			num += 1
			printClstr(clstr)
		flag = True
		clstr = []
	else :
		clstr.append(line)
if len(clstr) != 1 or clstr[0].split(' ')[1][:-3][-1] != 'S' :
	print ">Cluster " + str(num)
	printClstr(clstr)

cdhit.close()
