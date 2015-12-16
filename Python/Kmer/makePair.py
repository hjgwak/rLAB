import sys

def printUSAGE() :
	print """
###########################################################
# python makePair.py [options] [hl file] [fna file]
# options :
#     -ml	int	:	minimum length of fragment, Default length of primer
#     -Ml	int	:	maximum length of fragment, Default length of whole seq
#     -o	str	:	output path, Default stdout
#     -all		:	if set this report all fragment,
#         			default remain longest sequence
###########################################################
"""

def readFasta(fasta_n) :
	fasta_f = open(fasta_n, 'r')
	line = fasta_f.readline()
	if line[0] != '>' :
		print sys.stderr, "Not fasta format!"
		exit(-1)
	name = line.rstrip('\r\n')[1:]
	seq = ""
	for line in fasta_f.readlines() :
		line = line.rstrip('\r\n')
		if line[0] == '>' :
			print sys.stderr, "Multi fasta format! (Please input single fasta)"
			exit(-1)
		else :
			seq += line
	fasta_f.close()
	return (name, seq)

def readHL(hl_n) :
	hl_f = open(hl_n, 'r')
	res = {}
	for line in hl_f.readlines() :
		line = line.rstrip('\r\n')
		if line[0] == '#' :
			continue
		else :
			split = line.split(' ')
			res[split[0]] = split[1:]
	hl_f.close()
	return res

def makePosList(dic) :
	keys = dic.keys()
	pos_list = []
	for key in keys :
		pos_list += dic[key]
	pos_list.sort()
	return pos_list

def rmSub(frags) :
	res = []
	for frag1 in frags :
		remove = False
		for frag2 in frags :
			if frag1 == frag2 :
				continue
			elif frag1 in frag2 :
				remove = True
				break
		if not remove :
			res.append(frag1)
	return res

# main

print >> sys.stderr, "Start makePair.py"
if len(sys.argv) < 3 :
	printUSAGE()
	exit(-1)

print >> sys.stderr, "Parse options!"
ml = 0
Ml = 0
report_all = False
if '-ml' in sys.argv :
	ml = int(sys.argv[sys.argv.index('-ml') + 1])
if '-Ml' in sys.argv :
	Ml = int(sys.argv[sys.argv.index('-Ml') + 1])
if '-o' in sys.argv :
	sys.stdout = open(sys.argv[sys.argv.index('-o') + 1], 'w')
if '-all' in sys.argv :
	report_all = True

(name, seq) = readFasta(sys.argv[-1])
print >> sys.stderr, "Read Fasta!"
if Ml == 0 :
	Ml = len(seq)
primers = readHL(sys.argv[-2])
print >> sys.stderr, "Read HL!"
k = len(primers.keys()[0])
if ml < k :
	ml = k

print >> sys.stderr, "ml : " + str(ml) + "\tMl : " + str(Ml)

pos_list = makePosList(primers)

fragments = []
for pos1 in pos_list :
	pos1 = int(pos1)
	for pos2 in pos_list :
		pos2 = int(pos2)
		dist = pos2 - pos1
		if dist < ml - k :
			continue
		elif dist > Ml - k :
			break

		fragments.append(seq[pos1 - 1: pos2 + k - 1])

if not report_all :
	fragments = rmSub(fragments)

cnt = 0
for fragment in fragments :
	cnt += 1
	print '>' + str(cnt)
	print fragment

if '-o' in sys.argv :
	sys.stdout.close()

print >> sys.stderr, "Done!"
