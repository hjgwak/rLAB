#!/usr/bin/env python

import sys

def comp(a, b) :
	first = int(a.split('\t')[3])
	second = int(b.split('\t')[3])
	return first - second

if len(sys.argv) < 3 :
	print "python sortGFF.py [GFF file] [out file]"
	exit()

_gff = open(sys.argv[1], "r")
_gff.readline()
lines = _gff.readlines()
_gff.close()

lines.sort(comp)

_out = open(sys.argv[2], "w")
print >>_out, "##gff-version 3"
for line in lines :
	print >>_out, line[:-1]
_out.close()
