#!/bin/bash
echo "service apache2 start && service cron start && sleep infinity" | docker run -i -p 8080:80 hackpeas/jarvis-the-hunter:1.0 sh
