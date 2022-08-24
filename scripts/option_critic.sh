#!/bin/bash
#SBATCH --mem=4196  # Requested Memory
#SBATCH -p gpu  # Partition
#SBATCH -G 1  # Number of GPUs
#SBATCH -t 10:00:00  # Job time limit
#SBATCH -o out/option-critic-%j.out  # %j = job ID
#SBATCH -e out/option-critic-%j.err 

cd option_critic
python -m main --env="AmidarNoFrameskip-v4"