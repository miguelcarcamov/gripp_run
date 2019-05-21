#!/bin//bash
ls -lah
#cd meerkat
python3 /rm_synthesis_simple/realdata_test_parallel.py freqlist.txt data.par sim_Q.fits sim_U.fits sim_Q.fits output_test 8 1000 True 0.05 > outputtxt.txt
