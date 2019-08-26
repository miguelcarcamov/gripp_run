#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:18:54 2019

@author: miguel
"""
import sys
import os
from DIRAC.Core.Base import Script
Script.parseCommandLine()

from DIRAC.Core.Security.ProxyInfo import getProxyInfo
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.Interfaces.API.Job import Job

M = int(sys.argv[1])
N = int(sys.argv[2])
expmnt = sys.argv[3] #dataset_normal or dataset_midfreq
chunks = int(sys.argv[4])
total_pixels = M*N

lfn = 'LFN:/skatelescope.eu/user/m/miguel.carcamo/'
lfn_output = lfn + 'second/results_experiment_'+str(expmnt)

for i in range(0,total_pixels, chunks):
	id_start = i
	id_end = i + chunks
	lfn_output_file = lfn_output+'/'+'LOS_'+str(id_start)+'_to_'+str(id_end-1)+'.npy'
        print 'Deleted file: ' + lfn_output_file
	os.system('dirac-dms-remove-files '+lfn_output_file)    
