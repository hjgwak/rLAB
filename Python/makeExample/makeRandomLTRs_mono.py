#################################################################################################
# Input command: python makeRandomLTRs_mono.py -LTR=<F/R/D> [options] -SIM=<F/R/D> [options]    #
#                -PT=<F/R> [options] -TOTAL=<F/R> [options] -num=<number of examples>           #
# Short words : F = fix, R = random, D = uniformly decrease upper bound to lower bound          #
# Options : -LTR_f=<length of LTRs(bp)>               : It is necessary for F state of -LTR,    #
#                                                       Input the fixed length of LTRs          #
#           -LTR_d=<difference of lenght of LTRs(bp)> : It is necessary for D state of -LTR,    #
#                                                       Input the difference between LTRs       #
#           -SIM_f=<fixed similarity(%)>              : It is necessary for F state of -SIM,    #
#                                                       Input the fixed similarity of LTRs      #
#           -SIM_d=<difference of similarity(%p)>     : It is necessary for D state of -SIM,    #
#                                                       Input the difference between similarity #
#           -PT_f=<fixed length of protein(bp)>       : It is necessary for F state of -PT      #
#                                                       Input the fixed length of protein       #
#           -TOTAL_f=<fixed length of sequence(bp)>   : It is necessary for F state of -TOTAL   #
#                                                       Input the fixed length of sequence      #
#           -h(elp)                                   : print help text                         #
# Input Example : python makeRandomLTRs_mono.py -LTR=R -SIM=D -SIM_d=5 -PT=R -TOTAL=R -num=1000 #
# Output : Genome sequences that have only one pair of LTRs. Protein sequence that is enwrapped #
#          by LTR, it is random sequence that have no meanings                                  #
# Output format : MULTIFASTA file                                                               #
#################################################################################################

__author__ = 'hjgwak'
__version__ = '1.0.2'

import random
import sys
import os
import datetime
import const

def printHelp() :
	print '''
#################################################################################################
# Input command: python makeRandomLTRs_mono.py -LTR=<F/R/D> [options] -SIM=<F/R/D> [options]    #
#                -PT=<F/R> [options] -TOTAL=<F/R> [options] -num=<number of examples>           #
# Short words : F = fix, R = random, D = uniformly decrease upper bound to lower bound          #
# Options : -LTR_f=<length of LTRs(bp)>               : It is necessary for F state of -LTR,    #
#                                                       Input the fixed length of LTRs          #
#           -LTR_d=<difference of lenght of LTRs(bp)> : It is necessary for D state of -LTR,    #
#                                                       Input the difference between LTRs       #
#           -SIM_f=<fixed similarity(%)>              : It is necessary for F state of -SIM,    #
#                                                       Input the fixed similarity of LTRs      #
#           -SIM_d=<difference of similarity(%p)>     : It is necessary for D state of -SIM,    #
#                                                       Input the difference between similarity #
#           -PT_f=<fixed length of protein(bp)>       : It is necessary for F state of -PT      #
#                                                       Input the fixed length of protein       #
#           -TOTAL_f=<fixed length of sequence(bp)>   : It is necessary for F state of -TOTAL   #
#                                                       Input the fixed length of sequence      #
#           -h(elp)                                   : print help text                         #
# Input Example : python makeRandomLTRs_mono.py -LTR=R -SIM=D -SIM_d=5 -PT=R -TOTAL=R -num=1000 #
# Output : Genome sequences that have only one pair of LTRs. Protein sequence that is enwrapped #
#          by LTR, it is random sequence that have no meanings                                  #
# Output format : MULTIFASTA file                                                               #
#################################################################################################
'''

def parseArguments(argv) :
	dic = {}
	for arg in argv :
		idx = arg.find('=')
		if idx != -1 :
			dic[arg[:idx]] = arg[idx+1:].upper()
	return dic

def checkArguments(argv, inp_cmd) :
	valid = True
	if argv.has_key('-LTR') == False or argv.has_key('-SIM') == False or argv.has_key('-PT') == False or argv.has_key('-TOTAL') == False or argv.has_key('-num') == False :
		print "Lack of necessary options, please check your command"
		valid = False
	elif argv['-LTR'] == 'F' and argv.has_key('-LTR_f') == False :
	 	print "'-LTR=F' need '-LTR_f' option"
		valid = False
	elif argv['-LTR'] == 'D' and argv.has_key('-LTR_d') == False :
	 	print "'-LTR=D' need '-LTR_d' option"
		valid = False
	elif argv['-SIM'] == 'F' and argv.has_key('-SIM_f') == False :
	 	print "'-SIM=F' need '-SIM_f' option"
		valid = False
	elif argv['-SIM'] == 'D' and argv.has_key('-SIM_d') == False :
	 	print "'-SIM=D' need '-SIM_d' option"
		valid = False
	elif argv['-PT'] == 'F' and argv.has_key('-PT_f') == False :
	 	print "'-PT=F' need '-PT_f' option"
		valid = False
	elif argv['-TOTAL'] == 'F' and argv.has_key('-TOTAL_f') == False :
	 	print "'-TOTAL=F' need '-TOTAL_f' option"
		valid = False
	 	
	if valid == False :
		print "Your command : " + inp_cmd
		exit(2)

def determineLength(argv) :
	# L : length of 'L'TR, P : length of 'P'rotein, T : length of 'T'otal
	# S : 'S'tart position of LTR in sequence
	length = {'L' : 0, 'P' : 0, 'T' : 0, 'S' : 0}

	if argv['-TOTAL'] == 'F' :
		length['T'] = int(argv['-TOTAL_f'])
	elif argv['-TOTAL'] == 'R' :
		length['T'] = random.randint(const.TOTAL_L, const.TOTAL_U)
	else :
		print "Invalid state of '-TOTAL', please input 'F' or 'R'"
		exit(3)

	if argv['-LTR'] == 'F' :
		length['L'] = int(argv['-LTR_f'])
	elif argv['-LTR'] == 'D' :
		length['L'] = const.LTR_L
	elif argv['-LTR'] == 'R' :
		length['L'] = random.randint(const.LTR_L, const.LTR_U)
	else :
		print "Invalid state of '-LTR', please input 'F' or 'D' or 'R'"
		exit(3)

	if argv['-PT'] == 'F' :
		length['P'] = int(argv['-PT_f'])
	elif argv['-PT'] == 'R' :
		length['P'] = random.randint(const.PROTEIN_L, const.PROTEIN_U)
	else :
		print "Invalid state of '-PT', please input 'F' or 'R'"
		exit(3)

	if argv['-LTR'] != 'D' :
		length['S'] = random.randint(0, length['T'] - 2 * length['L'] - length['P'])
	else :
		length['S'] = random.randint(0, length['T'] - 2 * const.LTR_U - length['P'])
	
	return length

def mutateLTR(ltr, sim) :
	mut_num = int(len(ltr) * (1 - sim / 100.0))
	mut_idx = random.sample(range(len(ltr)), mut_num)
	res = ''
	for idx in range(len(ltr)) :
		nucl = ['A', 'G', 'T', 'C']
		if idx in mut_idx :
			del nucl[nucl.index(ltr[idx])]
			res += random.choice(nucl)
		else :
			res += ltr[idx]
	return res

def printLTRs(ltr, mltr) :
	while len(ltr) != 0 :
		one_time = 150
		if len(ltr) < one_time :
			one_time = len(ltr)
		for_print = ''
		for i in range(one_time) :
			for_print += ltr[i]
		print "LTR :\t" + for_print
		for_print = ''
		for i in range(one_time) :
			if ltr[i] == mltr[i] :
				for_print += '.'
			else :
				for_print += 'v'
		print "\t\t" + for_print
		for_print = ''
		for i in range(one_time) :
			for_print += mltr[i]
		print "mLTR :\t" + for_print
		if len(ltr) > one_time :
		 	ltr = ltr[one_time:]
		 	mltr = mltr[one_time:]
		else :
		 	break
		

# Main body of program

if sys.argv[1] == '-h' or sys.argv[1] == '-help' :
	printHelp()
	exit(0)

if len(sys.argv) < 6 :
	print "Too short arguments, please read help [python makeRandomLTRs_mono.py -h]"
	exit(1)
elif len(sys.argv) > 10 :
	print "Too long arguments, please read help [python makeRandomLTRs_mono.py -h]"
	exit(1)

inp_cmd = "python"
for arg in sys.argv :
	inp_cmd += " " + arg
print "inp_cmd : " + inp_cmd

#parsing and checking arguments
argv = parseArguments(sys.argv)
checkArguments(argv, inp_cmd)
argv['-num'] = int(argv['-num'])
print "argv :", argv

dt = str(datetime.datetime.now())[:19].replace(' ', '_').replace(':','')
file_name = 'sampleMonoLTR_' + dt
if argv['-SIM'] == 'F' :
	file_name += '_' + str(argv['-SIM_f'])
out_file = open(file_name + ".fa", 'w')

LTR_loop = 1
LTR_diff = 0
LTR_cnt = 0
if argv['-LTR'] == 'D' :
	LTR_loop = (const.LTR_U - const.LTR_L) / int(argv['-LTR_d'])
	LTR_diff = int(argv['-LTR_d'])
SIM_loop = 1
SIM_diff = 0
SIM_cnt = 0
if argv['-SIM'] == 'D' :
	SIM_loop = (const.SIM_U - const.SIM_L) / int(argv['-SIM_d'])
	SIM_diff = int(argv['-SIM_d'])

sim = 100
nucleotides = ['A', 'G', 'T', 'C']
# make random sequences

for i in range(argv['-num']) :
	print "\n[", i, "]"
	# write header of seqeunce
	out_file.write(">sample_" + str(i) + '\n')
	# determind length of each parts and similarity
	length_v = determineLength(argv)
	if argv['-SIM'] == 'R' :
		sim = random.randint(const.SIM_L, const.SIM_U)
	elif argv['-SIM'] == 'F' :
		sim = int(argv['-SIM_f'])
	elif argv['-SIM'] == 'D' :
		sim = const.SIM_L
	else :
		print "Invalid state of '-SIM', please input 'F' or 'D' or 'R'"
		exit(3)

	# when -LTR or -SIM state is 'D', uniformly increase their value
	if i % LTR_loop == 0 :
		length_v['L'] += LTR_diff * LTR_cnt
		LTR_cnt += 1
	print "len(LTR) :", length_v['L']

	if i % SIM_loop == 0 :
		sim += SIM_diff * SIM_cnt
		SIM_cnt += 1
	print "SIM :", sim

	print "LTR start :", length_v['S'] + 1
	print "LTR end :", length_v['S'] + length_v['L'] + 1
	print "mutated LTR start :", length_v['S'] + length_v['L'] + length_v['P'] + 1
	print "mutated LTR end :", length_v['S'] + 2 * length_v['L'] + length_v['P'] + 1
	sequence = ''
	# make random sequence 0 to start position of LTR
	for j in range(length_v['S']) :
		sequence += random.choice(nucleotides)
	ltr = ''
	# make LTR sequence which length is length_v['L']
	for j in range(length_v['L']) :
		ltr += random.choice(nucleotides)
	sequence += ltr
#	print "LTR :", ltr
	# make random Protein sequence which length is length_v['P']
	for j in range(length_v['P']) :
		sequence += random.choice(nucleotides)
	# mutate LTR and add in sequence
	mltr = mutateLTR(ltr, sim)
	sequence += mltr
#	print "mutated LTR :", ltr
	printLTRs(ltr, mltr)
	# make random sequence
	for j in range(length_v['T'] - length_v['S'] - 2*length_v['L'] - length_v['P']) :
		sequence += random.choice(nucleotides)
	# write sequence to file
	while len(sequence) > 100 :
		out_file.write(sequence[:100] + '\n')
		sequence = sequence[100:]
	if len(sequence) != 0 :
		out_file.write(sequence + '\n')
	else :
		out_file.write('\n')

out_file.close()
