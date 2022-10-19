#!/bin/env bash

ENV_NAME="django_venv"

pip3 install virtualenv
python3 -m virtualenv $ENV_NAME
activate="`pwd`/$ENV_NAME/bin/activate"

if [ ! -f "$activate" ]
then
    echo "ERROR: activate not found at $activate"
    return 1
fi

source "$activate"

pip3 install -r requirements.txt