import sys

if len(sys.argv) != 2 :
	print "python count_cluster.py [cdhit clstr]"
	exit()

clstr = open(sys.argv[1], 'r')

cnt = 0
for line in clstr.readlines() :
	if line[0] == '>' :
		cnt += 1

clstr.close()
print cnt
