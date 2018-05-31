#!/usr/bin/env python3

import sys

#print(sys.argv)
#print (type(sys.argv))
#exit()

ip_file = sys.argv[1]
op_file = sys.argv[2]


fout = open(op_file, "w")
f1 = open(ip_file, "r")
f1_lines = f1.readlines()
for line in f1_lines:
  stp = line.strip("\n")
  words = stp.split(",")
  print(words[0], words[-1], file=fout)

