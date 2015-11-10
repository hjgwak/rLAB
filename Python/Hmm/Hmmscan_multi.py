########################################################################################
# Input command : python Hmmscan_multi.py [options] <hmm directory> <seq file>         #
# Options :                                                                            #
#      -o=                : direct output to file <f>, not stdout                      #
#      --tblout           : save parseable table of per-sequence hits to file <s>      #
#      --domtblout        : save parseable table of per-domain hits to file <s>        #
#      --pfamtblout       : save table of hits and domains to file, in Pfam format <s> #
#      -cpu=#             : number of parallel CPU workers to use for multithreads     #
#      -h                 : print USAGE                                                #
# Output : <model_name>.out[.tblout, .domout, .pfamout] per each hmm models            #
########################################################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import glob, threading, sys, os, hj_toolkit

class runHmmThread(threading.Thread) :
	def __init__(self, options, hmms, seq) :
		threading.Thread.__init__(self)
		self.opts = options
		self.hmms = hmms
		self.seq = seq

	def makeFullOpt(self, options, hmm) :
		full_opt = ""
		hmm_name = hmm.split('/')
		hmm_name = hmm_name[-1]
		for opt in options :
			full_opt += opt + " " + hmm_name
			if opt == '-o' :
				full_opt += ".out "
			elif opt == '--tblout' :
				full_opt += ".tblout "
			elif opt == '--domtblout' :
				full_opt += ".domout "
			elif opt == '--pfamtblout' :
				full_opt += ".pfamout "
		return full_opt

	def run(self) :
		for hmm in self.hmms :
			cmd = "/program/hmmer-3.1b1-linux-intel-x86_64/src/hmmscan "
			cmd += self.makeFullOpt(opts, hmm)
			cmd += hmm + " " + self.seq
			os.system(cmd)

def printUSAGE() :
	print """
########################################################################################
# Input command : python Hmmscan_multi.py [options] <hmm directory> <seq file>         #
# Options :                                                                            #
#      -o                 : direct output to file <f>, not stdout                      #
#      --tblout           : save parseable table of per-sequence hits to file <s>      #
#      --domtblout        : save parseable table of per-domain hits to file <s>        #
#      --pfamtblout       : save table of hits and domains to file, in Pfam format <s> #
#      -cpu #             : number of parallel CPU workers to use for multithreads     #
#      -h                 : print USAGE                                                #
# Output : <model_name>.out[.tblout, .domout, .pfamout] per each hmm models            #
########################################################################################
"""

def checkValidArguments(argv) :
	arg_cnt = 0;
	for arg in argv :
		if arg == '-o' or arg == '--tblout' :
			arg_cnt += 1
		elif arg == '--domtblout' or arg == '--pfamtblout' :
			arg_cnt += 1
		elif arg == '-cpu' and argv[argv.index('-cpu') + 1].isdigit() :
			arg_cnt += 2
		elif arg[-1:] == '/' or arg[-2:] == 'fa' or arg[-5:] == 'fasta' or arg[-3:] == 'fst' :
		 	arg_cnt += 1
	if len(argv) != arg_cnt :
		print "\nWrong option!, check your command!"
		print hj_toolkit.makeCMD(argv)
		exit(1)

# main part of program

if len(sys.argv) == 2 and sys.argv[1] == '-h' :
	printUSAGE()
	exit(1)
elif len(sys.argv) < 3 :
	print "\nToo short arguments!, please check your command!"
	print hj_toolkit.makeCMD(sys.argv)
	exit(1)
elif len(sys.argv) > 10 :
	print "\nToo long arguments!, please check your command!"
	print hj_toolkit.makeCMD(sys.argv)
	exit(1)

argv = sys.argv[1:]
checkValidArguments(argv)

hmm = ""
seq = ""
cpu = 0
rm_list = []

for arg in argv : 
	if arg[-1:] == "/" :
		hmm = arg
		rm_list.append(arg)
	elif arg[-3:] == ".fa" or arg[-6:] == ".fasta" or arg[-4:] == ".fst" :
		seq = arg
		argv.remove(arg)
	elif arg == "-cpu" :
		cpu = int(argv[argv.index('-cpu')+1])
		rm_list.append(str(cpu))
		rm_list.append(arg)

for rm in rm_list :
	argv.remove(rm)
opts = argv

glob_hmm = glob.glob(hmm + '*.hmm')
hmm_per_thread = len(glob_hmm) / cpu
hmm_list = []
for i in range(cpu-1) :
	hmm_list.append(glob_hmm[:hmm_per_thread])
	glob_hmm = glob_hmm[hmm_per_thread:]
hmm_list.append(glob_hmm)

thread_list = []
for hmm in hmm_list :
	thread = runHmmThread(opts, hmm, seq)
	thread_list.append(thread)

for thread in thread_list :
	thread.start()
