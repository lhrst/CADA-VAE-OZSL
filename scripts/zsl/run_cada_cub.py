import os
GPU = 6
dataset = 'CUB'
generalized = 'False'

os.system('CUDA_VISIBLE_DEVICES={} OMP_NUM_THREADS=4 \
        python model/single_experiment.py --dataset {} --num_shots 0 --generalized {}\
            '.format(GPU, dataset, generalized))