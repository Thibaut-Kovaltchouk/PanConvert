#!/bin/bash
echo activation of PanConvert environment
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate PanConvert
echo $PREFIX
echo activation done
echo run python script
python ../Panconvert.py
echo end of the script
echo begin deactivate environment
conda deactivate
echo environment deactivated
