#!/bin/bash
echo installing dependencies...
sudo apt-get update
sudo apt-get install python3

python3 -m pip install keyboard
echo installation completed.