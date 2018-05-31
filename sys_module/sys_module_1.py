#!/usr/bin/env python3

#import sys

fout = open("ofile.csv", "w")
f1 = open("ifile.csv", "r")
f1_lines = f1.readlines()
for line in f1_lines:
  stp = line.strip("\n")
  words = stp.split(",")
  print(words[0], words[-1], file=fout)

