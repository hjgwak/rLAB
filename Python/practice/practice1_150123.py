def problemDescription() :
	print "******************************"
	print "Maximum number"
	print "******************************"

def strToInt(numbers) :
	i = 0
	while i < len(numbers) :
		numbers[i] = int(numbers[i])
		i += 1
	return numbers

def findMax(numbers) :
	i = 0
	maximum = -1
	while i < len(numbers) :
		if numbers[i] > maximum :
			maximum = numbers[i]
		i += 1
	return maximum

problemDescription()
inp = raw_input("Input the number : ")
numbers = inp.split(' ')
numbers = strToInt(numbers)
#maxNumber = max(numbers)
maxNumber = findMax(numbers)
print "Maximum number is " + str(maxNumber)
