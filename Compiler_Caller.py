# Denise Irvin
# January 3, 2015

# The idea of this file is that it will be used to compile files 
# and run them multiple times with different inputs.

import subprocess
from subprocess import  Popen, PIPE 
import sys


p = Popen(["g++", "-std=c++14", "-u", "add_two.cpp"], stdin=PIPE, stdout=PIPE, bufsize=1)
#print p.stdout.readline(), # read the first line
for i in range(10): # repeat several times to show that it works
    print >>p.stdin, i # write input
    p.stdin.flush() # not necessary in this case
    print p.stdout.readline(), # read output

#print p.communicate("n\n")[0],
