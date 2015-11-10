import sys, os

if len(sys.argv) != 2 :
	print "input ltr length!"
	print "cmd : python auto.py [ltr length]"
	exit(0)

cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta100/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res100.out -e=err.err -b=150 -c=2 > log100.out"

os.system(cmd)

cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta95/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res95.out -e=err.err -b=150 -c=2 > log95.out"

os.system(cmd)

cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta90/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res90.out -e=err.err -b=150 -c=2 > log90.out"

os.system(cmd)

cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta85/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res85.out -e=err.err -b=150 -c=2 > log85.out"

os.system(cmd)
cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta80/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res80.out -e=err.err -b=150 -c=2 > log80.out"

os.system(cmd)
cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta75/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res75.out -e=err.err -b=150 -c=2 > log75.out"

os.system(cmd)

cmd = "python ~/Python/save_log.py python ~/Python/MER/findLTR.py -f=/data1/hjgwak/test_data/RepSeek/fasta/each_ltr_length/ltr_" + sys.argv[1] + "/fasta70/ "
cmd += "-l=20 -r=/data1/hjgwak/test_data/MER/res_d0/seed20/ltr_" + sys.argv[1] + "/res70.out -e=err.err -b=150 -c=2 > log70.out"

os.system(cmd)
