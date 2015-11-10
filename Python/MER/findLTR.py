##########################################################################
# Input format : python findLTR.py [options] <core values>               #
# Core Values :                                                          #
#     -f= dir              : path of dir that has fasta files            #
#     -l= #                : minimum seed length                         #
# Options [Default] :                                                    #
#     -r= file             : output file [stdout]                        #
#     -e= file             : Error log file [stderr]                     #
#     -d= #                : minimum distance of seed [0]                #
#     -D= #                : maximum distance of seed[2147483647]        #
#     -b= #                : boundary of result length of ltr [0]        #
#     -c= #                : number of cpu for program [1]               #
#     -h                   : print USAGE                                 #
# Ouput : LTR                                                            #
##########################################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import sys, os, threading, datetime, glob, hj_toolkit, path

# part of functions

def printUSAGE() : 
	sys.stderr.write("""
##########################################################################
# Input format : python findLTR.py [options] <core values>               #
# Core Values :                                                          #
#     -f= dir              : path of dir that has fasta files            #
#     -l= #                : minimum seed length                         #
# Options [Default] :                                                    #
#     -r= file             : output file [stdout]                        #
#     -e= file             : Error log file [stderr]                     #
#     -d= #                : minimum distance of seed [0]                #
#     -D= #                : maximum distance of seed[2147483647]        #
#     -b= #                : boundary of result length of ltr [0]        #
#     -c= #                : number of cpu for program [1]               #
#     -h                   : print USAGE                                 #
# Ouput : LTR                                                            #
##########################################################################
\n""")

def checkCoreValues(argv, cmd) :
	fail = False
	if argv.has_key('-f') == False :
		sys.stderr.write("\nfasta file miss\n")
		fail = True
	if argv.has_key('-l') == False :
		sys.stderr.write("\nlmin info miss\n")
		fail = True

	if fail :
		sys.stderr.write("check your command : " + cmd + "\n")
		printUSAGE()
		exit(1)

def checkValidOpt(argv, cmd) :
	valid = ['-f', '-l', '-r', '-e', '-d', '-D', '-b', '-c']
	args = argv.keys()

	for arg in args :
		try :
			valid.index(arg)
		except ValueError :
			sys.stderr.write("Wrong option!\n")
			sys.stderr.write("check your command : " + cmd + "\n")
			printUSAGE()
			exit(2)

def runMER(argv, fasta) :
	global tseed_dir
	cmd = path.MER_PATH + " -i " + fasta
	out_path = tseed_dir + fasta.split('/')[-1] + '.tseed'
	cmd += " -o " + out_path + " -s " + argv['-l'] + " -S "
	if argv.has_key('-d') :
		cmd += " -d " + argv['-d']
	if argv.has_key('-D') :
		cmd += " -D " + argv['-D']
	os.system(cmd)

def seedPostProcessing(argv, fasta) :
	global tseed_dir, seed_dir
	fasta_name = fasta.split('/')[-1]
	cmd = "python " + path.SEED_POST_PATH
	tseed_path = tseed_dir + fasta_name + '.tseed'
	seed_path = seed_dir + fasta_name + '.seed'
	cmd += " " + tseed_path + " > " + seed_path
	os.system(cmd)

def runRepSeek(argv, fasta) :
	global tmp_dir, seed_dir
	cmd = path.REPSEEK_PATH
	fasta_name = fasta.split('/')[-1]
	out_path = tmp_dir + fasta_name + '.tmp'
	seed_path = seed_dir + fasta_name + '.seed'
	cmd += " -r " + out_path + " -s " + seed_path + " -l " + argv['-l'] + " " + fasta
	os.system(cmd)

def mergeResults(bound) :
	global tmp_dir
	tmp_list = glob.glob(os.getcwd() + "/" + tmp_dir + "*")
	tmp_list.sort()
	for tmp in tmp_list :
		_file = open(tmp, "r")
		print "-----" + tmp.split('/')[-1][:-4] + "-----"
		lines = _file.readlines()
		_file.close()
		for line in lines :
			comp = line.split('\t')
			if int(comp[3]) >= bound and int(comp[4]) >= bound :
				print line[:-1]

# part of classes and threads

class divThread(threading.Thread) :
	def __init__(self, argv, fasta_stack, lock, num) :
		threading.Thread.__init__(self)
		self.argv = argv
		self.fasta_stack = fasta_stack
		self.lock = lock
		self.num = num
		self.cnt = 0

#	def __del__(self) :
#		sys.stderr.write("Thread" + str(self.num) + " is done.\n")
#		sys.stderr.write("Thread" + str(self.num) + " was finished " + str(self.cnt) + " jobs\n")

	def run(self) :
		while True :
			fasta = ""
			self.lock.acquire()
			if self.fasta_stack == [] :
				self.lock.release()
				break
			else :
				fasta = self.fasta_stack.pop()
			self.lock.release()
			runMER(self.argv, fasta)
			seedPostProcessing(self.argv, fasta)
			runRepSeek(self.argv, fasta)
			self.cnt += 1

# main part of program

if len(sys.argv) == 2 and sys.argv[1] == "-h" :
	printUSAGE()
	exit(0)

argv = hj_toolkit.parseArgument(sys.argv)
checkCoreValues(argv, hj_toolkit.makeCMD(sys.argv))
checkValidOpt(argv, hj_toolkit.makeCMD(sys.argv))

if argv.has_key('-r') :
	sys.stdout = open(argv['-r'], "w")
if argv.has_key('-e') :
	sys.stderr = open(argv['-e'], "a")

	#prepare temp directories
dt = str(datetime.datetime.now())[:19].replace(' ','_').replace(':','')
seed_dir = 'LTR_' + dt + '/seed/'
tseed_dir = 'LTR_' + dt + '/tseed/'
tmp_dir = 'LTR_' + dt + '/tmp/'
os.mkdir('LTR_' + dt)
os.mkdir(seed_dir)
os.mkdir(tseed_dir)
os.mkdir(tmp_dir)

	#get datas for running program
fasta_files = glob.glob(argv['-f'] + "*")
cpu = 1
if argv.has_key('-c') :
	try :
		cpu = int(argv['-c'])
	except ValueError :
		sys.stderr.write("ERROR : wrong cpu number!, please input natural number\n")
		exit(2)
bound = 0
if argv.has_key('-b') :
	try :
		bound = int(argv['-b'])
	except ValueError :
		sys.stderr.write("ERROR : wrong boundary number!, please input natural number\n")
		exit(2)

	#make threads and start to compute
thread_list = []
lock = threading.Lock()
for i in range(cpu) :
	thread = divThread(argv, fasta_files, lock, i)
	thread_list.append(thread)

for thread in thread_list :
	thread.start()

for thread in thread_list :
	thread.join()

mergeResults(bound)

os.system("rm -r LTR_" + dt)
