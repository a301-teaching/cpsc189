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

def write_moby(counter,sample,dirname):
    level1,level2,level3,level4=dirname.split('/')
    dir1= level1
    dir2= dir1 + '/' + level2
    dir3= dir2 + '/' + level3
    #
    # loop through the four directories in
    # [dir1,dir2,dir3,dirname] and
    # write a new chapter of moby dict in each folder
    #
    for the_dir in [dir1,dir2,dir3,dirname]:
        level=find_level(the_dir)
        for filenum in range(level):
            full_path='{}/moby_para{:03d}.txt'.format(the_dir,filenum)
            if os.path.exists(full_path):
                continue
            print "writing: ",full_path
            with open(full_path,'w') as f:
                f.write(sample[counter])
            counter+=1
    return counter

if __name__=="__main__":
    try:
        shutil.rmtree('folder_l1_0')
    except:
        pass
    
    with open('moby.txt','r') as f:
        sample=f.read()
    paras=sample.split('\n\n')

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

    counter=0
    for dirname in dir_list:
        counter=write_moby(counter,paras,dirname)
       

    

    
        
