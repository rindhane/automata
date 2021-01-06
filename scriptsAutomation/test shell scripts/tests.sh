#! /usr/bin/env bash

echo 'running tests.sh'

function get_file {
    #file="$1";
    echo 1;
}

file="./trial.sh"

function get_input {
    files=$1; #$*/ $#
    echo "$files";
}

function inputs {
    for ((i=0;i<2;i++))
    do 
        echo $i;
    done 
}

echo 2 | echo $(</dev/stdin)

#inputs | "$($file)" "$(</dev/stdin)"

#what's wrong here
#name=1
#echo  $name | message=$(</dev/stdin); echo $message 

#what's wrong here
#name=1
#echo  $name | read message; echo $message ;

#why this works
#name=1
#echo $name | { read message; echo $message;} 

#why this doesn't works
#inputs | get_input $(</dev/stdin)

