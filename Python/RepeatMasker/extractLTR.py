import sys

def parseComponent(comp) :
	i = 0
	while i < len(comp) :
		if comp[i] == '' :
			del comp[i]
		else :
			i += 1
	return comp

if len(sys.argv) != 2 :
	print "python extractLTR.py [RepeatMasker out]"
	exit(0)

_file = open(sys.argv[1], "r")
for i in range(3) :
	_file.readline()

line = _file.readline()
while line :
	comp = line.split(' ')
	comp = parseComponent(comp)
	if comp[10].split('/')[0] == "LTR" :
		out = comp[4] + "\tRepeatMasker\tLTR\t" + comp[5] + "\t" + comp[6] + "\t" + comp[1]
		if comp[8] == "+" :
			out += "\t+\t.\t"
		else :
			out += "\t-\t.\t"
		out += "Class=" + comp[10]
		print out
	line = _file.readline()
_file.close()
