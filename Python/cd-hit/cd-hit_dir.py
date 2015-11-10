import os

sims = [90, 85, 80, 75, 70]
n = {100 : 10, 95: 8, 90: 7, 85: 6, 80: 5, 75: 4, 70: 3}

for sim in sims :
	os.chdir("sim" + str(sim))
	kinds = ['first', 'second']
	for kind in kinds :
		os.mkdir(kind)
		os.chdir(kind)
		overs = [60, 65, 70, 75, 80]
		for over in overs :
			os.mkdir("over" + str(over))
			os.chdir("over" + str(over))
			os.system("python ~/Python/save_log.py python ~/Python/cd-hit/cd-hit_multi.py -c " + str(sim/100.0) + " -M 0 -n " + str(n[sim]) + " -d 100 -G 0 -aS " + str(over/100.0) + " -th 3 /data1/hjgwak/whale/310752_ref_BalAcu1.0_chrUn/MGEScan/parse4seq/" + kind + "/ > log.log_w")
			os.chdir("../")
		os.chdir("../")
	os.chdir("../")
