#!/bin/bash


#THIS IS THE STARTUP SCRIPT FOR RUNNING MOSIX ON CLOUD
sudo apt update
sudo apt install python3-pip
export LC_ALL=C
wget http://www.mosix.cs.huji.ac.il/mos4/MOSIX-4.4.4.tbz
tar -xf ./MOSIX-4.4.4.tbz
pip3 install redis
echo 'now install mosix and run ./discovery'