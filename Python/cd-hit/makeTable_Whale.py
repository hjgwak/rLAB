import sys

__author__ = "hjgwak"
__version__ = "1.0.2"

def printUSAGE() :
	print """
###########################################################
# python makeTable_whale.py [options] [cd-hit output]
# options :
# 	-S	[float]	:	Score of Singleton (default 1.0)
#	-M	[float]	:	Score of Multiple (default 2.0)
#	-sum[0, 1]	:	Set 0, It works like PF 'S or M' (default 1)
###########################################################
"""

def parseOptions(opts) :
	res = {'S' : 1.0, 'M' : 2.0, 'sum' : True}
	idx = 0
	while idx < len(opts) :
		if opts[idx] == '-S' :
			res['S'] = float(opts[idx + 1])
		elif opts[idx] == '-M' :
			res['M'] = float(opts[idx + 1])
		elif opts[idx] == '-sum' :
			if opts[idx + 1] == '0' :
				res['sum'] = False
			else :
				res['sum'] = True
		else :
			print "Wrong option!"
			exit()
		idx += 2

	return res

def whalesInit() :
	whales = {}
	whales["Lipotes_vexillifer"] = 0 
	whales["Physeter_macrocephalus"] = 0
	whales["oor_Oorc"] = 0
	whales["BalAcu"] = 0
	whales["ttn_Ttru"] = 0

	return whales

def calcScore(ch, opt) :
	score = 0.0
	if ch == 'S' :
		score = opt['S']
	elif ch == 'M' :
		score = opt['M']

	return score

# main

if '-h' in sys.argv or '-help' in sys.argv :
	printUSAGE()
	exit()

if len(sys.argv) < 2 or len(sys.argv) > 8 or len(sys.argv) % 2 == 1 :
	printUSAGE()
	exit()

whales = whalesInit()
options = parseOptions(sys.argv[1:-1])

names = whales.keys()

print '\t'.join(names)

cdhit = open(sys.argv[-1], 'r')

flag = False
prev = ""

for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == ">" :
		if flag :
			print prev + "\t" + str(whales[names[0]]) + "\t" + str(whales[names[1]]) + "\t" + str(whales[names[2]]) + "\t" + str(whales[names[3]]) + "\t" + str(whales[names[4]])
		flag = True
		whales = whalesInit()
		prev = '_'.join(line[1:].split(' '))
	else :
		kind = line.split(' ')[1]
		score = calcScore(kind[-4], options)
		if options['sum'] :
			if kind.startswith(">118797") :
				whales["Lipotes_vexillifer"] += score
			elif kind.startswith(">9755") :
				whales["Physeter_macrocephalus"] += score
			elif kind.startswith(">oor") :
				whales["oor_Oorc"] += score
			elif kind.startswith(">310752") :
				whales["BalAcu"] += score
			elif kind.startswith(">ttn") :
				whales["ttn_Ttru"] += score
			else :
				print "strange input!"
				exit()
		else :
			if kind.startswith(">118797") :
				whales["Lipotes_vexillifer"] = max(whales["Lipotes_vexillifer"], score)
			elif kind.startswith(">9755") :
				whales["Physeter_macrocephalus"] = max(whales["Physeter_macrocephalus"], score)
			elif kind.startswith(">oor") :
				whales["oor_Oorc"] = max(whales["oor_Oorc"], score)
			elif kind.startswith(">310752") :
				whales["BalAcu"] = max(whales["BalAcu"], score)
			elif kind.startswith(">ttn") :
				whales["ttn_Ttru"] = max(whales["ttn_Ttru"], score)
			else :
				print "strange input!"
				exit()
print prev + "\t" + str(whales[names[0]]) + "\t" + str(whales[names[1]]) + "\t" + str(whales[names[2]]) + "\t" + str(whales[names[3]]) + "\t" + str(whales[names[4]])

cdhit.close()
