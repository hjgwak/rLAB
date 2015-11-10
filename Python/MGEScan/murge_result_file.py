import sys, os, glob

def printCurDir() :
	print "cur in " + os.getcwd()

for i in range(int(sys.argv[1])) :
	if i == 0 :
		os.chdir("./res0")
	else :
		os.chdir("../res" + str(i))
	printCurDir()
	os.system("cp *.dat ../res_all/")
	main = os.getcwd()
	res = glob.glob("./*")
	if "./genome" in res :
		os.chdir("./genome/")
		printCurDir()
		os.system("cp * ../../res_all/genome")
		os.chdir(main)
	if "./ltr" in res :
		os.chdir("./ltr/")
		printCurDir()
		ltr = os.getcwd()
		ltr_f = glob.glob("./*")
		if "./ir_seq" in ltr_f :
			os.chdir("./ir_seq/")
			printCurDir()
			os.system("cp * ../../../res_all/ltr/ir_seq/")
			os.chdir(ltr)
		if "./ltr" in ltr_f :
			os.chdir("./ltr/")
			printCurDir()
			os.system("cp * ../../../res_all/ltr/ltr/")
			os.chdir(ltr)
		if "./ltr_seq" in ltr_f :
			os.chdir("./ltr_seq/")
			printCurDir()
			os.system("cp * ../../../res_all/ltr/ltr_seq/")
			os.chdir(ltr)
		os.chdir(main)
