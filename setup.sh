#! /bin/sh

CURRENT_FILE_DIRECTORY=$(dirname $0)

# Install test package dependencies
pip install -r $CURRENT_FILE_DIRECTORY/requirements.txt

# Install 9dt
APP_DIRECTORY="9dt-app"
ZIP_FILE="$APP_DIRECTORY/9dt-app-tmp.zip"
rm -rf $APP_DIRECTORY || true
mkdir $APP_DIRECTORY
curl "https://98point6-homework-assets.s3-us-west-2.amazonaws.com/9dt-test.zip" --output $ZIP_FILE

# Unzip and move contents to appropriate folder
unzip $ZIP_FILE -d $APP_DIRECTORY
cp -a $APP_DIRECTORY/9dt-test/example_implementation/. $APP_DIRECTORY/

# Clean up 9dt folder
rm -rf $APP_DIRECTORY/9dt-test
rm $ZIP_FILE

# Install 9dt dependencies
pip2 install -r 9dt-app/requirements.txt