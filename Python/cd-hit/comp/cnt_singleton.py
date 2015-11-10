import sys

if len(sys.argv) != 2 or sys.argv[1] == '-h' :
	print "python cnt_singleton.py [cd-hit cluster]"

cdhit = open(sys.argv[1], 'r')

cnt = 0
flag = False
S = 0
M = 0

total_S = 0
total_M = 0

for line in cdhit.readlines() :
	line = line.rstrip('\r\n')
	if line[0] == '>' :
		if flag :
			if cnt == 1 :
				if S == 1 and M == 0 :
					total_S += 1
				elif S == 0 and M == 1 :
					total_M += 1
				else :
					print "strange cluster!"
					exit()
		flag = True
		S = 0
		M = 0
		cnt = 0
	else :
		cnt += 1
		ch = line.split(' ')[1][:-3][-1] 
		if ch == 'S' :
			S += 1
		elif ch == 'M' :
			M += 1
		else :
			print "strange input!"
			exit()
if cnt == 1 :
	if S == 1 and M == 0 :
		total_S += 1
	elif S == 0 and M == 1 :
		total_M += 1
	else :
		print "strange!"
		exit()

print "Singleton : " + str(total_S)
print "Multiple : " + str(total_M)

cdhit.close()
