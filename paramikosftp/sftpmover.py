#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

machine = input("enter machine IP: ")
user = input("enter the username: ")
passw = input("enter the password: ")


## where to connect to
# t = paramiko.Transport("10.10.2.3", 22) ## IP and port
t = paramiko.Transport(machine, 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
# t.connect(username="bender", password="alta3")
t.connect(username=user, password=passw)

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
for x in os.listdir("/home/student/2021-10-25-Python_Training/filestocopy/"): # iterate on directory contents
  if not os.path.isdir("/home/student/2021-10-25-Python_Training/filestocopy/"+x): # filter everything that is NOT a directory
    sftp.put("/home/student/2021-10-25-Python_Training/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
sftp.close() # close the connection

