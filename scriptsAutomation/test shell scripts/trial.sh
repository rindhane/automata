#! /usr/bin/env bash

input1=$1 

function trial {
    echo "$(($input1 + 1))"
    echo $input1
}

trial

#why this doesn't work
#echo "$(($1+1))"