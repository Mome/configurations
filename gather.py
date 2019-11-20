#! /bin/python

import distutils
import os
import warnings

def copy_files(src, dst):
    if os.isdir(src):
        distutils.dir_utils.copy_tree(src, dst)
    else:
        distutils.file_utils.copy_file(src, dst)

def name_filter(fn):
    if '#' in fn:
        i = fn.index('#')
        fn = fn[:i+1]
    fn = fn.strip()
    return fn

with open('file_list') as f:
    filenames = f.readlines()

for fname in map(name_filter, filenames):
    fname = ...
    dst = os.path.join('./files', fname)
    copy_files()





# setup files folder 
rm -rf files
mkdir files
cd files

cp ~/.config/openbox/rc.xml .

mkdir usr_local_bin
cp /usr/local/bin/* usr_local_bin

cp ~/.shrc .
