import sys

if len(sys.argv) != 2 :
	print "wrong arguments!"
	exit(0)

_file = open(sys.argv[1], "r")

line = _file.readline()

total = 0
match = 0
miss = 0

while line :
	line = line[:-1]
	for char in line :
		if char == "|" :
			total += 1
			match += 1
		elif char == "." :
			total += 1
			miss += 1
	line = _file.readline()

print "total : " + str(total)
print "match : " + str(match)
print "miss : " + str(miss)
print
print "sim : " + str((float(match)/float(total))*100) + "%"
