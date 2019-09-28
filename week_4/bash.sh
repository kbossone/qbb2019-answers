#!/bin/bash
echo "enter the directory path:"
read directory
for file in $directory; do
    ./manhattan.py $file
done