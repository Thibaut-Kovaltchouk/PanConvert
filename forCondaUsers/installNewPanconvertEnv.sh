#!/bin/bash
echo creation of the PanConvert environment with python 3.8
conda create --name PanConvert python=3.8 -y
echo installation of PyQt
conda install --name PanConvert PyQt -y
echo installation of pandoc
conda install --name PanConvert Pandoc -y
echo PanConvert environment created
