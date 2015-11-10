import sys

__author__ = "hjgwak"
__version__ = "1.0.1"

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def createOutFiles(name, num) :
	files = []
	for i in range(num) :
		fmt = name.find('.')
		file_name = name[:fmt] + "_" + str(i+1) + name[fmt:]
		out_f = open(file_name, 'w')
		files.append(out_f)

	return files
#[seq_info, seq, seq_info, quality]
def read4lines(_file) :
	lines = []
	for i in range(4) :
		line = _file.readline()
		if line :
			lines.append(line.rstrip('\r\n'))
		else :
			return None

	return lines

# main

if '-h' in sys.argv or '-help' in sys.argv :
	print "python split_fastq.py [fastq file] [number for split]"
	exit()

if len(sys.argv) != 3 :
	print "python split_fastq.py [fastq file] [number for split]"
	exit()

sp_num = int(sys.argv[-1])
input_f = open(sys.argv[1], 'r')
files = createOutFiles(getFileName(sys.argv[1]), sp_num)
lines = read4lines(input_f)

while lines :
	info1 = lines[0].split(' ')
	info2 = lines[2].split(' ')
	seq = lines[1]
	quality = lines[3]
	for i in range(sp_num) :
		seq_r = seq[i*len(seq)/sp_num:(i+1)*len(seq)/sp_num]
		qual_r = quality[i*len(quality)/sp_num:(i+1)*len(quality)/sp_num]
		name = [info1[0] + '.' + str(i+1), info1[1], "length=" + str(len(seq_r))]
		add = [info2[0] + '.' + str(i+1), info2[1], "length=" + str(len(qual_r))]
		files[i].write(' '.join(name) + "\n")
		files[i].write(seq_r + "\n")
		files[i].write(' '.join(add) + "\n")
		files[i].write(qual_r + "\n")
	lines = read4lines(input_f)

input_f.close()
for _file in files :
	_file.close()
