#!/bin/bash
apt-get update && apt-get upgrade
apt-get install docker.io
docker pull hackpeas/jarvis-the-hunter:1.0
echo -e "\e[1;31m Setup is done, run start.sh \e[0m"
