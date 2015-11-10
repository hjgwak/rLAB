##################################################################################
# Input : MULTIFASTA file                                                        #
# Input command : python splitOver3000.py <multi fasta file> <output Directory>  #
# Output : SINGLEFASTA file that sequence has length over 3000bp                 #
# Ouput filename : <input filename>_n.fa                                         #
##################################################################################

__author__ = 'hjgwak'
__version__ = "1.0.2"

import sys

def ParsePath(filename) :
	#split filename by '/'\
	#get last element
	name_list = filename.split('/')
	filename = name_list[len(name_list)-1]
	return filename

def ParseExtension(filename) :
	#if there are some '.' token, then parse name
	if filename.rfind('.') != -1 :
		filename = filename[:filename.rfind('.')]
	return filename

def ParseName(filename) :
	#remove all gap in filename
	#replace all '|' tokens to '_'
	#then, parse path and extension
	filename = filename.replace(' ', '')
	filename = filename.replace('|', '_')
	filename = ParsePath(filename)
	filename = ParseExtension(filename)
	return filename

def MeasureSequenceLength(sequence) :
	length = 0
	for fragment in sequence :
		length += len(fragment)
	return length

if len(sys.argv) < 3 :
	print "Please input FASTA file or output directory"
	print "python split.py <input fasta file> <output directory>"
	exit(1)
elif len(sys.argv) > 3 :
	print "Too many arguments"
	print "python split.py <input fasta file> <output directory>"
	exit(2)

total_cnt = 0
output_cnt = 0
ori_name = ParseName(sys.argv[1])
out_dir = sys.argv[2]
if out_dir[-1] != '/' :
	out_dir = out_dir + '/'
print "Start split '" + ori_name + "' to " + out_dir

input_file = open(sys.argv[1], 'r')
name = input_file.readline()
line = input_file.readline()
sequence = []
while line :
	if line[0] == '>' :
		total_cnt += 1
		slen = MeasureSequenceLength(sequence)
		if slen > 3000 :
			output_cnt += 1
			output_file = open(out_dir + ori_name + '_' + str(output_cnt) + '.fa', 'w')
			output_file.write(name)
			for fragment in sequence :
				output_file.write(fragment)
			output_file.close()
			sequence = []
			name = line
	else :
		sequence.append(line)
	line = input_file.readline()
slen = MeasureSequenceLength(sequence)
if slen > 3000 :
	output_cnt += 1
	output_file = open(out_dir + ori_name + "_" + str(output_cnt) + ".fa", 'w')
	output_file.write(name)
	for fragment in sequence :
		output_file.write(fragment)
	output_file.close()

input_file.close()
print "End split '" + ori_name + "' to " + out_dir
print "Total sequences : " + str(total_cnt)
print "Out sequences : " + str(output_cnt)
