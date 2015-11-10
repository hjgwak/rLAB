import sys, os

if len(sys.argv) != 4 :
	print "python result_compare_multi.py [ref directory] [res directory] -buf=#"
	exit()

os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref100.out " + sys.argv[2] + "res100.out " + sys.argv[3] + " > stats100.out");
os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref95.out " + sys.argv[2] + "res95.out " + sys.argv[3] + " > stats95.out");
os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref90.out " + sys.argv[2] + "res90.out " + sys.argv[3] + " > stats90.out");
os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref85.out " + sys.argv[2] + "res85.out " + sys.argv[3] + " > stats85.out");
os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref80.out " + sys.argv[2] + "res80.out " + sys.argv[3] + " > stats80.out");
os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref75.out " + sys.argv[2] + "res75.out " + sys.argv[3] + " > stats75.out");
os.system("python ~/Python/RepSeek/result_compare.py " + sys.argv[1] + "ref70.out " + sys.argv[2] + "res70.out " + sys.argv[3] + " > stats70.out");
