#!/bin/bash
set -e
echo "========="
ls -lah
echo "=================="
echo "Print environment details"
printenv
echo "========="
singularity --version

echo "Extracting Process Monitor - This is to monitor the processes that we will run"
mkdir prmon && tar xf prmon_1.0.1_x86_64-static-gnu72-opt.tar.gz -C prmon --strip-components 1
echo "Extracting our dataset. This contains the Meerkat Simulated data with 10000 sources in a 2048x2048 image"
tar -xzvf HPC_data.tar.gz
echo "Running prmon"
./prmon/bin/prmon -p $$ -i 10 &

echo "Let's see in what path are we"
echo $PWD

echo "Let's see what's in here"
ls -lah

echo "Let's see how many processors our machine has"
lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('

echo "Lets create a tmp folder to keep temporal files"
mkdir tmp

echo "Ok! Let's run the container"
singularity exec --cleanenv -H $PWD:/srv -B $PWD:/srv -W $PWD:/srv -C shub://miguelcarcamov/container_docker:hpc bash run.sh

mv prmon.txt prmon.txt
ls -ltrh
