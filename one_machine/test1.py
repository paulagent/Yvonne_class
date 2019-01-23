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
os.chdir("/polymer-v4.8")
print("enter polymer dir")
for filename in glob('/spectral/tests/unpack/S3A*.SEN3'):
        print("filename is ", filename)
        run_atm_corr(Level1(filename), Level2(outdir='/spectral/gaobing/outdir1/',  # level2 filename determined from level1 name, if outdir is not provided it will go to the same folder as level1
                        fmt='netcdf4', datasets=default_datasets+['SPM']), calib = {
                400 : 1.0  , 412 : 0.997,
                443 : 0.997, 490 : 0.989,
                510 : 0.993, 560 : 0.998,
                620 : 1.0  , 665 : 1.0,
                674 : 1.0  , 681 : 1.0,
                709 : 1.0  , 754 : 1.0,
                760 : 1.0  , 764 : 1.0,
                767 : 1.0  , 779 : 1.0,
                865 : 1.0  , 885 : 1.0,
                900 : 1.0  , 940 : 1.0,
                1020: 1.0  , 1375: 1.0,
                1610: 1.0  , 2250: 1.0,
                }, multiprocessing=-1 # thres_Rcloud = 0.13
                 )
        toc=time.clock()
        print('Processing time',filename,': (seconds)')
        print(toc-tic)

toc=time.clock()
print('Total processing time: (seconds)')
print(toc-tic)
