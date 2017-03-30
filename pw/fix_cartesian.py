#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 3:
  print("usage:\tfix_md.py inputfile outputfile")
  sys.exit()
else:
  inf  = sys.argv[1]
  outf = sys.argv[2]
  infile = open(inf,'r').readlines()

  counter = 0
  passed  = 0
  replaced_lines = []

  for i in range(len(infile)):
    s = infile[i]
    if 'Cartesian axes' in s:
      if 'Forces' in s:
        newline = s.replace('Cartesian','cartesian')
        infile[i] = newline
        counter += 1
        replaced_lines.append(i)
      else:
        passed += 1

if outf in os.listdir('.'):
  print("{}/{} exists.  Please choose a new filename and try again.\nExiting now.".format(os.getcwd(), outf))
  sys.exit()
else:
  outfile = open(outf, 'w')
  for line in infile:
    outfile.write(line)
  outfile.close()

print("JOB DONE!\nnew outfile:\t{}/{}\nlines replced:\t\t\t{}\nlines preserved:\t\t{}\n\n... bye.\n".format(os.getcwd(), outf, counter, passed))

