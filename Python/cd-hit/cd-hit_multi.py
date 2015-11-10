###############################################################
# python cd-hit_multi.py [options] [-th #]  input directory   #
# options :                                                   #
#    all cd-hit-est options are vaild                         #
#    -H print cd-hit option table                             #
# -th : number of thread for cd-hit-multi.py. not for cd-hit  #
# (*) -i, -o options is automatically add.                    #
#     please, do not give this 2 options                      #
###############################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import sys, os, glob, threading

def printUSAGE() :
	print """
###############################################################
# python cd-hit_multi.py [options] [-th #]  input directory   #
# options :                                                   #
#    all cd-hit-est options are vaild                         #
#    -H print cd-hit option table                             #
# -th : number of thread for cd-hit-multi.py. not for cd-hit  #
# (*) -i, -o options is automatically add.                    #
#     please, do not give this 2 options                      #
###############################################################
"""

def printOptions() :
	print """
		====== CD-HIT version 4.6 (built on Jan 24 2014) ======

Usage: /program/cd-hit-v4.6.1-2012-08-27/cd-hit-est [Options] 

Options

   -i	input filename in fasta format, required
   -o	output filename, required
   -c	sequence identity threshold, default 0.9
 	this is the default cd-hit's "global sequence identity" calculated as:
 	number of identical amino acids in alignment
 	divided by the full length of the shorter sequence
   -G	use global sequence identity, default 1
 	if set to 0, then use local sequence identity, calculated as :
 	number of identical amino acids in alignment
 	divided by the length of the alignment
 	NOTE!!! don't use -G 0 unless you use alignment coverage controls
 	see options -aL, -AL, -aS, -AS
   -b	band_width of alignment, default 20
   -M	memory limit (in MB) for the program, default 800; 0 for unlimitted;
   -T	number of threads, default 1; with 0, all CPUs will be used
   -n	word_length, default 10, see user's guide for choosing it
   -l	length of throw_away_sequences, default 10
   -d	length of description in .clstr file, default 20
 	if set to 0, it takes the fasta defline and stops at first space
   -s	length difference cutoff, default 0.0
 	if set to 0.9, the shorter sequences need to be
 	at least 90% length of the representative of the cluster
   -S	length difference cutoff in amino acid, default 999999
 	if set to 60, the length difference between the shorter sequences
 	and the representative of the cluster can not be bigger than 60
   -aL	alignment coverage for the longer sequence, default 0.0
 	if set to 0.9, the alignment must covers 90% of the sequence
   -AL	alignment coverage control for the longer sequence, default 99999999
 	if set to 60, and the length of the sequence is 400,
 	then the alignment must be >= 340 (400-60) residues
   -aS	alignment coverage for the shorter sequence, default 0.0
 	if set to 0.9, the alignment must covers 90% of the sequence
   -AS	alignment coverage control for the shorter sequence, default 99999999
 	if set to 60, and the length of the sequence is 400,
 	then the alignment must be >= 340 (400-60) residues
   -A	minimal alignment coverage control for the both sequences, default 0
 	alignment must cover >= this value for both sequences 
   -uL	maximum unmatched percentage for the longer sequence, default 1.0
 	if set to 0.1, the unmatched region (excluding leading and tailing gaps)
 	must not be more than 10% of the sequence
   -uS	maximum unmatched percentage for the shorter sequence, default 1.0
 	if set to 0.1, the unmatched region (excluding leading and tailing gaps)
 	must not be more than 10% of the sequence
   -U	maximum unmatched length, default 99999999
 	if set to 10, the unmatched region (excluding leading and tailing gaps)
 	must not be more than 10 bases
   -B	1 or 0, default 0, by default, sequences are stored in RAM
 	if set to 1, sequence are stored on hard drive
 	it is recommended to use -B 1 for huge databases
   -p	1 or 0, default 0
 	if set to 1, print alignment overlap in .clstr file
   -g	1 or 0, default 0
 	by cd-hit's default algorithm, a sequence is clustered to the first 
 	cluster that meet the threshold (fast cluster). If set to 1, the program
 	will cluster it into the most similar cluster that meet the threshold
 	(accurate but slow mode)
 	but either 1 or 0 won't change the representatives of final clusters
   -r	1 or 0, default 1, by default do both +/+ & +/- alignments
 	if set to 0, only +/+ strand alignment
   -mask	masking letters (e.g. -mask NX, to mask out both 'N' and 'X')
   -match	matching score, default 2 (1 for T-U and N-N)
   -mismatch	mismatching score, default -2
   -gap	gap opening score, default -6
   -gap-ext	gap extension score, default -1
   -bak	write backup cluster file (1 or 0, default 0)
   -h	print this help

   Questions, bugs, contact Limin Fu at l2fu@ucsd.edu, or Weizhong Li at liwz@sdsc.edu
   For updated versions and information, please visit: http://cd-hit.org

   cd-hit web server is also available from http://cd-hit.org

   If you find cd-hit useful, please kindly cite:

   "Clustering of highly homologous sequences to reduce thesize of large protein database", Weizhong Li, Lukasz Jaroszewski & Adam Godzik. Bioinformatics, (2001) 17:282-283
   "Cd-hit: a fast program for clustering and comparing large sets of protein or nucleotide sequences", Weizhong Li & Adam Godzik. Bioinformatics, (2006) 22:1658-1659
"""

class divThread(threading.Thread) :
	def __init__(self, lock, stack, opts) :
		threading.Thread.__init__(self)
		self.lock = lock
		self.stack = stack
		self.opts = opts

	def run(self) :
		while True :
			inp = ''
			self.lock.acquire()
			if self.stack == [] :
				self.lock.release()
				break
			else :
				inp = self.stack.pop()
			self.lock.release()
			output = inp.split('/')[-1] + ".cdhit"
			os.system("~/program/cd-hit-v4.6.1-2012-08-27/cd-hit-est -i " + inp + " -o " + output + " " + self.opts + " > " + output + ".log")

#main part of program

if len(sys.argv) < 2 :
	printUSAGE()
	print "Your command : python " + " ".join(sys.argv)
	exit(1)

if sys.argv[1] == '-h' :
	printUSAGE()
	exit(0)
elif sys.argv[1] == '-H' :
	printOptions()
	exit(0)

files = glob.glob(sys.argv[-1] + '*')
threads = 1
opts = ''

if (sys.argv[-3] == '-th') :
	threads = int(sys.argv[-2])
	opts = ' '.join(sys.argv[1:-3])
else :
	opts = ' '.join(sys.argv[1:-1])

print threads

thread_list = []
lock = threading.Lock()
for i in range(threads) :
	thread = divThread(lock, files, opts)
	thread_list.append(thread)

for thread in thread_list :
	thread.start()

for thread in thread_list :
	thread.join()

#option code
os.mkdir("clstr/")
os.mkdir("seq/")
os.mkdir("log/")
os.system("mv *.clstr clstr/")
os.system("mv *.log log/")
os.system("mv *.cdhit seq/")
