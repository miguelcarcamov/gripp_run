#!/bin/bash
set -e
echo "========="
ls -la
echo "=================="
echo "Print environment details"
printenv
echo "========="
echo $PWD
singularity --version

mkdir prmon && tar xf prmon_1.0.1_x86_64-static-gnu72-opt.tar.gz -C prmon --strip-components 1
tar -xzcf HPC_data.tar.gz
./prmon/bin/prmon -p $$ -i 10 &

cd meerkat

singularity -d  exec  --cleanenv --home $PWD:/srv --pwd /srv -C  shub://miguelcarcamov/container_docker:hpc './run.sh'
mv prmon.txt prmon.txt
ls -ltrh
