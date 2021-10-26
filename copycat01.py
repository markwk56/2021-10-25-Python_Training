#!/usr/bin/env python3
# this code creats a new folder and backs up the files to a backup foilder

# import packages to use the proper methoids
import shutil

import os

# changes directories to the proper directory

os.chdir('/home/student/2021-10-25-Python_Training/')

# copies the file to a backup file

shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

#copies the foler to a backup folder

shutil.copytree('5g_research/', '5g_research_backup/')


