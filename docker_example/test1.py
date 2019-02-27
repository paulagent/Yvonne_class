#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import polymer
import os
tic=time.clock()


from subprocess import call

from polymer.main import run_atm_corr, Level1, Level2
from polymer.level2 import default_datasets
from glob import glob
#call(["cd", "/polymer-v4.8"])
#os.chdir("/polymer-v4.8")

for filename in glob('/raw_file/S3A*.SEN3'):
        print("filename is ", filename)
        run_atm_corr(Level1(filename), Level2(outdir='/raw_file/outdir1/',  # level2 filename determined from level1 name, if outdir is not provided it will go to the same folder as level1
                        fmt='netcdf4', datasets=default_datasets+['SPM']), multiprocessing=0 # thres_Rcloud = 0.13
                 )
        toc=time.clock()
        print('Processing time',filename,': (seconds)')
        print(toc-tic)

toc=time.clock()
print('Total processing time: (seconds)')
print(toc-tic)
