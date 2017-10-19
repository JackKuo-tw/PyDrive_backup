#!/bin/bash

date=$(date '+%Y-%m-%d-%H-%M-%S')
location='/tmp/'
file=$location$date
7z a $file.7z `cat file_list`
python backup.py $file.7z $date.7z
