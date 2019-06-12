#!/bin/bash
set -e
echo "========="
ls -lah
echo "=================="
echo "Print environment details"
printenv
echo "========="
singularity --version

echo "Printing parameters"
echo $0
echo $1 #nprocs
echo $2 #id_start
echo $3 #id_end
echo $4 #experiment

echo "Extracting Process Monitor - This is to monitor the processes that we will run"
mkdir -p prmon && tar xf prmon_1.0.1_x86_64-static-gnu72-opt.tar.gz -C prmon --strip-components 1
echo "Extracting our dataset. This contains the Meerkat Simulated data with 10000 sources in a 2048x2048 image"
cat HPC_data.tar.gz.* | tar xzvf -
echo "Running prmon"
./prmon/bin/prmon -p $$ -i 10 &

echo "Let's see in what path are we"
echo $PWD

echo "Let's see what's in here"
ls -lah

echo "Let's see how many processors our machine has"
lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('

echo "Lets create a tmp folder to keep temporal files"
mkdir -p tmp

echo "Lets create a folder to save the results"
result_string=results_experiment_$4/
mkdir -p $result_string

echo "Let's see what in here again!"
ls -lah

echo "Ok! Let's run the container"
echo "run2.sh file is going to run with the following parameters: $1 $2 $3 $4 $result_string"
singularity exec --cleanenv -H $PWD:/srv --pwd /srv -C shub://miguelcarcamov/container_docker:hpc bash run2.sh $1 $2 $3 $4 $result_string

mv prmon.txt prmon$2_$3.txt
ls -ltrh
