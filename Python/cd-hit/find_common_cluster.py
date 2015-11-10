import sys

def makeClstrList(clstr_f) :
	res_clstr = {}
	item_clstr = []
	name = ""
	for line in clstr_f.readlines() :
		line = line.rstrip('\r\n')
		if line[0] == '>' :
			if name != "" and item_clstr != [] :
				res_clstr[name] = item_clstr
			name = line
			item_clstr = []
		else :
			item_clstr.append(line)
	if item_clstr != [] :
		res_clstr[name] = item_clstr
	
	return res_clstr

def findCommonClstr(clstr1, clstr2) :
	flag = True
	res = {}

	for key1 in clstr1 :
		for key2 in clstr2 :
			flag = True
			for item in clstr1[key1] :
				flag = flag and (item in clstr2[key2])
			if flag :
				res[(key1, key2)] = clstr1[key1]

	return res

# main

if sys.argv[1] == '-h' or len(sys.argv) != 3 :
	print "python find_common_cluster.py [cd-hit clstr 1] [cd-hit clstr 2]"
	exit()

clstr1_f = open(sys.argv[1], 'r')
clstr2_f = open(sys.argv[2], 'r')

clstr1 = makeClstrList(clstr1_f)
clstr2 = makeClstrList(clstr2_f)

clstr1_f.close()
clstr2_f.close()

common_clstr = findCommonClstr(clstr1, clstr2)

for key in common_clstr :
	print ">" + key[0] + ", " + key[1]
	for item in common_clstr[key] :
		print item
