#!/bin/bash
apt-get update && apt-get upgrade
apt-get install docker.io
docker pull hackpeas/jarvis-the-hunter:1.0
