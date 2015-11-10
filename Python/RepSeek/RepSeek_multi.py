###############################################################################################
#  [RepSeek_multi.py]                                                                         #
#  Input command : python RepSeek_multi.py <Core Values> [options]                            #
#  Core Values : -fasta=<directory>     : directory which invloves fasta files                #
#                -name=<file name>      : output file name                                    #
#                -l=<L min value>       : L min value for executing RepSeek                   #
#  Options     : -out=<directory>       : directory for output                                #
#                -cut=<cutoff>          : cutoff for result LTRs                              #
#                -h(elp)                : print usage                                         #
#  Input : Directory which involves fasta files, directory for output,                        #
#          output file name, Options for excuting RepSeek                                     #
#          *Directory name must be given by absolute path                                     #
#  Output : A set of RepSeek output. If you give the cut option, then a set of RepSeek ouput  # 
#           except LTRs which length under cutoff                                             #
###############################################################################################

__author__ = "hjgwak"
__version__ = "1.0.2"

import sys, os, datetime, time

def printUSAGE() : 
	print """
###############################################################################################
#  [RepSeek_multi.py]                                                                         #
#  Input command : python RepSeek_multi.py <Core Values> [options]                            #
#  Core Values : -fasta=<directory>     : directory which invloves fasta files                #
#                -name=<file name>      : output file name                                    #
#                -l=<L min value>       : L min value for executing RepSeek                   #
#  Options     : -out=<directory>       : directory for output                                #
#                -cut=<cutoff>          : cutoff for result LTRs                              #
#                -h(elp)                : print usage                                         #
#  Input : Directory which involves fasta files, directory for output,                        #
#          output file name, Options for excuting RepSeek                                     #
#          *Directory name must be given by absolute path                                     #
#  Output : A set of RepSeek output. If you give the cut option, then a set of RepSeek ouput  # 
#           except LTRs which length under cutoff                                             #
###############################################################################################
"""

def parseArguments(argv) :
	dic = {}
	for arg in argv :
		idx = arg.find('=')
		if idx != -1 :
			dic[arg[:idx]] = arg[idx+1:]
	return dic

def runRepSeek(fst_dir, rs_dir, Lmin) :
	cnt = 0
	if fst_dir[-1] != '/' :
		fst_dir += '/'
	os.system('ls ' + fst_dir + ' > ' + rs_dir + '/RepSeek_ls.tmp')

	fst_list = open(rs_dir + '/RepSeek_ls.tmp', 'r')
	fasta = fst_list.readline()
	while fasta :
		cnt += 1
		if fasta[-1] == '\n' :
			fasta = fasta[:-1]
		cmd = "/program/RepSeek/repseek -r " + rs_dir + "/RepSeek_res/"
		cmd += fasta + ".tmp -l " + str(Lmin) + " " + fst_dir + fasta
		os.system(cmd)
		fasta = fst_list.readline()
	fst_list.close()
	return cnt

def mergeResult(rs_dir, out_dir, cut = 0) :
	os.system('ls ' + rs_dir + '/RepSeek_res/ > ' + rs_dir + '/RepSeek_res.tmp')	

	res_list = open(rs_dir + '/RepSeek_res.tmp', 'r')
	out_file = open(out_dir, 'w')
	res = res_list.readline()
	while res :
		if res[-1] == '\n' :
			res = res[:-1]
		out_file.write("-----" + res[:-4] + "-----\n")
		res_file = open(rs_dir + '/RepSeek_res/' + res, 'r')
		outs = res_file.readlines()
		res_file.close()
		for out in outs :
			tmp = out.split('\t')
			if int(tmp[3]) >= cut and int(tmp[4]) >= cut :
				out_file.write(out)
		res = res_list.readline()
	out_file.close()
	res_list.close()

def makeSimpleTime(time) :
	sec_t = time % 60
	time = int(time) / 60
	min_t = time % 60
	time /= 60
	hour_t = time % 24
	res = "%dd%dh%dm%0.2fs" % (time / 24, hour_t, min_t, sec_t)
	return res

if __name__ == "__main__" :
	inp_cmd = "python " + ' '.join(sys.argv)

	if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "-help" :
		printUSAGE()
		exit(0)

	argv = parseArguments(sys.argv)

	if argv.has_key('-fasta') == False or argv.has_key('-name') == False or argv.has_key('-l') == False :
		print "\nLack of Core Values! please check Usage (you can check usage with -h option)\n"
		print "check your command : " + inp_cmd
		exit(1)
	elif len(argv) > 5 :
		print "\nToo many arguments! please check the Usage (you can check usage with -h option)\n"
		print "check your command : " + inp_cmd
		exit(1)
	#make value type of options correct
	argv['-l'] = int(argv['-l'])
	if argv.has_key('-cut') :
		argv['-cut'] = int(argv['-cut'])
	#make datetime information
	dt = str(datetime.datetime.now())[:19].replace(' ','_').replace(':','')

	#make temp directory
	rs_dir = 'RS_multi_' + dt
	os.mkdir(rs_dir)
	os.mkdir(rs_dir + '/RepSeek_res')

	#run RepSeek and measure total running time, average running time
	start_time = time.time()
	cnt = runRepSeek(argv['-fasta'], rs_dir, argv['-l'])
	end_time = time.time()

	#merge each result file in one
	out_dir = ''
	if argv.has_key('-out') :
		out_dir += argv['-out']
	if out_dir != '' and out_dir[-1] != '/'	:
		out_dir += '/'
	out_dir += argv['-name']
	
	if argv.has_key('-cut') :
		mergeResult(rs_dir, out_dir, argv['-cut'])
	else :
		mergeResult(rs_dir, out_dir)

	#print running time information
	run_time = end_time - start_time
	print "Total running : " + makeSimpleTime(run_time)
	print "Average time : " + makeSimpleTime(run_time/cnt)
	print "Total number of files : " + str(cnt)

	os.system('rm -r ' + rs_dir)
