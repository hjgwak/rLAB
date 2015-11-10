import sys

if len(sys.argv) != 2 :
	print "python countElements.py [intersectBed result]"
	exit(0)

_file = open(sys.argv[1], "r")

prev = ""
cur = ""
cnt = 0
line = _file.readline()
while line :
	split = line.split('\t')
	cur = (split[0], split[3], split[4])
	if cur != prev :
		cnt += 1
	prev = cur
	line = _file.readline()
_file.close()
print cnt
