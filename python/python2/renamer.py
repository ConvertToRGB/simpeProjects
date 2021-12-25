#!python2

import os
import sys

# get list of all files that was dropped on the script excluding script file
arg = sys.argv[1:]

# default
padding = 3

# input new file name
print 'Enter name'
newName = raw_input('name: ')
print "Enter custom padding (must be integer), by default padding = 3:"
inputPadding = raw_input('padding: ')
if inputPadding.isdigit():
    padding = int(inputPadding)

if newName:
    for i, f in enumerate(arg):
        d = os.path.dirname(f)  # get directory full path
        name, ext = os.path.splitext(os.path.basename(f))  # get file name and extension
        fName  = newName + '_' + str(i+1).zfill(padding) + ext  # create new file name
        fullPath = os.path.join(d, fName)  # create new full path with new names
        
        os.rename(f, fullPath)

raw_input()