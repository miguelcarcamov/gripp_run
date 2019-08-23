#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:18:54 2019

@author: miguel
"""
import sys
from DIRAC.Core.Base import Script
Script.parseCommandLine()

from DIRAC.Core.Security.ProxyInfo import getProxyInfo
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.Interfaces.API.Job import Job
j = Job(stdout='StdOut', stderr='StdErr')

M = int(sys.argv[1])
N = int(sys.argv[2])
expmnt = sys.argv[3] #dataset_normal or dataset_midfreq
nprocs = int(sys.argv[4])
chunks = int(sys.argv[5])
total_pixels = M*N

lfn = 'LFN:/skatelescope.eu/user/m/miguel.carcamo/'
lfn_output = lfn + 'second/results_experiment_'+str(expmnt)

parts = 17
inputdata_list = []

for i in range(parts):
	if i<10:
		inputdata_list.append(lfn + 'second/HPC_data.tar.gz.0'+str(i))
	else:
		inputdata_list.append(lfn + 'second/HPC_data.tar.gz.'+str(i))
SitesList = ['LCG.UKI-NORTHGRID-MAN-HEP.uk', 'LCG.UKI-LT2-IC-HEP.uk', 'LCG.UKI-LT2-QMUL.uk', 'LCG.UKI-NORTHGRID-LANCS-HEP.uk']
SEList = ['UKI-NORTHGRID-MAN-HEP-disk', 'UKI-LT2-IC-HEP-disk', 'UKI-LT2-QMUL2-HEP-disk', 'UKI-NORTHGRID-LANCS-HEP-disk']
print("Input data list:\n")
print(inputdata_list)
for i in range(0,total_pixels, chunks):
    id_start = i
    id_end = i + chunks
    dirac = Dirac()
    j.setName('CS Faraday Rotation Measurement Reconstruction - Pixels from '+str(id_start)+' to '+str(id_end-1))
    j.setPlatform('EL7')
    j.setTag( ['8Processors'])
    j.setDestination(SitesList)
    j.setExecutable('RMSynthesis2.sh', arguments=str(nprocs)+' '+str(id_start)+' '+str(id_end)+' '+str(expmnt))
    # Input data
    j.setInputData(inputdata_list)
    j.setInputSandbox(['RMSynthesis2.sh','run2.sh','prmon_1.0.1_x86_64-static-gnu72-opt.tar.gz'])
    # Output data
    j.setOutputSandbox(['StdOut', 'StdErr', 'outputtxt_'+str(id_start)+'_'+str(id_end-1)+'.txt', 'prmon'+str(id_start)+'_'+str(id_end-1)+'.txt'])
    #j.setOutputData([lfn_output+'/LOS_'+str(id_start)+'_to_'+str(id_end-1)+'.npy'], outputSE='UKI-NORTHGRID-MAN-HEP-disk')
    j.setOutputData(['LOS_'+str(id_start)+'_to_'+str(id_end-1)+'.npy'], outputSE=SEList, outputPath='/second/results_experiment_'+str(expmnt))
    try:
        diracUsername = getProxyInfo()['Value']['username']
    except:
        print 'Failed to get DIRAC username. No proxy set up?'
        sys.exit(1)
    j.setJobGroup(diracUsername+'_rmsynthesis_by_'+str(nprocs)+'_'+expmnt)
    jobID = dirac.submitJob(j)
    print 'Submission Result: ',j._toJDL()
    print '\n'
