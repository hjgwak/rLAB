numOfNumbers = int(raw_input("Please, Input the number of numbers : "))
nums = raw_input("Input numbers : ")
numbers = nums.split(' ')

tmp = []
maxs = []
idxs = []
i = 0
while i < len(numbers) :
	numbers[i] = int(numbers[i])
	tmp.append(numbers[i])
	maxs.append(numbers[i])
	idxs.append(i)
	i += 1

i = 0
while i < len(numbers) :
	j = i + 1
	while j < len(numbers) :
		tmp[i] = tmp[i] + numbers[j]
		if tmp[i] > maxs[i] :
			maxs[i] = tmp[i]
			idxs[i] = j
		j += 1
	i += 1

ans = max(maxs)
idx = maxs.index(ans)

print "The answer sequence is (" + str(numbers[idx]),
i = idx
while i < idxs[idx] :
	print ", " + str(numbers[i+1]),
	i += 1
print ")"
print "The maximum addtion is " + str(ans)
