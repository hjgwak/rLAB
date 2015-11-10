import sys

__author__ = "hjgwak"
__version__ = "1.0.1"

def printUSAGE() :
	print """
###########################################################
# python make_table.py [-csv] [score option] [output list]
#      -csv 	:	print output csv format
# score option :
#      -cover1	:	use (n-1)-coverage for score
#      -cover2 	:	use n-coverage for score
#      -cover3	:	use (n+1)-coverage for score
#      -avg_depth	:	use avg_depth for score
#      -med_depth	:	use median_depth for score
#      -rpkm	:	use rpkm for score
# notice : select only one socore option!
###########################################################
"""

def makeScoreHash(path) :
	_file = open(path, 'r')

	res = {}
	for line in _file.readlines() :
		line = line.rstrip('\r\n')
		split = line.split('\t')
		res[split[0]] = split[1:]
	_file.close()

	return res

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit()

if len(sys.argv) < 3 :
	printUSAGE()
	exit()

pos_dic = {
	"-cover1" : 0,
	"-cover2" : 1,
	"-cover3" : 2,
	"-avg_depth" : 3,
	"-mid_depth" : 4,
	"-rpkm" : 5
}

csv = False

if "-csv" in sys.argv :
	csv = True
	sys.argv.remove("-csv")

score_opt = sys.argv[1]
outputs = sys.argv[2:]
score_pos = pos_dic[score_opt]

if csv :
	print ",".join(["elem"] + outputs)
else :
	print "\t".join(outputs)

hash_table = {}
for output in outputs :
	hash_table[output] = makeScoreHash(output)

elems = set([])
for output in outputs :
	elems = elems.union(set(hash_table[output].keys()))
elems = list(elems)

for elem in elems :
	for_print = [elem]
	for output in outputs :
		if elem in hash_table[output] :
			for_print.append(hash_table[output][elem][score_pos])
		else :
			for_print.append('0')

	if csv :
		print ",".join(for_print)
	else :
		print "\t".join(for_print)
