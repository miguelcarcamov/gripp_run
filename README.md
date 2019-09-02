# Scripts to run Rotation Measure Synthesis on the GRIDPP using Dirac nodes

## Chain

1. job_submit_API.py

2. RMSynthesis2.sh

3. run2.sh

## job_submit_API.py

This script take the following arguments as input:

1. Number of pixels. For example, if the image has 2048x2048 pixels, then the args would be 2048 2048
2. The input dataset folder. We are going to work with different simulated input dataset. If the beam size changes along frequency then we would use dataset_normal, if the beam size is constant along frequencies we will use dataset_midfreq. mid_freq is the name because all images in the cube have been convolved with the middle frequency CLEAN beam.
3. Number of processors. The number of processors that will calculate the rotation measurement in phi space.
4. Chunks. Each node, will receive a chunk of lines of sight. For example, if chunks is 512, then each node will work on 512 lines of sight.

## Input data
Since the input data has two simulated MeerKAT datasets that consist in two cubes Q and U each, the input data has been compressed in a 17 parts tarball. The MeerKAT cubes are 135 images of 2048x2048 pixels along frequency. 

## Lines of sight ID

The IDs of the output files on each depend of what chunk the node will process. For example, if the chunks input argument is 512, then in the first submission, the node will work from ID 0 to ID 511. Then the second will work from 512 to 1023, and so on. Until reach the 2048x2048 lines of sight.

