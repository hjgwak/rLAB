import time

def problemDescription() :
	print "******************************"
	print "Reverse guess the number"
	print "******************************"

def comGuess(start, end) :
	return (start + end) / 2

problemDescription()
	
userNumber = int(raw_input("userNumber : "))
interval = int(raw_input("interval : "))
start = 1
end = 100
guessesTaken = 0

while True :
	Guess = comGuess(start, end)
	guessesTaken += 1
	
	time.sleep(interval)
	print "Computer's guess is " + str(Guess)
	
	if Guess < userNumber :
		print "Computer! your guess is too small!"
		start = Guess
	elif Guess > userNumber :
		print "Computer! your guess is too big!"
		end = Guess
	else :
		print "Congraturation! you get the answer in " + str(guessesTaken) + " times"
		print "The answer is " + str(userNumber)
		break
