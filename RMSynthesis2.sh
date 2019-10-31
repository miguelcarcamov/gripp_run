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
echo $5 #job ID

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

#echo "Lets create a tmp folder to keep temporal files"
#mkdir -p tmp

#echo "Lets create a folder to save the results"
#result_string=results_experiment_$4/
result_string=./
#mkdir -p $result_string

echo "Let's see what in here again!"
ls -lah

echo "Ok! Let's run the container"

chmod +x run2.sh

rm -rf .singularity

rm -rf *.simg

rm -rf rm_synthesis_simple

git clone https://github.com/miguelcarcamov/rm_synthesis_simple.git

echo "The image is in /cvmfs/sw.skatelescope.eu/images/RMSynthesisTest.simg"

echo "run2.sh file is going to run with the following parameters: $1 $2 $3 $4 $result_string"
singularity exec --cleanenv -H $PWD:/srv --pwd /srv -C /cvmfs/sw.skatelescope.eu/images/RMSynthesisTest.simg bash run2.sh $1 $2 $3 $4 $result_string

real_n=$(($3-1))
mv prmon.txt prmon$2_$real_n.txt
mv $6.npy $6_$5.npy
ls -ltrh
