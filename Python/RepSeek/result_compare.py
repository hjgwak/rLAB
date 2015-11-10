############################################################################
# Input command : python result_compare.py <reference file> <result file>  #
# Ouput : hit ratio, miss ratio, ratio of each hit case                    #
############################################################################

__author__ = 'hjgwak'
__version__ = '1.0.2'

import sys

def printUSAGE() :
	print """
#####################################################################################
# Input command : python result_compare.py <reference file> <result file> [option]  #
# Options :                                                                         #
#      -buf=<bp>          : set up buffer bp to recognize hit                       #
# Ouput : hit ratio, miss ratio, ratio of each hit case                             #
#####################################################################################
"""

def findStr(_str, _file) :
	res = 0
	line = _file.readline()
	while line :
		if line.find(_str) != -1 :
			res = int(line.split(' : ')[1][:-1])
			break
		line = _file.readline()
	return res

def findEOF(_file) :
	_file.seek(0,2)
	eof = _file.tell()
	_file.seek(0,0)
	return eof

def nextRef(ref_file) :
	length = findStr('len(LTR) :', ref_file)
	ltr = findStr('LTR start :', ref_file)
	mltr = findStr('mutated LTR start :', ref_file)
	return (ltr, mltr, length, length)

def nextRes(res_file) :
	res = []
	line = res_file.readline()
	while line and line[:5] != '-----' :
		data = line.split('\t')
		res.append((int(data[1]), int(data[2]), int(data[3]), int(data[4])))
		line = res_file.readline()
	return res

def deter3(ref, res, buf) :
	diff = ref - res
	det = -1
	if res < ref :
		det = 0
	elif res > ref :
		det = 1
	elif res == ref :
		det = 2
		hit = True
	return (det, diff)

def determineCaseHit(ref, resi, buf) :
	left = deter3(ref[0], res[0], buf)
	right = deter3(ref[0] + ref[2], res[0] + res[2], buf)
	case = 3 * left[0] + right[0]
	hit = True
	if -left[1] > buf or right[1] > buf :
		hit = False
# miss finder
	if res[0] + res[2] < ref[0] or res[0] > ref[0] + ref[2] :
		case = 9
		hit = False
	return ('case' + str(case), hit)

def printResult(stats, hit) :
	keys = stats.keys()
	keys.sort()
	for key in keys :
		print key + "\t",
	print
	for key in keys :
	 	print str(stats[key]) + "\t\t",
	print "\n"

	total = 0
	for item in stats :
		total += stats[item]
	miss = total - hit
	print "Total :\t" + str(total)
	print "Hit :\t" + str(hit)
	print "Miss :\t" + str(miss)
	print "Out :\t" + str(stats['case9'])
	print "\nHit ratio : %0.3f" % (float(hit) / float(total))
	print "Miss ratio : %0.3f" % (float(miss) / float(total))
	

if __name__ == '__main__' :
	if sys.argv[1].lower() == '-h' :
		printUSAGE()
		exit(0)

	if len(sys.argv) < 3 :
		print "\nToo short arguments, check your command\n"
		exit(1)
	elif len(sys.argv) > 4 :
		print "\nToo long arguments, check your command\n"
		exit(1)

# read options
	buf = 0
	if len(sys.argv) == 4 :
		idx = sys.argv[3].find('-buf=')
		if idx != -1 :
			buf = int(sys.argv[3][5:])
		else :
			print "Wrong option!"

# file open and find EOF
	ref_file = open(sys.argv[1], 'r')
	res_file = open(sys.argv[2], 'r')

	ref_end = findEOF(ref_file)
	res_end = findEOF(res_file)
# construct result dictionary that initialized 0
	stats = { }
	for i in range(10) :
		stats['case' + str(i)] = 0

	tmp = res_file.readline()
	hit = 0
	while res_file.tell() != res_end :
		ref = nextRef(ref_file)
		resv = nextRes(res_file)
		for res in resv :
#			print "ref :", ref
#			print "res :", res
			det = determineCaseHit(ref, res, buf)
			stats[det[0]] += 1
			if det[1] :
				hit += 1
	printResult(stats, hit)

	ref_file.close()
	res_file.close()
