import os
#os module contains functions that deal with long file names
def index(directory):
    # like os.listdir, but traverses directory trees
    stack = [directory]
    #list contains the directory which is the input to the function
    files = []
    #this creates an empty list
    sizesoffiles= []
   
    while stack:
        #while stack is empty
        directory = stack.pop()
        #.pop removes and returns the last item in the list
        
        for file in os.listdir(directory):
           #this loops through and prints out the name of the subfiles and directories
            #os.listdir returns a list containing the names of the entries in "directory", by path
            fullname = os.path.join(directory, file)
            #os.path.join joins one of more path components, assigns to fullname
            files.append(fullname)
            #.append adds an item to the end of "fullname"
            sizesoffiles=os.path.getsize(fullname)
            
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
                
                files.append(sizesoffiles)
   
             #os.path.isdir returns true if "fullname is in an existing directory, islink true if "fullname"refers to a 
            #directory entry that is in symbolic list
                return files,sizesoffiles
  
            

for file in index("."):
    #index returns a list of filenames
    print file
