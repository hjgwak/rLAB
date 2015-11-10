import sys

__author__ = "hjgwak"
__version__ = "1.0,2"

def printClstr(clstr) :
	for item in clstr :
		print item

# main

if len(sys.argv) != 2 :
	print "python rm_single_set.py [cd-hit output]"
	exit()

cdhit = open(sys.argv[1], 'r')

flag = False
single_set = True
clstr = []
cnt = 0

for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == '>' :
		if flag :
			if single_set == False :
				print ">Cluster " + str(cnt)
				printClstr(clstr)
				cnt += 1
		flag = True
		single_set = True
		clstr = []
	else :
		comp = line.split(' ')[1][-4]
		clstr.append(line)
		single_set = single_set and (comp == 'S')

if single_set == False :
	print ">Cluster " + str(cnt)
	printClstr(clstr)

cdhit.close()
