#!/bin/bash
echo "NICE!!!!!! NOW WE ARE EXECUTING THE CONTAINER"

echo "Let's see where we are"
pwd

echo "Let's see what's here"
ls -lah

echo "Let's see how many processors our machine has"

lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
PROCS=$(lscpu | grep -E '^Thread|^Core|^Socket|^CPU\(' | grep "CPU" | grep -o '[[:digit:]]*')
#PROCS=8

echo "Running RMSynthesis with $PROCS cores"
echo "Running command: python3 /rm_synthesis_simple/realdata_test_parallel.py meerkat/freqlist.txt meerkat/data.par meerkat/sim_Q.fits meerkat/sim_U.fits meerkat/sim_Q.fits meerkat/output_test $PROCS 1000 True 0.05 > outputtxt.txt"

python3 /rm_synthesis_simple/realdata_test_parallel.py meerkat/freqlist.txt meerkat/data.par meerkat/sim_Q.fits meerkat/sim_U.fits meerkat/sim_Q.fits meerkat/output_test $PROCS 1000 True 0.05 > outputtxt.txt
