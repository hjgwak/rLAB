def printMTable(num) :
	print "***" + str(num) + "***"
	for i in range(1, 10) :
		print str(num) + "*" + str(i) + "= " + str(num*i)

for i in range(2, 10) :
	printMTable(i)
	print
