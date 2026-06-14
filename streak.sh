#!/bin/bash

cd ~/home/dhruv/Desktop/revision

git add .
git commit -m "revision Daily Update $(date '+%Y-%m-%d %H:%M:%S')"
git push origin master

echo "GitHub streak updated!"