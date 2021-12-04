#!/bin/bash
# A bash script to make some config changes when the files are pulled from git.
sudo touch temp.json
sudo chmod 666 temp.json
sudo chown -R watkins_aaron2:watkins_aaron2 *
sudo chmod +x *.py
