# -problem3_6.py *- coding: utf-8 -*-

import sys

first=sys.argv[1]
second=sys.argv[2]

infile=open(first)
outfile=open(second, 'w')
  
for lines in infile:
    lines=lines.strip("\n")
    outfile.write(str(len(lines)))
    outfile.write("\n")
  
infile.close()
outfile.close()
  
              
# add your code here