#!/bin/bash
echo "======================================== CONTAINER OUTPUT =============================================="
echo "NICE!!!!!! NOW WE ARE EXECUTING THE CONTAINER"
echo "Let's print the variables"
echo $0
echo $1 #nprocs
echo $2 #id_start
echo $3 #id_end
echo $4 #experiment
echo $5 #results

echo "Let's see where we are"
pwd

echo "Let's see what's here"
ls -lah

echo "Let's see how many processors our machine has"

lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
#PROCS=$(lscpu | grep -E '^Thread|^Core|^Socket|^CPU\(' | grep "CPU" | grep -o '[[:digit:]]*')
#PROCS=1

real_end=$(($3-1))

echo "Running RMSynthesis with $1 cores"
echo "Running command: python3 rm_synthesis_simple/realdata_parallel_los.py meerkat/$4/freqlist.txt $2 $3 meerkat/$4/sim_Q.fits meerkat/$4/sim_U.fits meerkat/$4/sim_Q.fits $5 $1 True 1e-5 1e-1 Thin False > outputtxt_$2_$real_end.txt"

python3 rm_synthesis_simple/realdata_parallel_los.py meerkat/$4/freqlist.txt $2 $3 meerkat/$4/sim_Q.fits meerkat/$4/sim_U.fits meerkat/$4/sim_Q.fits $5 $1 True 1e-8 1e-4 Thin False > outputtxt_$2_$real_end.txt
