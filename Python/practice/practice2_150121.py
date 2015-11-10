dan = int(raw_input("Please input multiplication level : "))

if 2 <= dan <= 9 :
	print "**********" + str(dan) + "**********"
	mul = 1
	while mul < 10 :
		print str(dan) + "*" + str(mul) + "= " + str(dan*mul)
		mul += 1
	print "*********************"

else :
	print "Wrong input"
