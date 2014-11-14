"""


"""


from __future__ import print_function
import os,site
import pandas as pd
import new_walk
reload(new_walk)

def tree_to_csv(filename,filelist):
    with open(filename,'w') as f:
        #write the header first
        f.write('file_name;owner;size;modified;level\n')
        for the_line in filelist:
            f.write("{:s};{:s};{:d};{:d};{:d}\n".format(*the_line))

#
# break the foldername up into seperate directories so
# they can be sorted in order using folder_sort as a key function
#
def folder_sort(foldername):
    #python knows how to sort lists and tuples alphabetically
    #for any number of items
    return foldername.split(os.sep)

if __name__=="__main__":
    target='folder_l1_0'
    if not os.path.exists('folder_l1_0'):
        raise IOError('need folder {} produced by build_tree_sol.py'.format(target))
    files=new_walk.index('folder_l1_0')
    #
    # append the level to each item in the list
    #
    new_list=[]
    for the_file in files:
        the_level=len(the_file[0].split(os.sep)) - 1
        new_list.append(the_file + (the_level,))

#
# don't really need to write and then read a csv file to create
# dataframe, use the from_records method
#            
    #tree_to_csv('out.csv',new_list)
    #df=pd.read_csv('out.csv',sep=';')

    headers='file_name;owner;size;modified;level'.split(';')
    df=pd.DataFrame.from_records(new_list,columns=headers)
    out=df.groupby('level')

    indent='   '
    for level,item in out:
        the_indent=indent*(level - 1)
        level_size=item['size'].sum()
        file_dict={}
        for idx,out in item.iterrows():
            dirname,filename=os.path.split(out['file_name'])
            #
            # could also use collections.defaultdict(list) here to get
            # empty list as default value for new key, then the if
            # statement could be replaced by the single line
            #
            #  file_dict[dirname].append(filename)
            #
            #
            if dirname not in file_dict:
                file_dict[dirname]=[filename]
            else:
                file_dict[dirname].append(filename)
        if level==1:
            print("level 1 directory is {} with {} bytes".format(dirname,level_size))
        else:
            folder_names=file_dict.keys()
            folder_names.sort(key=folder_sort)
            print("{:s}level {:d} directories: {:d} bytes".format(the_indent,level,level_size))
            for the_folder in folder_names:
                files=file_dict[the_folder]
                folder_indent=the_indent + indent
                print("{}{}".format(folder_indent,the_folder))
                for the_file in files:
                    file_indent=folder_indent + indent
                    print("{}{}".format(file_indent,the_file))

