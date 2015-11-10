import sys

if len(sys.argv) != 2 :
	print "\nInput format : python seedPostProcessing.py <seed file>\n"
	exit(0)

seed_file = open(sys.argv[1], "r")

seed = seed_file.readline()
while seed :
	split = seed.split('\t')
	print "d\t" + str(int(split[0])+1) + "\t" + str(int(split[1])+1) + "\t" + split[2]
	seed = seed_file.readline()
