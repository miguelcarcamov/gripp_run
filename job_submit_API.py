#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:18:54 2019

@author: miguel
"""
import sys
import os
import subprocess
import time
from DIRAC.Core.Base import Script
Script.parseCommandLine()

from DIRAC.Core.Security.ProxyInfo import getProxyInfo
from DIRAC.Interfaces.API.Dirac import Dirac
from DIRAC.Interfaces.API.Job import Job
j = Job(stdout='StdOut', stderr='StdErr')

timestamp = time.strftime('.%Y%m%d%H%M%S') 
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
#SitesList = ['LCG.UKI-NORTHGRID-MAN-HEP.uk', 'LCG.UKI-LT2-IC-HEP.uk', 'LCG.UKI-LT2-QMUL.uk', 'LCG.UKI-NORTHGRID-LANCS-HEP.uk']
#SEList = ['UKI-NORTHGRID-MAN-HEP-disk', 'UKI-LT2-IC-HEP-disk', 'UKI-LT2-QMUL2-disk', 'UKI-NORTHGRID-LANCS-HEP-disk']
inputdatastr='"LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.00", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.01", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.02", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.03", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.04", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.05", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.06", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.07", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.08", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.09", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.10", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.11", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.12", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.13", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.14", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.15", "LFN:/skatelescope.eu/user/m/miguel.carcamo/second/HPC_data.tar.gz.16"'
SitesList = ['LCG.UKI-NORTHGRID-MAN-HEP.uk']
SEList = ['UKI-NORTHGRID-MAN-HEP-disk']
print("Input data list:\n")
print(inputdata_list)
for i in range(0,total_pixels, chunks):
    id_start = i
    id_end = i + chunks
    dirac = Dirac()
    jdl = ''
    jdl += 'JobName = "CS Faraday Rotation Measurement Reconstruction - Pixels from ' + str(id_start)+' to '+str(id_end-1)+'";\n'
    jdl += 'Platform = "EL7";\n'
    jdl += 'Tags = "'+ str(nprocs)+'Processors'+'";\n'
    jdl += 'Site = "LCG.UKI-NORTHGRID-MAN-HEP.uk";\n'
    jdl += 'Executable = "RMSynthesis2.sh";\n'
    jdl += 'Arguments = "'+str(nprocs)+' '+str(id_start)+' '+str(id_end)+' '+str(expmnt)+' %j'+' LOS_'+str(id_start)+'_to_'+str(id_end-1)+'";\n'
    # Input data
    jdl += 'InputData = {'+ inputdatastr + '};\n'
    jdl += 'InputSandbox = {"RMSynthesis2.sh", "run2.sh", "prmon_1.0.1_x86_64-static-gnu72-opt.tar.gz"};\n'
    # Output data
    jdl += 'OutputSandbox = {"StdOut", "StdErr", '+'"outputtxt_'+str(id_start)+'_'+str(id_end-1)+'.txt",'+'"prmon'+str(id_start)+'_'+str(id_end-1)+'.txt"' + '};\n'
    jdl += 'OutputData = "'+lfn+'/second/test_results_experiment_'+str(expmnt)+'/' + timestamp + '/LOS_'+str(id_start)+'_to_'+str(id_end-1)+'_%j.npy";\n'
    jdl += 'OutputSE = "UKI-NORTHGRID-MAN-HEP-disk";\n'
    try:
        diracUsername = getProxyInfo()['Value']['username']
    except:
        print 'Failed to get DIRAC username. No proxy set up?'
        sys.exit(1)
    jdl += 'JobGroup = "' +diracUsername+ 'rmsynthesis_test'+ '";\n'
    #print jdl
    result = dirac.submitJob(jdl)
    if result['OK']:
     print 'Submission Result: ',result['JobID']
    else:
     print 'There was a problem submitting your job(s)'
     print result
    print

    print '\n'
