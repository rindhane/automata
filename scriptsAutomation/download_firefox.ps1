#! /usr/bin/env bash 
# commands are set for powershell
# remove $ from variable assignment to make it ready for bash shell

$version='89.0.1'
#$system='linux-x86_64'
#$name="firefox-${version}.tar.bz2"
$system='win64-EME-free'
$name="Firefox%20Setup%20${version}.exe"

curl https://download-installer.cdn.mozilla.net/pub/firefox/releases/${version}/$system/en-US/${name} -o ${name}

