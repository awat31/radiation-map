#!/bin/bash
# This script is added to cron to automatically start the data pull process and update the map
cd /var/www/html
python3 json_to_geojson-sql.py
echo "Map Updated"
