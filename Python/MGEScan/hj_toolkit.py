__author__ = 'hjgwak'
__version__ = '1.0.1'

import sys

def printUSAGE() :
	print
'''
[0]
int2str : 
	[options]
	-num=<number>                : integer for change string
	-skel=<number>               : integer for skeleton
	[example]
	python hj_toolkit.py -mode=0 -num=123 -skel=10000
	==> '00123'

[1]
parseArgument :
	[options]
	-name_option=<information>   : any arguments
	[example]
	python hj_toolkit.py -mode=1 -option=hello -opt=world
	==> {'-option':'hello', '-opt':'world'}
'''

'''
function : make integer to string that aligned by skel
input : integer to type change
        skel for alignment
example : int2str(123, '10000')
          ==> '00123'
'''
def int2str(num, skel) :
	num = int(num)
	skel = str(skel)
	res = []

	for i in range(len(skel)) :
		res.append('0')
	idx = 1
	while num > 0 :
	 	res[-idx] = str(num % 10)
	 	num /= 10
	 	idx += 1
	return ''.join(res)

'''
function : argument parsing, arguments are identified by '='
input : argument vector
example : python program.py -opt=1 -op=2
          ==> {'-opt':1, '-op':2}
'''
def parseArgument(argv) :
	dic = {}
	for arg in argv :
		idx = arg.find('=')
		if idx != -1 :
			dic[arg[:idx]] = arg[idx+1:]
	return dic

if __name__ == 'main' :
	argv = parseArgument(sys.argv)
	mode = ''
	
	try :
		if sys.argv[1].lower() == '-h' :
			printUSAGE()
			exit(0)
		if argv.has_key('-mode') :
			mode = argv['-mode']
		else :
		 	print "\nERROR: improper command, please input mode option"
		 	exit(1)

	except IndexError :
		print "\nERROR: improper command, check your command\n"

	except Exception as e :
		print "\n\nError with:\n" + str(e) + '\n'

	else :
		if mode == '0' :
			print int2str(argv['-num'], str(argv['-skel']))
		elif mode == '1' :
			print parseArgument(sys.argv)
