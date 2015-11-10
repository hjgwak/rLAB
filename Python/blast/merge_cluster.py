import sys, glob

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def fileFunc(a, b) :
	a = getFileName(a)
	b = getFileName(b)
	if a[:5] == 'whole' :
		return 1
	elif b[:5] == 'whole' :
		return -1
	aint = int(a.split('.')[0][7:])
	bint = int(b.split('.')[0][7:])
	if aint > bint :
		return 1
	else :
		return -1

# main

if len(sys.argv) != 2 :
	print "python merge_cluster.py [m0.parse directory]"
	exit()

_files = glob.glob(makeDirForm(sys.argv[1]) + "*.parse")
_files.sort(fileFunc)

cnt = 0

for _file in _files :
	print ">Cluster " + str(cnt)
	clstr = open(_file, 'r')
	for line in clstr.readlines() :
		line = line.rstrip('\r\n')
		print line
	clstr.close()
	cnt += 1
