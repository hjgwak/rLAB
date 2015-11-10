import sys

__author__ = "hjgwak"
__version__ = "1.0.1"

def printUSAGE() :
	print """
###########################################################
# python mapping_list.py [-window #] [MGEScan output] [.sort file]
#     Default of window is 1
###########################################################
"""

def rm_fmt(name) :
	return name[:name.rfind('.')]

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def getLength(mge, name) :
	res = 0
	mge_f = open(mge, 'r')
	for line in mge_f.readlines() :
		line = line.rstrip('\r\n')
		if "----------" in line :
			continue
		if line.split('\t')[0] == name :
			res = int(line.split('\t')[8])
			break
	mge_f.close()
	return res

def printMappingList(mapping_list, window) :
	cnt = 0
	tmp_list = []
	for item in mapping_list :
		cnt += 1
		tmp_list.append(item)
		if cnt >= window :
			print float(sum(tmp_list)) / len(tmp_list)
			cnt = 0
			tmp_list = []
	if tmp_list != [] :
		print float(sum(tmp_list)) / len(tmp_list)

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit(0)

window = 1
if "-window" in sys.argv :
	window = int(sys.argv[sys.argv.index('-window') + 1])

sort_f = open(sys.argv[-1], 'r')
len_elem = getLength(sys.argv[-2], rm_fmt(getFileName(sys.argv[-1])))

mapping_list = []
for i in range(len_elem) :
	mapping_list.append(0)

for line in sort_f.readlines() :
	line = line.rstrip('\r\n')
	start_pos = int(line.split('\t')[3])
	for i in range(100) :
		if start_pos + i >= len_elem :
			break
		mapping_list[start_pos + i] += 1
sort_f.close()

printMappingList(mapping_list, window)
