#!/bin/bash
#SBATCH --mem=4196  # Requested Memory
#SBATCH -p gpu  # Partition
#SBATCH -G 1  # Number of GPUs
#SBATCH -t 10:00:00  # Job time limit
#SBATCH -o storage/logs/option-critic-%j.out  # %j = job ID
#SBATCH -e storage/logs/option-critic-%j.err 

cd option_critic
python -m main --env="AmidarNoFrameskip-v4"