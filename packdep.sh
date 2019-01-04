#! /bin/bash

if [ -e "cthrough_lambda.zip"  ]; then
	echo "removing existing package"
	rm cthrough_lambda.zip
fi
export VIRTUALENV='cthrough_lambda_env'
export ZIP_FILE='cthrough_lambda.zip'
export PYTHON_VERSION='python3.6'

# Zip dependencies from virtualenv, and main.py
cd $VIRTUALENV/lib/$PYTHON_VERSION/site-packages/
zip -r9 ../../../../$ZIP_FILE *
cd ../../../../
zip -g $ZIP_FILE csim.py knowledge_extractor.py simlib.py stopwords.py lambda_func.py util.py imageinfo_extractor.py

echo "deploy to lambda"
python3 update_lambda.py
if [ $? = '0' ]; then
	echo 'successfully deployed to lambda'
else
	echo 'deployment failed'
fi
