import sys, os, glob

__author__ = "hjgwak"
__version__ = "1.0,1"

def printUSAGE() :
	print """
###########################################################
# python calc_coverage_depth.py [options] [MGEScan output] [splited dir]
# options :
#     -out	str	:	print output in file named given option (default stdout)
#     -ncover	#	:	set True when list element over n for coverage (default 1)
#     -coverage	#	:	setting a threshold for coverage [0.0 ~ 1.0] (default 0.0)
#     -depth	#	:	setting a threshold for depth [0 ~ ] (default 0)
#     -split		:	Preprocess split sam file (User have to input sam file instead of dir)
#     -rpkm	read_fastq	:	Normalize depth score
# output fmt :
#     element_name (n-1)-coverage  n-coverage (n+1)-coverage  avg_depth  median_depth (RPKM score)
###########################################################
"""

def rm_fmt(name) :
	return name.split('.')[0]

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def makeLengthDB(mge) :
	res = {}
	mge_f = open(mge, 'r')
	for line in mge_f.readlines() :
		line = line.rstrip('\r\n')
		if line[-10:] == '----------' :
			continue
		split = line.split('\t')
		res[split[0]] = int(split[8])
	mge_f.close()

	return res

def makeFlagList(length) :
	res = []
	for i in range(length) :
		res.append(0)

	return res

def calcCoverage(flag_list, ncover) :
	whole_len = len(flag_list)
	exist = [0, 0, 0]
	for item in flag_list :
		if item >= ncover-1 :
			exist[0] += 1
		if item >= ncover :
			exist[1] += 1
		if item >= ncover+1 :
			exist[2] += 1
	minuscover = float(exist[0]) / whole_len
	n_cover = float(exist[1]) / whole_len
	pluscover = float(exist[2]) / whole_len
	return (minuscover, n_cover, pluscover)

def calcDepth(flag_list) :
	tmp = flag_list
	avg = float(sum(flag_list)) / len(flag_list)
	tmp.sort()
	tmp = tmp[tmp.count(0):]
	median = tmp[len(tmp)/2]

	return (avg, median)

def getTotalReads(fastq) :
	fq = open(fastq, 'r')
	
	cnt = 0
	line = fq.readline()
	while line :
		cnt += 1
		line = fq.readline()
		
	fq.close()

	return cnt / 4

def calcRPKM(mapped_reads, total_reads, seq_length) :
	mega_read = total_reads / 1.0E6
	kilo_len = seq_length / 1.0E3
	return mapped_reads / (mega_read * kilo_len)

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit()

if len(sys.argv) < 3 :
	printUSAGE()
	exit()

# setting options

ncover = 1
coverage_th = 0.0
depth_th = 0
total_reads = 0

if '-out' in sys.argv :
	sys.stdout = open(sys.argv[sys.argv.index('-out') + 1], 'w')

if '-ncover' in sys.argv :
	ncover = int(sys.argv[sys.argv.index('-ncover') + 1])

if '-coverage' in sys.argv :
	coverage_th = float(sys.argv[sys.argv.index('-coverage') + 1])

if '-depth' in sys.argv :
	depth_th = int(sys.argv[sys.argv.index('-depth') + 1])

if '-rpkm' in sys.argv :
	total_reads = getTotalReads(sys.argv[sys.argv.index('-rpkm') + 1])

# preprocess

data_dir = makeDirForm(sys.argv[-1])
if '-split' in sys.argv :
	os.system("python /home/hjgwak/Python/bowtie/split_parsed_sam.py -Sa -Sb -Q " + sys.argv[-1])
	data_dir = makeDirForm(rm_fmt(getFileName(sys.argv[-1])))

length_db = makeLengthDB(sys.argv[-2])

# body

sorted_list = glob.glob(data_dir + "*.sort")

for element in sorted_list :
	elem = open(element, 'r')
	flag_list = []
	ref_name = ""
	first = True
	mapped_reads = 0
	seq_length = 0

	for line in elem.readlines() :
		line = line.rstrip('\r\n')
		if first :
			ref_name = line.split('\t')[2]
			seq_length = length_db[ref_name]
			flag_list = makeFlagList(seq_length)
		
		start_pos = int(line.split('\t')[3])
		for i in range(100) :
			if start_pos + i >= length_db[ref_name] :
				break
			flag_list[start_pos + i] += 1
		first = False
		mapped_reads += 1

	coverage = calcCoverage(flag_list, ncover)
	depth = calcDepth(flag_list)

	if coverage[1] >= coverage_th and depth[0] >= depth_th :
		for_print = [ref_name, str(coverage[0]), str(coverage[1]), str(coverage[2]), str(depth[0]), str(depth[1])]
		if '-rpkm' in sys.argv :
			for_print.append(str(calcRPKM(mapped_reads, total_reads, seq_length)))
		print "\t".join(for_print)
	elem.close()

if '-out' in sys.argv :
	sys.stdout.close()
