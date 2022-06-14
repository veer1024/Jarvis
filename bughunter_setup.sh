#!/bin/bash
python3 banner2.py
#read -p "Enter email you have assigned to jarvis: " jarvis
jarvis="noneed@gmail.com"
#read -p "Enter password for jarvis: " jarvis_pass
jarvis_pass="noneed"
#read -p "Enter email you have assigned to bughunter: " bughunter
bughunter="noneed@gmail.com"
#read -p "Enter password for bughunter: " bughunter_pass
bughunter_pass="noneed"
read -p "Enter S3 bucket name: " bucket
read -p "Enter AWS user access_key: " access_key
read -p "Enter AWS user secret_key: " secret_key
echo "Jarvis:$jarvis:$jarvis_pass
Bughunter:$bughunter:$bughunter_pass
Bucket:name:$bucket
aws_creds:$access_key:$secret_key" > /etc/creds.config-test

