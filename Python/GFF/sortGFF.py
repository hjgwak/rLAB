import sys

def comp(a, b) :
	first = a.split('\t')[0]
	second = b.split('\t')[0]

	if first < second :
		return -1
	elif first > second :
		return 1
	else :
		return 0

if len(sys.argv) != 3 :
	print "python sortGFF.py [number of ignore line] [gff file]"
	exit(0)

gff = open(sys.argv[2], "r")
lines = gff.readlines()
gff.close()

gff = open(sys.argv[2], "w")

for i in range(int(sys.argv[1])) :
	print >>gff, lines[0][:-1]
	del lines[0]

lines.sort(comp)

for line in lines :
	print >>gff, line[:-1]

gff.close()
