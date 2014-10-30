import os
import shutil

def find_level(directory):
    """
       
    """
    front,back=os.path.split(directory)
    folder,level,dirnum=back.split('_')
    junk,levelnum=level.split('l')
    levelnum=int(levelnum)
    return levelnum

def write_moby(counter,paras,dirname):
    level1,level2,level3,level4=dirname.split('/')
    dir1= level1
    dir2= dir1 + '/' + level2
    dir3= dir2 + '/' + level3
    for the_dir in [dir1,dir2,dir3,dirname]:
        level=find_level(the_dir)
    #
    # loop through the four directories in
    # [dir1,dir2,dir3,dirname] and
    # write a new chapter of moby dict in each folder by
    # opening and writing 1 file the level1 folder, 2 files in
    # each of the level 2 folders, 3 files in level3 folders
    # and 4 files in level4.  Use the counter variable to
    # make sure that each file gets a different paragraph of moby dick
    #

    return counter

if __name__=="__main__":
    #
    # clean up old folders and start fresh
    #
    try:
        shutil.rmtree('folder_l1_0')
    except:
        pass

    #
    # read in all the chapter so moby dick and split into a list
    #    
    with open('moby.txt','r') as f:
        sample=f.read()
    paras=sample.split('\n\n')

    #
    # create 4 levels of folders if they don't exists
    #
    dir_list=[]
    for level_one in range(1):
        for level_two in range(2):
            for level_three in range(3):
                for level_four in range(4):
                    name_vals=(level_one,level_two,level_three,level_four)
                    path="folder_l1_{}/folder_l2_{}/folder_l3_{}/folder_l4_{}".format(*name_vals)
                    dir_list.append(path)
                    if not os.path.exists(path):
                        os.makedirs(path)

    #
    # write the files in the directories in dir_list
    #
    counter=0
    for dirname in dir_list:
       counter=write_moby(counter,paras,dirname)
       

    

    
        
