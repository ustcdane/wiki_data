#!/usr/bin/env python 
#-*- coding:utf-8 -*-
import sys
import os
import glob # set glob module

#read dir 读取指定文件夹下满足要求的文件
def read_dir(dir_name):
    file_list=glob.glob(dir_name)
    dm={}
    for file in file_list:
        if os.path.isfile(file): 
            date=file.split('-')[1]# get date
            with open(file) as f:
                for line in f:
                    sl=line.split()#split 
                    if date in dm:
                        if sl[0] in dm[date]:
                            dm[date][sl[0]]=dm[date][sl[0]]+int(sl[2])
                        else:
                            dm[date][sl[0]]=int(sl[2])
                    else:
                        items={}
                        items[sl[0]]=int(sl[2])
                        dm[date]=items
    return dm
if __name__=='__main__':
    #main
    d=r'./projectcounts-201401*'
    dm=read_dir(d)
    for k,v in dm['20140112'].iteritems():
        print k,v
