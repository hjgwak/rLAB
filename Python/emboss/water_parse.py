import sys, glob, os, re

#water_file = sys.argv[1]
#open_water_file = open(water_file, 'r')

def init(text):
	return int(text) if text.isdigit() else text

def natural_keys(text):
	return [ init(c) for c in re.split('(\d+)', text) ]

ListOfWater = []
for file_name in glob.iglob('*.water'):
	file_name = file_name.rstrip('\n')
	ListOfWater.append(file_name)

ListOfWater.sort(key=natural_keys)
#for line in ListOfWater:
#	print line


print 'asequence\tbsequence\talign_length\tidentity\tsimilarity'

seq1 = ''
seq2 = ''
align_length = ''
identity = ''
similarity = ''

k = 0
while 1:
	inopen = open(ListOfWater[k], 'r')
	
	for line in inopen:
		line = line.rstrip('\n')
		if line.startswith('# 1:'):
			seq1 = line.split(': ')[1]
			#print seq1

		elif line.startswith('# 2:'):
			seq2 = line.split(': ')[1]
			#print seq2
	
		elif line.startswith('# Length:'):
			align_length = line.split(': ')[1]
			#print align_length
	
		elif line.startswith('# Identity:'):
			temp_split = line.split(' ')
			for i in range(0, len(temp_split)):
				if temp_split[i].startswith('('):
					identity = temp_split[i][1:-1]
#					break
		
			#print identity
	
		elif line.startswith('# Similarity:'):
			temp_split = line.split(' ')
			for i in range(0, len(temp_split)):
				if temp_split[i].startswith('('):
					similarity = temp_split[i][1:-1]
			#print similarity
	
		raw = [seq1, seq2, align_length, identity, similarity]
	
	print raw[0] + '\t' + raw[1] + '\t' + raw[2] + '\t' + raw[3] + '\t' + raw[4]

	k += 1

	if k == len(ListOfWater):
		break
