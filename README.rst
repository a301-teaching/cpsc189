cpsc189
=======

Course text:  http://www.cs.ubc.ca/~pcarter/cs189/


Assignment 1:
_____________

1) check in a  notebook on a branch called "assign1" that
   uses http://effbot.org/librarybook/os-path/os-path-walk-example-2.py
   described at http://effbot.org/librarybook/os-path.htm to walk a folder
   tree with at least 3 levels printing out all the filenames.  Add comments
   to the function that explain as clearly as possible what each part of the
   code is doing, using a specific example if that helps

2) Modfiy your function so that it also returns the size of each file, and the
   total size of all files in the directory.  Verify that the total size
   agrees with  windows explorer
     
Assignment 2:
_____________

Do the 5 input/output exercises in `Pine Chapter 4 <http://clouds.eos.ubc.ca/~phil/djpine_python/Book/_build/html/chap4/chap4_io.html>`_

Assignment 3:
_____________

For this week,  can you:

1)  translate http://synesthesiam.com/posts/an-introduction-to-pandas.html  into a notebook and run it on the data he provides

2) write out a csv file for you directory tree walker that has four columns:

   full file name (i.e. C:\....);owner;size;date last modified (unix timestamp)

3) read that csv file into a pandas data frame

   Check in a new branch that has the following files:

     1) lib/atsc212.py that contains your tree_walker() and
        tree_to_csv() to csv functions

     2) a new notebook notebooks/tree_demo.ipynb  that uses these two functions to
        walk a directory tree and prints the resulting DataFrame
