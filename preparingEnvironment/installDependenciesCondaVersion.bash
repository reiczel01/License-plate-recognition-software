#!/bin/bash

# Tworzenie nowego środowiska Anaconda
conda create -n myenv python=3.8

# Aktywacja nowego środowiska
conda activate myenv

# Instalacja biblioteki OpenCV (cv2)
conda install -n myenv -c conda-forge opencv

# Instalacja biblioteki pickle
conda install -n myenv -c anaconda pickle-mixin

# Instalacja biblioteki cvzone
pip install cvzone

# Instalacja biblioteki numpy
conda install -n myenv -c anaconda numpy
