# File: os-path-walk-example-2.py
#http://effbot.org/librarybook/os-path/os-path-walk-example-2.py
#http://stackoverflow.com/questions/1830618/how-to-find-the-owner-of-a-file-or-directory-in-python

import os
import stat
from collections import defaultdict
try:
    from pwd import getpwuid
    has_pwd=True
except ImportError:
    has_pwd=False

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
        #directory=os.path.abspath(directory)
        for the_file in os.listdir(directory):
            fullname = os.path.join(directory, the_file)
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
                if has_pwd:
                    owner=getpwuid(st[stat.ST_UID]).pw_name
                else:
                    owner='NA'
                modified=st[stat.ST_MTIME]
                files.append((fullname,owner,size,modified))
    return files

if __name__=="__main__":
    #
    # get the file list and the dictionary of files
    #
    files=index('.')
    print files
    

## .\aifc-example-1.py
## .\anydbm-example-1.py
## .\array-example-1.py
## ...
