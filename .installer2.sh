#!/bin/bash

if [[ ! $(command -v ruby) ]]; then
	echo 'Installing ruby...'
	sleep .1
	pkg install ruby -y
elif [[ $(command -v ruby) ]]; then
	echo ' '
fi
if [[ ! $(command -v lolcat) ]]; then
	echo "Installing lolcat..."
	sleep .1
	gem install lolcat > /dev/null 2>&1
elif [[ $(command -v lolcat) ]]; then
	echo " "



fi
if [[ ! $(command -v mpv) ]]; then
	echo "Installing mpv..."
	sleep .1
	apt install mpv -y > /dev/null 2>&1
elif [[ $(command -v lolcat) ]]; then
	echo " "


fi
#python3 .cybersh.py

if [[ ! $(echo $?) == "0" ]]; then
	echo "an error occured"
	exit
else
	python3 .cybersh2.py
fi
