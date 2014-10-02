# File: os-path-walk-example-2.py
#http://effbot.org/librarybook/os-path/os-path-walk-example-2.py

import os

def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            print(directory,file)
            fullname = os.path.join(directory, file)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files

for file in index("."):
    print file

## .\aifc-example-1.py
## .\anydbm-example-1.py
## .\array-example-1.py
## ...
