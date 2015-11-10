#!/usr/bin/env python

import sys, glob

if len(sys.argv) < 3 :
	print "python convGFF.py [fasta directory] [gff file]"
	exit(0)

fa_dir = glob.glob(sys.argv[1] + "*")

dic = {}
for fa in fa_dir :
	fasta = open(fa, "r")
	fasta_line = fasta.readline()
	dic[fa.split('/')[-1]] = fasta_line.split(' ')[-5]
	fasta.close()

gff = open(sys.argv[2], "r")
out = open("out.gff", "w")

gff_line = gff.readline()
print >>out, gff_line[:-1]
gff_line = gff.readline()
while gff_line :
	split = gff_line.split('\t')
	split[0] = dic[split[0]]
	res = '\t'.join(split)
	print >>out, res[:-1]
	gff_line = gff.readline()
gff.close()
out.close()
