#!/bin/bash
apt-get update 1>/dev/null 2>error.txt && apt-get upgrade -y 1>/dev/null 2>error.txt 
apt-get -y install python3 1>/dev/null 2>error.txt
apt  -y install python3-pip 1>/dev/null 2>error.txt
pip3 install -r requirements.txt 1>/dev/null 2>error.txt
python3 banner.py
#echo -e "\e[1;31m Installation will begun shortly \e[0m" 
apt-get install docker.io -y 1>/dev/null 2>error.txt
docker pull hackpeas/jarvis-the-hunter:1.0 1>/dev/null 2>error.txt
cat error.txt 2>/dev/null
echo -e "\e[1;31m Setup is done, run start.sh \e[0m" 
