import random
import time

def randomString(num) :
	alphabet = 'qwertyuiopasdfghjklzxcvbnm'
	string = ''
	for i in range(num) :
		idx = random.randint(0, 25)
		string += alphabet[idx]
	return string

def removeAlphabets(cheese, eat) :
	res = ''
	for i in range(len(cheese)) :
		if cheese[i] == eat :
			res += '_'
		else :
			res += cheese[i]
	return res

def printEaten(eaten) :
	print "Eaten alphabet of cheese :",
	for eat in eaten :
		print eat,
	print

def printStatus(eaten, original, cheese) :
	printEaten(eaten)
	print "Original cheese : " + original
	print "Current cheese status : " + cheese
	print

length_of_cheese = int(raw_input("Input the length of the string : "))
cheese = randomString(length_of_cheese)
original = cheese
print "Generated Cheese is '" + cheese + "'"

remain = ''
for i in range(length_of_cheese) :
	remain += '_'

alphabet = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'
alphabets = alphabet.split()
print "Mouse starts eating!"

eaten = []
for i in range(10) :
	time.sleep(1)
	eat = random.choice(alphabets)
	eaten.append(eat)
	alphabets.remove(eat)

	print "Start eating '" + eat + "'"
	cheese = removeAlphabets(cheese, eat)
	printStatus(eaten, original, cheese)

	if cheese == remain :
		break


if cheese == remain :
	print "Out of cheese!"
else :
	print "Finally remained Cheese Status : " + remain
	printStatus(eaten, original, cheese)
