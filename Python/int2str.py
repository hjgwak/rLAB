def int2str(num, skel) :
	num = int(num)
	skel = str(skel)
	res = []
	
	for i in range(len(skel)) :
		res.append('0')
	idx = 1
	while num > 0 :
	 	res[-idx] = str(num % 10)
	 	num /= 10
	 	idx += 1
	return ''.join(res)

print int2str(10, '1000')
