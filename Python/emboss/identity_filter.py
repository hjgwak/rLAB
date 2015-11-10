###########################################################
# python identity_filter.py [emboss output.sim] [threshold]
###########################################################

import sys

def printUSAGE() :
	print """
###########################################################
# python identity_filter.py [emboss output.sim] [threshold]
###########################################################
"""

# main

if len(sys.argv) != 3 :
	printUSAGE()
	exit()

_file = open(sys.argv[1], 'r')
threshold = float(sys.argv[2])

for line in _file.readlines() :
	line = line.rstrip('\r\n')
	identity = float(line.split('\t')[2])
	if identity >= threshold :
		print line

_file.close()
