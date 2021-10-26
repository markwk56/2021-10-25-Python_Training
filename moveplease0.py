#!/usr/bin/env python3
# import package to manipulate files
import shutil
# import package to change directories
import os

os.chdir('/home/student/2021-10-25-Python_Training/')



# moves file to new directory
shutil.move('raynor.obj', 'ceph_storage/')
# prompts user for the new name of a file
xname = input('What is the new name for kerrigan.obj? ')
# moves file to a new directory and gives it a new name

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



