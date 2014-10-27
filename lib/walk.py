# File: os-path-walk-example-2.py
#http://effbot.org/librarybook/os-path/os-path-walk-example-2.py

import os
import stat
from collections import defaultdict

#make a dictionary for which every entry is intialized to
#an empty list -- use this to sort files and sizes by directory

def index(directory):
    # like os.listdir, but traverses directory trees
    #
    # initialize dir_dict as a dictionary that starts each entry
    # with an empty list
    #
    dir_dict=defaultdict(list)
    #
    # start at the top directory
    #
    stack = [directory]
    files = []
    #
    # this loop exits when all directories are poped
    #
    while stack:
        directory = stack.pop()
        #
        # directory name may be relative to current directory, make it absolute
        #
        directory=os.path.abspath(directory)
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            #
            # if it is a directory, append to stack so loop will reach it
            #
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
            else:  #it's a file
                #
                # retrieve thefile size and append to the list and the
                # directory dict as tuples
                #
                st=os.stat(fullname)
                size=st[stat.ST_SIZE]
                files.append((fullname,size,directory))
                dir_dict[directory].append((fullname,size))
    return files,dir_dict



if __name__=="__main__":
    #
    # get the file list and the dictionary of files
    #
    files,dir_dict=index('.')
    totsize=0
    for dirname,filelist in dir_dict.items():
        for the_file in filelist:
            totsize+=the_file[1]
    print('found total size of: {:d} bytes'.format(totsize))
    

## .\aifc-example-1.py
## .\anydbm-example-1.py
## .\array-example-1.py
## ...
