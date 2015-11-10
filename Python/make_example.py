test_cnt = 1
genome_name = "test_genome"
line_cnt = 200
genome_cnt = 20

output_file = open('test.fa', 'w')
for i in range(genome_cnt) :
	output_file.write('>' + genome_name + '_' + str(test_cnt) + '\n')
	for j in range(line_cnt) :
		output_file.write("AGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTC\n")
	line_cnt -= 10
	test_cnt += 1
output_file.close()
