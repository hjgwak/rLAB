import sys, os

__author__ = "hjgwak"
__version__ = "1.0.1"

def makeDirForm(string) :
	if string[-1] != '/' :
		string = string + '/'
	return string

def getFileName(path) :
	split = path.split('/')
	return split[-1]

def getWhaleMark(path) :
	res = ""
	if "Lipotes" in path :
		res = "Lipotes"
	elif "Physeter" in path :
		res = "Physeter"
	elif "Ttru" in path :
		res = "Ttru"
	elif "Oorc" in path :
		res = "Oorc"
	elif "BalAcu" in path :
		res = "BalAcu"

	return res

def doBLAST(db, num, whales, part) :
	for whale in whales :
		cmd = "blastn -db " + db + "cluster" + str(num) + "." + part
		cmd += " -out cluster" + str(num) + "_" + getWhaleMark(whale) + "_" + part + ".m0"
		cmd += " -query " + whale + " -outfmt 0"
		os.system(cmd)

# main	
	
if len(sys.argv) != 3 :
	print "python whale_valid.py [cd-hit output] [blast db dir]"
	exit()

whale_dic = {
	"Lipotes" : "/data1/hjgwak/whale/118797_ref_Lipotes_vexillifer_v1_chrUn/118797_ref_Lipotes_vexillifer_v1_chrUn.fa",
	"Physeter" : "/data1/hjgwak/whale/9755_ref_Physeter_macrocephalus-2.0.2_chrUn/9755_ref_Physeter_macrocephalus-2.0.2_chrUn.fa",
	"Ttru" : "/data1/hjgwak/whale/ttn_ref_Ttru_1.4_chrUn/ttn_ref_Ttru_1.4_chrUn.fa",
	"Oorc" : "/data1/hjgwak/whale/oor_ref_Oorc_1.1_chrUn/oor_ref_Oorc_1.1_chrUn.fa",
	"BalAcu" : "/data1/hjgwak/whale/310752_ref_BalAcu1.0_chrUn/310752_ref_BalAcu1.0_chrUn.fa"
}

db = makeDirForm(sys.argv[2])
part = getFileName(db[:-1])

cdhit = open(sys.argv[1], 'r')

flag = False
clstr_num = 0
whale = [whale_dic["Lipotes"], whale_dic["Physeter"], whale_dic["Ttru"], whale_dic["Oorc"], whale_dic["BalAcu"]]
for line in cdhit.readlines() :
	line = line.rstrip("\r\n")
	if line[0] == ">" :
		if flag and len(whale):
			doBLAST(db, clstr_num, whale, part)
			print "Finish BLAST : cluster" + str(clstr_num)
		flag = True
		clstr_num += 1
		whale = [whale_dic["Lipotes"], whale_dic["Physeter"], whale_dic["Ttru"], whale_dic["Oorc"], whale_dic["BalAcu"]]
	else :
		if "Lipotes" in line and whale_dic["Lipotes"] in whale :
			whale.remove(whale_dic["Lipotes"])
		if "Physeter" in line and whale_dic["Physeter"] in whale :
			whale.remove(whale_dic["Physeter"])
		if "Ttru" in line and whale_dic["Ttru"] in whale :
			whale.remove(whale_dic["Ttru"])
		if "Oorc" in line and whale_dic["Oorc"] in whale :
			whale.remove(whale_dic["Oorc"])
		if "BalAcu" in line and whale_dic["BalAcu"] in whale :
			whale.remove(whale_dic["BalAcu"])

if flag and len(whale) :
	doBLAST(db, clstr_num, whale, part)
