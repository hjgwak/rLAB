###############################################################################
# Input command : python intersectGFF.py [options] file1 file2                #
#                 (*) file1,2 must gff format                                 #
# Options :                                                                   #
#     -s (sort)              : Sort by start position before main process     #
#     -m (minimum)           : If there are many data in file2 intersected    #
#                              data in file1, then keep data that has minimum #
#                              intersect score                                #
#     -M (Maximum)           : If there are multi data in file2 intersected   #
#                              data in file1, then keep data that has Maximum #
#                              intersect score                                #
#     -e (exclusice)         : post data in file1 that has no intersect       #
#     -c # (cpu)             : set number of thread for running program       #
#     -h (help)              : print USAGE                                    #
# Ouput :                                                                     #
#     default GFF format + [seq number in file2]                              #
###############################################################################

import sys, hj_toolkit

def printUSAGE() :
	print """
###############################################################################
# Input command : python intersectGFF.py [options] file1 file2                #
#                 (*) file1,2 must gff format                                 #
# Options :                                                                   #
#     -s (sort)              : Sort by start position before main process     #
#     -m (minimum)           : If there are many data in file2 intersected    #
#                              data in file1, then keep data that has minimum #
#                              intersect score                                #
#     -M (Maximum)           : If there are multi data in file2 intersected   #
#                              data in file1, then keep data that has Maximum #
#                              intersect score                                #
#     -e (exclusice)         : post data in file1 that has no intersect       #
#     -c # (cpu)             : set number of thread for running program       #
#     -r file (redirect)     : redirect output, default is stdout             #
#     -h (help)              : print USAGE                                    #
# Ouput :                                                                     #
#     default GFF format + [intersect score] [seq number in file2]            #
#     (*) If you give -e option, then intersecr score is 0                    #
###############################################################################
"""

def comp(a, b) :
	first = int(a.split('\t')[3])
	second = int(b.split('\t')[3])
	return first - second

def checkValidOpt(argv, cmd) :
	opts = {"-s" : False, "-m" : False, "-M" : False, "-e" : False, "-c" : 1}
	prev = ""
	for arg in argv :
		if prev == "-c" :
			try :
				opts["-c"] = int(arg)
				continue
			except ValueError :
				print >>sys.stderr, "\nplease input natual number for CPU option"
				print >>sys.stderr, "Your command : " + cmd + "\n"
				exit(1)
		if prev == "-r" :
			sys.stdout = open(arg, "w")
			continue
		if opts.has_key(arg) and arg != "-c":
			opts[arg] = True
		elif arg == "-c" or arg == "-r" :
			prev = arg
			continue
		else :
			print >>sys.stderr, "\nWrong option! check your command"
			print >>sys.stderr, "Your command : " + cmd + "\n"
			exit(1)
		prev = arg
	
	if opts["-m"] and opts["-M"] :
		print >>sys.stderr, "\n-m and -M options are exclusive"
		print >>sys.stderr, "Your command : " + cmd + "\n"
	return opts

# main part of program

userCMD = hj_toolkit.makeCMD(sys.argv)

if len(sys.argv) == 2 and sys.argv[1] == "-h" :
	printUSAGE()
	exit(0)
elif len(sys.argv) < 3 :
	print >>sys.stderr, "\nplease input right format"
	print >>sts.stderr, "Your command : " + userCMD + "\n"

opts = checkValidOpt(sys.argv[1:-2], userCMD)

_file1 = open(sys.argv[-2], "r")
_file2 = open(sys.argv[-1], "r")

_data1 = _file1.readlines()
_file1.close()
_data2 = _file2.readlines()
_file2.close()

if opts['-s'] :
	_data1.sort(comp)
	_data2.sort(comp)
