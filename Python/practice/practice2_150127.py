#-*-encoding:utf-8-*-

def problemDescription() :
	print "***** Ramen shop *****"
	print "1.Input sales"
	print "2.Change sales"
	print "3.Check sales"
	print "4.Quit"
	print "**********************"

def printMenu() :
	print "0.Ramen"
	print "1.Cheese ramen"
	print "2.Rice cake ramen"
	print "3.Fried ramen"
	print "4.Nagasaki ramen"

def inputSales(sales) :
	printMenu()
	kind = int(raw_input("What kind of ramen is sold? "))
	many = int(raw_input("How many ramen is sold? "))
	sales[kind] += many
	return sales

def changeSales(sales) :
	printMenu()
	kind = int(raw_input("What kind of ramen you want to change sales? "))
	many = int(raw_input("Input the sales for change : "))
	sales[kind] = many
	return sales

def printSales(prices, sales) :
	names = ["Ramen", "Cheese ramen", "Rice cake ramen", "Fried ramen", "Nagasaki ramen"]
	total = 0
	print "***** Sales *****"
	for i in range(len(names)) :
		print str(i) + "." + names[i]
		print "Price : " + str(prices[i])
		print str(sales[i]) + " " + names[i] + "s was sold, sales : " + str(prices[i]*sales[i])
		total += prices[i]*sales[i]
	print "\ntotal sales : " + str(total)

prices = [0, 0, 0, 0, 0]
sales = [0, 0, 0, 0, 0]
print "***** Ramen shop *****"
print "Setting price."
prices[0] = int(raw_input("Price of ramen : "))
prices[1] = int(raw_input("Price of cheese ramen : "))
prices[2] = int(raw_input("Price of rice cake ramen : "))
prices[3] = int(raw_input("Price of fried ramen : "))
prices[4] = int(raw_input("Price of Nagasaki ramen : "))

inp = '0'
while inp != '4' :
	problemDescription()
	inp = raw_input("Input : ")

	if inp == '1' :
		sales = inputSales(sales)
	elif inp == '2' :
		sales = changeSales(sales)
	elif inp == '3' :
		printSales(prices, sales)
	elif inp == '4' :
		break
	else :
		print "Please, Input the number between 1 to 4"
