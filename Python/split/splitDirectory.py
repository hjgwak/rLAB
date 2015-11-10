################################################################################################################
# Input : File name, File type number of files, number of directories, Y = make directories, N = don'y make    #
#         Files should be named <common part of name>_<number>.fa                                              #
#         e.g) 310752_ref_BalAcu1.0_1.fa ~ 310752_ref_BalAcu1.0_10775.fa                                       #
#                                                                                                              #
# Input command : python splitDirectory.py -name=<common part of name> -ext=<extension of file>                #
#                 -file=<number of total files> -dir=<number of directories> -make=<Y/N>                       #
#         e.g) python splitDirectory.py -name 310752_ref_BalAcu1.0 -ext=fa -file 10775 -dir 10 -make Y         #
#                                                                                                              #
# Output : separate files fairly in directory named split0 ~ split<dir-1>                                      #
# Caution : You must run this program in directory that involves files for split                               #
################################################################################################################

__author__ = 'hjgwak'

import os
import sys

def makeCMD(argv) :
	cmd = 'python'
	for arg in argv :
		cmd += ' ' + arg
	return cmd

def printInputCommand() :
	print "Command : python splitDirectory.py -name=<common part of name> -ext=<extension of file>"
	print "          -file=<number of total files> -dir=<number of directories> -make=<Y/N>"

# parse each arguments
def parseArguments(argv) :
	_name = ''
	_ext = ''
	_file = ''
	_dir = ''
	_make = ''
	for arg in argv :
		if arg.find('-name=') != -1 :
			_name = arg[6:]
		if arg.find('-ext=') != -1 :
			_ext = arg[5:]
		elif arg.find('-file=') != -1 :
			_file = arg[6:]
		elif arg.find('-dir=') != -1 :
			_dir = arg[5:]
		elif arg.find('-make=') != -1 :
			_make = arg[6:]
	return {'name':_name, 'ext':_ext, 'file':_file, 'dir':_dir, 'make':_make}

#check arguments are valid
def argTest(arg, inp_cmd) :
	if arg['name'] == '' :
		print "Please, Input the name information (-name=<common part of name>)"
		print "Your command : " + inp_cmd
		exit(2)
	if arg['ext'] == '' :
		print "Please, Input the extension information (-ext=<extension of file>)"
		print "Your command : " + inp_cmd
		exit(2)
	if arg['file'] == '' :
		print "Please, Input the file information (-file=<number of total files>)"
		print "Your command : " + inp_cmd
		exit(2)
	else :
		arg['file'] = int(arg['file'])
	if arg['dir'] == '' :
		print "Please, Input the dir information (-dir=<number of directories>)"
		print "Your command : " + inp_cmd
		exit(2)
	else :
		arg['dir'] = int(arg['dir'])
	if arg['make'] == '' :
		print "Please, Input the make information (-make=<Y/N> | Y = make directories for split, N = don't make)"
		print "Your command : " + inp_cmd
		exit(2)
	else :
		arg['make'] = arg['make'].upper()
	return arg

# make directories split0 ~ split<num> in current directory
def makeDirectories(num) :
	for i in range(num) :
		dir_name = 'split' + str(i)
		os.system('mkdir ' + dir_name)


#main body of program
inp_cmd = makeCMD(sys.argv)

if len(sys.argv) < 6 :
	print "Too short arguments"
	print "Your command : " + inp_cmd
	printInputCommand()
	exit(1)
elif len(sys.argv) > 6 :
	print "Too long arguments"
	print "Your command : " + inp_cmd
	printInputCommand()
	exit(1)

arg = parseArguments(sys.argv)
arg = argTest(arg, inp_cmd)

if arg['make'] == 'Y' :
	makeDirectories(arg['dir'])

cut = arg['file'] / arg['dir']
if arg['file'] % arg['dir'] > arg['dir'] / 2 :
	cut += 1

file_cnt = 0
cut_cnt = 0
dir_cnt = 0
while file_cnt < arg['file'] :
	file_cnt += 1
	cut_cnt += 1
	file_name = arg['name'] + '_' + str(file_cnt) + '.' + arg['ext']
	dir_name = 'split' + str(dir_cnt)
	os.system('mv ' + file_name + ' ' + dir_name)
	if cut_cnt >= cut :
		dir_cnt += 1
		cut_cnt = 0

print str(arg['file']) + " files were splited to " + str(arg['dir']) + " directories"
print "Each directories has " + str(cut) + " files"
