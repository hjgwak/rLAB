import sys, os, glob

__author__ = "hjgwak"
__version__ = "1.0.1"

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def makeHash(name) :
	res = {}
	fasta = open(name, "r")

	name = ""
	seq = ""
	for line in fasta.readlines() :
		line = line.rstrip("\r\n")
		if line[0] == ">" :
			if name != "" and seq != "" :
				res[name] = seq
			name = line[1:]
			seq = ""
		else :
			seq += line
	if name != "" and seq != "" :
		res[name] = seq

	fasta.close()

	return res

def getClstrInfo(name) :
	tp = name[:name.find('.')]
	tp = tp.split('_')

	return tuple(tp)

def makeTempSeq(ltr, info) :
	global whale_dic

	seq_dic = makeHash(whale_dic[info[1]] + info[2] + "/whole_seq." + info[2])
	ltr_f = open(ltr, 'r')
	out_f = open('./temp/' + getFileName(ltr), 'w')
	done = []

	for line in ltr_f.readlines() :
		line = line.rstrip('\r\n')
		seq = line[:line.find('\t')]
		
		if seq in done :
			continue

		out_f.write(">" + seq + "\n")
		out_f.write(seq_dic[seq] + "\n")
		done.append(seq)

	ltr_f.close()

# main

if len(sys.argv) != 2 :
	print "python additional_clstr.py [m0.parse.ltr dir]"
	exit()

whale_dic = {
	"Lipotes" : "/data1/hjgwak/whale/118797_ref_Lipotes_vexillifer_v1_chrUn/MGEScan/sub_seq/",
	"Physeter" : "/data1/hjgwak/whale/9755_ref_Physeter_macrocephalus-2.0.2_chrUn/MGEScan/sub_seq/",
	"Ttru" : "/data1/hjgwak/whale/ttn_ref_Ttru_1.4_chrUn/MGEScan/sub_seq/",
	"Oorc" : "/data1/hjgwak/whale/oor_ref_Oorc_1.1_chrUn/MGEScan/sub_seq/",
	"BalAcu" : "/data1/hjgwak/whale/310752_ref_BalAcu1.0_chrUn/MGEScan/sub_seq/"
}

ltr_files = glob.glob(makeDirForm(sys.argv[1]) + "*.ltr")

os.mkdir("temp")
os.mkdir("cd-hit")

for ltr in ltr_files :
	ltr_name = getFileName(ltr)
	ltr_info = getClstrInfo(ltr_name)
#	print ltr_info
	makeTempSeq(ltr, ltr_info)
	os.system("~/program/cd-hit-v4.6.1-2012-08-27/cd-hit-est -i ./temp/" + ltr_name + " -o ./cd-hit/" + ltr_name + ".cdhit -c 0.8 -M 0 -n 5 -d 100 -s 0.8 -G 0 -aL 0.8")
