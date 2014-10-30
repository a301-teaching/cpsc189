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

Assignment 1 solution:
++++++++++++++++++++++

See the script `lib/walk.py <https://github.com/a301-teaching/cpsc189/blob/master/lib/walk.py>`_

   
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

   a) lib/atsc212.py that contains your tree_walker() and
      tree_to_csv() to csv functions

   b) a new notebook notebooks/tree_demo.ipynb  that uses these two functions to
      walk a directory tree and prints the resulting DataFrame


Assignment 3 solution
+++++++++++++++++++++

See the `tree_demo.ipynb notebook <http://nbviewer.ipython.org/github/a301-teaching/cpsc189/blob/master/notebooks/tree_demo.ipynb>`_ that
calls `lib/new_walk.py <lib/new_walk.py>`_

Assignment 4:
_____________

Read this `testing tutorial <http://www.jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing>`_

Use the new script `lib/build_tree.py  <https://github.com/a301-teaching/cpsc189/blob/6119c915c91368e9dc34e86e85daf72a21f96daf/lib/build_tree.py>`_
to create a 4-level set of folders and
fill them with paragraphs from Moby Dick.  I've written most of what's needed
but removed the lines from the function write_moby that actually handle the
file writing::

  def write_moby(counter,sample,dirname):
    level1,level2,level3,level4=dirname.split('/')
    dir1= level1
    dir2= dir1 + '/' + level2
    dir3= dir2 + '/' + level3
    for the_dir in [dir1,dir2,dir3,dirname]:
        level=find_level(the_dir)
    #
    # loop through the four directories in
    # [dir1,dir2,dir3,dirname] and
    # write a new paragraph of moby dict in each folder by
    # opening and writing 1 file the level1 folder, 2 files in
    # each of the level 2 folders, 3 files in level3 folders
    # and 4 files in level4.  Use the counter variable to
    # make sure that each file gets a different paragraph of moby dick
    #

    return counter

Once you've got a working version check it in and we'll write tests of your
tree_walker.py using this folder tree.

