#!/bin/bash
echo "NICE!!!!!! NOW WE ARE EXECUTING THE CONTAINER"
echo "Let's print the variables"
echo $0
echo $1
echo $2
echo $3

echo "Let's see where we are"
pwd

echo "Let's see what's here"
ls -lah

echo "Let's see how many processors our machine has"

lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
#PROCS=$(lscpu | grep -E '^Thread|^Core|^Socket|^CPU\(' | grep "CPU" | grep -o '[[:digit:]]*')
PROCS=1

echo "Running RMSynthesis with $PROCS cores"
echo "Running command: python3 /rm_synthesis_simple/realdata_test_onepixel.py meerkat/$2/freqlist.txt meerkat/$2/data.par meerkat/$2/sim_Q.fits meerkat/$2/sim_U.fits meerkat/$2/sim_Q.fits $3/output_test_$1.npy $1 True 1e-8 1e-4 False Thin > outputtxt.txt"

python3 /rm_synthesis_simple/realdata_test_onepixel.py meerkat/$2/freqlist.txt meerkat/$2/data.par meerkat/$2/sim_Q.fits meerkat/$2/sim_U.fits meerkat/$2/sim_Q.fits $3/output_test_$1.npy $1 True 1e-8 1e-4 False Thin > outputtxt_$1.txt
