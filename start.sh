#!/bin/bash
echo "bash /Jarvis/start.sh && sleep infinity" | docker run -i -p 80:80 hackpeas/jarvis-the-hunter:1.0 sh
