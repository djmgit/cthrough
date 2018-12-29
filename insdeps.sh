#! /bin/bash

export VIRTUALENV='cthrough_lambda_env'
rm -fr $VIRTUALENV

# Setup fresh virtualenv and install requirements
virtualenv $VIRTUALENV
source $VIRTUALENV/bin/activate
pip install -r requirements_lambda.txt
deactivate
