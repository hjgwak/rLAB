def problemDescription() :
	print "******************************"
	print "1 : upper triangle"
	print "2 : down triangle"
	print "3 : diamond"
	print "4 : diamond 10 times"
	print "q : Quit"
	print "******************************"

def makeString(height, i) :
	string = ''
	for j in range(height - i) :
		string += ' '
	for j in range(2 * i - 1) :
		string += '*'
	return string

def upTri(height) :
	i = 1
	while i <= height :
		string = makeString(height, i)
		i += 1
		print string

def downTri(height) :
	i = height
	while i > 0 :
		string = makeString(height, i)
		i -= 1
		print string

while True :
	problemDescription()
	inp = raw_input("Input : ")
	if inp == 'q' :
		break
	height = int(raw_input("Height : "))
	if inp == '1' :
		upTri(height)
	elif inp == '2' :
		downTri(height)
	elif inp == '3' :
		upTri(height)
		downTri(height-1)
	elif inp == '4' :
		for i in range(10) :
			upTri(height)
			downTri(height-1)
	else :
	  	print "Please Input 1 to 4 or q"
