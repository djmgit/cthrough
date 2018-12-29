#! /bin/bash

export VIRTUALENV='cthrough_lambda_env'
export ZIP_FILE='cthrough_lambda.zip'
export PYTHON_VERSION='python3.6'

# Zip dependencies from virtualenv, and main.py
cd $VIRTUALENV/lib/$PYTHON_VERSION/site-packages/
zip -r9 ../../../../$ZIP_FILE *
cd ../../../../
zip -g $ZIP_FILE csim.py knowledge_extractor.py simlib.py stopwords.py lambda_handler.py
