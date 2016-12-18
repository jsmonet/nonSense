#!/bin/bash

echo -e "setting up basic packages"
if [ -z `which pip` ]; then sudo apt-get install -y python-pip; else echo "already installed"; fi

for pippkg in pydns validate_email; do if pip list | grep ${pippkg}; then echo "$pippkg installed"; else sudo pip install ${pippkg}; fi

if [ -z `apt -qq list sense-hat`]; then sudo apt-get install -y sense-hat; else echo "sense-hat already installed"; fi
