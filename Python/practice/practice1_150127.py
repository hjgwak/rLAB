def problemDescription() :
	print "*************"
	print "1.Calculate"
	print "2.Show it!"
	print "3.Initialize"
	print "4.Quit"
	print "*************"

def calcFibo(num) :
	fibo = [0, 1]
	for i in range(2, num+1) :
		fibo.append(fibo[i-2] + fibo[i-1])
	return fibo


inp = '0'
fibo = [0, 1]
while inp != '4' :
	problemDescription()
	inp = raw_input("Input : ")

	if inp == '1' :
		num = int(raw_input("Input the number : "))
		fibo = calcFibo(num)
	elif inp == '2' :
		for i in range(len(fibo)) :
			print fibo[i],
		print
	elif inp == '3' :
		fibo = [0, 1]
	elif inp == '4' :
		break
	else :
		print "Please, Input the number between 1 to 4"
