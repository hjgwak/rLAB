############################################################################
# Input Command : python run_MGEScan_multi_dir.py <core values>            #
# core values :                                                            #
#        -genome=[dir]        : directory that has genomes                 #
#        -data=[dir]          : directory where the output will be saved   #
#        -hmmerv=#            : HMMER version 2 or 3                       #
#        -program=[L N B]     : L/ LTR, N/ nonLTR, B/Both                  #
#        -num=#               : number of directories                      #
# Output : MGEScan result in each directories                              #
#         * output directories have to be named res#                       #
#         * Input directories have to be numbered                          #
############################################################################

__author__ = "hjgwak"
__version__ = "1.0.1"

import sys, os, hj_toolkit

def printUSAGE() :
	print '''
############################################################################
# Input Command : python run_MGEScan_multi_dir.py <core values>            #
# core values :                                                            #
#        -genome=[dir]        : directory that has genomes                 #
#        -data=[dir]          : directory where the output will be saved   #
#        -hmmerv=#            : HMMER version 2 or 3                       #
#        -program=[L N B]     : L/ LTR, N/ nonLTR, B/Both                  #
#        -num=#               : number of directories                      #
# Output : MGEScan result in each directories                              #
#         * output directories have to be named [-data]#                   #
#         * Input directories have to be numbered                          #
############################################################################
'''

def userCMD(cmd) :
	print "Your command : " + cmd + "\n"

if __name__ == "__main__" :

	inp_cmd = "python " + ' '.join(sys.argv)

	if len(sys.argv) == 1 :
		print "\nPlease input some options (core values or -h(elp))"
		userCMD(inp_cmd)
		exit(0)
	
	if sys.argv[1] == "-h" or sys.argv[1] == "-help" :
		printUSAGE()
		exit(0)

	if len(sys.argv) > 6 :
		print "\ntoo long options! check usage"
		userCMD(inp_cmd)
		exit(1)
	elif len(sys.argv) < 6 :
		print "\ntoo short options! check usage"
		userCMD(inp_cmd)
		exit(1)

	argv = hj_toolkit.parseArgument(sys.argv)
	if argv.has_key('-genome') == False or argv.has_key('-data') == False or argv.has_key('-hmmerv') == False or argv.has_key('-program') == False or argv.has_key('-num') == False :
		print "\nWrong options! check your command"
		userCMD(inp_cmd)
		exit(1)

	for i in range(int(argv['-num'])) :
		genome = " -genome=" + argv['-genome'] + hj_toolkit.int2str(i, str(int(argv['-num'])-1))
		data = " -data=" + argv['-data'] + hj_toolkit.int2str(i, str(int(argv['-num'])-1))
		hmmerv = " -hmmerv=" + argv['-hmmerv']
		program = " -program=" + argv['-program']

		os.chdir(argv['-data'] + hj_toolkit.int2str(i, str(int(argv['-num'])-1)))
		os.system("/program/MGEScan1.3.1/run_MGEScan.pl" + genome + data + hmmerv + program + " > log.log &")
