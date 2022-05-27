#!/bin/bash

if [[ ! $(command -v ruby) ]]; then
	echo 'Installing ruby...'
	sleep .1
	pkg install ruby -y
elif [[ $(command -v ruby) ]]; then
	echo 'Ruby is already installed..'
fi
if [[ ! $(command -v lolcat) ]]; then
	echo "Installing lolcat..."
	sleep .1
	gem install lolcat > /dev/null 2>&1
elif [[ $(command -v lolcat) ]]; then
	echo "Lolcat is already installed.."
fi
#python3 .cybersh.py

if [[ ! $(echo $?) == "0" ]]; then
	echo "an error occured"
	exit
else
	python3 .cybersh.py
fi
