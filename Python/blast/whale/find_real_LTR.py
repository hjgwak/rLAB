import sys

__author__ = "hjgwak"
__version__ = "1.0.1"


# main

if len(sys.argv) != 4 :
	print "python find_real_LTR.py [length perc] [identity] [m0.parse file]"
	exit()

if float(sys.argv[1]) > 1.0 or float(sys.argv[2]) > 1.0 :
	print "threshold range error [0.0 to 1.0]"
	exit()

m0 = open(sys.argv[-1], 'r')

cover_th = float(sys.argv[1])
iden_th = float(sys.argv[2])

for line in m0.readlines() :
	line = line.rstrip("\r\n")
	split = line.split("\t")

	length = float(split[2])
	cover = float(split[3])
	identity = float(split[4][:-1])/100

	if cover / length >= cover_th and identity >= iden_th :
		print line

m0.close()
