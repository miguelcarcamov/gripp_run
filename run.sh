#!/bin/bash
ls -lah

python3 /rm_synthesis_simple/realdata_test_parallel.py meerkat/freqlist.txt meerkat/data.par meerkat/sim_Q.fits meerkat/sim_U.fits meerkat/sim_Q.fits meerkat/output_test 8 1000 True 0.05 > outputtxt.txt
