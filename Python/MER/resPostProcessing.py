import sys

if len(sys.argv) != 4 :
	print "\nInput format : python resPostProcessing.py -cut # <res file>\n"

cut = int(sys.argv[2])
res_file = open(sys.argv[3], "r")

line = res_file.readline()
while line :
	component = line.split("\t")
	if int(component[3] >= cut) and int(component[4]) >= cut :
		print line[:-1]
	line = res_file.readline()
