#!/bin/env bash

ENV_NAME="django_venv"
PYTHON_PATH='/usr/bin/python3'
pip3 install virtualenv
$PYTHON_PATH -m virtualenv $ENV_NAME
activate="`pwd`/$ENV_NAME/bin/activate"

if [ ! -f "$activate" ]
then
    echo "ERROR: activate not found at $activate"
    return 1
fi

source $activate

pip install -r requirement.txt