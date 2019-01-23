#!/bin/bash
#SBATCH --time=03:00:00
#SBATCH --nodes=1
#SBATCH --job-name=Fernanda-task_2018
#SBATCH --account=def-ycoady
#SBATCH --mem=0
#SBATCH --array=1-200
#SBATCH --mail-type=all               # Type of email notification- BEGIN,END,FAIL,ALL
#SBATCH --mail-user=gaobing@uvic.ca   # Email to which notifications will be sent
module load singularity/2.6
module load python/3
echo 'Step1 load singularity!'
#singularity shell --bind /project/rpp-ycoady/spectral:spectral /project/rpp-ycoady/spectral/singularity/polymer.simg  

echo 'Step2 start singularity exec command!'
singularity exec --bind /home/gaobing/projects/rpp-ycoady/spectral:spectral /home/gaobing/projects/rpp-ycoady/spectral/singularity/polymer4.9co4.simg  /spectral/gaobing/scripts/2018/stub49a_1.sh
#echo 'Step3 go to  polymer!'
#python3
#echo 'Step4 start python!'
#import polymer
#exec(open("/spectral/gaobing/scripts/test1.py").read())
echo 'Finished!'

