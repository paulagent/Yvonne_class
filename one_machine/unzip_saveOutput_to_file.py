#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script simply unzip zip file in a recusively way for a input directory and write all the unzipped file to a txt file.
import zipfile,fnmatch,os
import sys
from subprocess import call

rootPath = "/home/derekja/projects/rpp-ycoady/spectral/derekja/OLCI/2016"
#rootPath = sys.argv[1]
pattern = '*.zip'
print(rootPath)
call(["pushd", rootPath], shell=True)
call("pwd")
#create file to save unzip file name and path
file = open("orig2016unzipfilelist_derekja.txt", "a+")  
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
# extractall method's first parameter means dest directory for unzip file 
#zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
#print(zipfile.ZipFile(os.path.join(root, filename)).namelist())
        #for info in zipfile.ZipFile(os.path.join(root, filename)).infolist(): 
        #    print(info.filename)
        try:
                zipfile.ZipFile(os.path.join(root, filename)).extractall(root) 
                filename= zipfile.ZipFile(os.path.join(root, filename)).namelist()
                print(filename[0]) 
                file.write(os.path.join(root,filename[0]))
                file.write("\r\n")
        except:
                print("skipped invalid file: "+filename[0])
file.close       

        
