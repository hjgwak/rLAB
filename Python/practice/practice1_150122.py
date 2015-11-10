def problemDescription() :
	print "******************************"
	print "Number of Common divisors"
	print "******************************"

def commonDivisors(num1, num2) :
	print "Common divisors : ",
	div = 1
	cut = num1
	cnt = 0 
	greatest = 0
	while True :
		if num1 % div == 0 and num2 % div == 0 :
			print str(div) + ", ",
			cnt += 1
			greatest = div
		if num1 == div or num2 == div :
			break
		div += 1
	print "\b\b"
	print "Number of common divisors of two number is " + str(cnt)
	print "Greatest common divisors of two number is " + str(greatest)
	return cnt

problemDescription()
num1 = int(raw_input("Input the first number : "))
num2 = int(raw_input("Input the second number : "))
res = commonDivisors(num1, num2)
