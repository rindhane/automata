#! /usr/bin/env bash

folder='Conversion'
len=${#folder}
last='.py'
end=$((-${#last}-1))

for i in $folder/*; 
do 
    ./pdf_to_img.py "${i}" --output_path=./outputs --format png \
    --prefix "${i:$(($len+1)):$end}" --output_path=images --fullconvert=yes
done