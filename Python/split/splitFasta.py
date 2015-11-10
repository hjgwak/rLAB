#########################################################################
# Input : MULTIFASTA file                                               #
# Input command : python split.py <multi fasta file> <output Directory> #
# Output : SINGLEFASTA files                                            #
# Output filename : <input filename>_n.fa                               #
#########################################################################

__author__ = 'hjgwak'
__version__ = '1.0.3'

import sys, os

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

def int2str(num, skel) :
	num = int(num)
	skel = str(skel)
	res = []

	for i in range(len(skel)) :
		res.append('0')
	idx = 1
	while num > 0 :
	 	res[-idx] = str(num % 10)
	 	num /= 10
	 	idx += 1
	return ''.join(res)

if len(sys.argv) < 3 :
	print "Please input FASTA file or output directory"
	print "python split.py <input fasta file> <output directory>"
	exit(1)
elif len(sys.argv) > 3 :
	print "Too many arguments"
	print "python split.py <input fasta file> <output directory>"
	exit(2)

output_cnt = 1
ori_name = ParseName(sys.argv[1])
out_dir = sys.argv[2]
if out_dir[-1] != '/' :
	out_dir = out_dir + '/'
print "Start split '" + ori_name + "' to " + out_dir

first = True
input_file = open(sys.argv[1], 'r')
line = input_file.readline()
output_file = open(out_dir + ori_name + '_' + str(output_cnt) + '.fa', 'w')
while line :
	if line[0] == '>' and first == False :
		output_file.close()
		output_cnt += 1
		output_name = out_dir + ori_name + '_' + str(output_cnt) + '.fa'
		output_file = open(output_name, 'w')
	output_file.write(line)
	line = input_file.readline()
	first = False

input_file.close()
output_file.close()

for i in range(1, output_cnt+1) :
	if len(str(i)) == len(str(output_cnt)) :
		break
	skel = out_dir + ori_name + '_'
	os.rename(skel + str(i) + '.fa', skel + int2str(i, str(output_cnt)) + '.fa')

print "End split '" + ori_name + "' to " + out_dir
print "Total sequences : " + str(output_cnt)
