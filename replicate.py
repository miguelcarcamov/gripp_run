import sys
import os


lfn = 'LFN:/skatelescope.eu/user/m/miguel.carcamo/'

parts = 17
inputdata_list = []

for i in range(parts):
	if i<10:
		inputdata_list.append(lfn + 'second/HPC_data.tar.gz.0'+str(i))
	else:
		inputdata_list.append(lfn + 'second/HPC_data.tar.gz.'+str(i))

inputdata_list.append(lfn + 'second/'+'run2.sh')
inputdata_list.append(lfn + 'second/'+'RMSynthesis2.sh')

SEList = ['UKI-LT2-IC-HEP-disk', 'UKI-LT2-QMUL2-HEP-disk', 'UKI-NORTHGRID-LANCS-HEP-disk']
source = 'UKI-NORTHGRID-MAN-HEP-disk'

for stel in SEList:
	for inp_data in inputdata_list:
		command = 'dirac-dms-replicate-lfn '+inp_data+' '+stel+' '+source
		print command
		os.system(command)
