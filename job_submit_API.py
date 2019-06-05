#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:18:54 2019

@author: miguel
"""

from DIRAC.Core.Base import Script
Script.parseCommandLine()

from DIRAC.Core.Security.ProxyInfo import getProxyInfo
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.Interfaces.API.Job import Job
j = Job(stdout='StdOut', stderr='StdErr')

M = sys.argv[1]
N = sys.argv[2]
expmnt = sys.argv[3] #dataset_normal or dataset_midfreq
total_pixels = M*N

lfn = 'LFN:/skatelescope.eu/user/m/miguel.carcamo/'
lfn_output = lfn + 'second/results_experiment_'+str(expmnt)
for i in range(total_pixels)
    dirac = Dirac()
    j.setName('CS Faraday Rotation Measurement Reconstruction - Pixel '+str(i))
    j.setPlatform('EL7')
    j.setTag( ['1Processors'])
    j.setDestination('LCG.UKI-NORTHGRID-MAN-HEP.uk')
    j.setExecutable('RMSynthesis2.sh', arguments=str(i)+' '+str(expmnt))
    # Input data
    j.setInputData([lfn + 'second/HPC_data.tar.gz'])
    j.setInputSandbox(['RMSynthesis2.sh','run2.sh','prmon_1.0.1_x86_64-static-gnu72-opt.tar.gz'])
    # Output data
    j.setOutputSandbox(['StdOut', 'StdErr', 'outputtxt'+str(i)+'.txt', 'prmon'+str(i)+'.txt'])
    j.setOutputData([lfn_output + '/output_test_'+str(i)+'.npy'], outputSE='UKI-NORTHGRID-MAN-HEP-disk')
    try:
        diracUsername = getProxyInfo()['Value']['username']
    except:
        print 'Failed to get DIRAC username. No proxy set up?'
        sys.exit(1)
    j.setJobGroup(diracUsername+'rmsynthesis_byone')
    jobID = dirac.submitJob(j)
    print 'Submission Result: ',jobID
