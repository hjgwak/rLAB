cnt = 0
passed = 0
failed = 0

while cnt < 10 :
	inp = raw_input("Enter result (1 = pass, 2 = fail) : ")

	if inp == '1' :
		passed += 1
	elif inp == '2' :
		failed += 1

	cnt += 1

print "Passed= " + str(passed)
print "Failed= " + str(failed)
