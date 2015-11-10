import sys, os

if '-h' in sys.argv or '-help' in sys.argv or len(sys.argv) < 3 :
	print "\npython SRA_download.py [sra program] [Accession list]\n"
	exit()

program = sys.argv[1]
accessions = sys.argv[2:]
for accession in accessions :
	os.system("/home/hjgwak/program/sratoolkit.2.5.2-ubuntu64/bin/" + program + " " + accession)
