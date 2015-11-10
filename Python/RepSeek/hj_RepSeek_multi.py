import sys, os

if len(sys.argv) != 5 :
	print "python ~/Python/RepSeek/hj_RepSeek_multi.py -fasta=[dir] -l=# -out=[dir] -cut=#"
	exit()

os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta100/ -name=res100.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log100.out")
os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta95/ -name=res95.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log95.out")
os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta90/ -name=res90.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log90.out")
os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta85/ -name=res85.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log85.out")
os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta80/ -name=res80.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log80.out")
os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta75/ -name=res75.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log75.out")
os.system("python ~/Python/save_log.py python ~/Python/RepSeek/RepSeek_multi.py " + sys.argv[1] + "fasta70/ -name=res70.out " + sys.argv[2] + " " + sys.argv[3] + " " + sys.argv[4] + " > log70.out")
