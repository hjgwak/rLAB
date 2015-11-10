import sys

if len(sys.argv) != 2 :
	print "Please give only one emboss output file"
	exit(0)

_file = open(sys.argv[1], "r")
debug = True

# Skip header of file
line = _file.readline()
while line != "\n" :
	line = _file.readline()

prev = line
line = _file.readline()
while line :
	file_a = ""
	file_b = ""
	seqlen = 0
	identity = 0.0
	coverage = 0.0
	gap = 0
	lendgap = 0
	rendgap = 0
	match = 0
	mismatch = 0

	# Get information of alignment
	for i in range(17) :
		if line == '' :
			exit()

		if line.startswith("# 1: ")	:
			file_a = line[5:-1]
		elif line.startswith("# 2: ") :
			file_b = line[5:-1]
		elif line.startswith("# Length: ") :
			seqlen = int(line[10:-1])
		prev = line
		line = _file.readline()
	
	# Parse alignment
	start = True	
	while prev != line :
		if line.startswith("          ") :
			line = line[21:-1]
			for cell in line :
				if cell == ' ' and start :
					lendgap += 1
				elif cell == ' ' :
					rendgap += 1
				elif cell == '|' or cell == '.' :
					start = False
					gap += rendgap
					rendgap = 0
					if cell == '|' :
						match += 1
					else :
						mismatch += 1
		prev = line
		line = _file.readline()

	# Calc identity and coverage
	identity = (float(match) / float(match + mismatch + gap)) * 100
	coverage = (float(seqlen - lendgap - rendgap - gap) / float(seqlen - lendgap - rendgap)) * 100

#output = file_a + "\t" + file_b + "\t" + str(identity) + "%\t" + str(coverage) + "%"
	output = file_a + "\t" + file_b + "\t%.2f\t%.2f"
	if debug :
		output += "\t" + str(match) + "\t" + str(mismatch) + "\t" + str(gap) + "\t" + str(lendgap) + "\t" + str(rendgap)
	print output % (identity, coverage)

	prev = line
	line = _file.readline()
