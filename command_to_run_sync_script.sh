#!/bin/bash

# This is a Bash script to run a Python script.

# show user who is execute this script
echo "$0 is executed by $(whoami)"

# path to python scritp
SyncScriptFilePath="sync_script.py"

# Check if sync script exists
if [ -f "$SyncScriptFilePath" ]; then

	# inform user
	echo "Running the Python script: $SyncScriptFilePath"

	# run python script
	python3 "$SyncScriptFilePath" --testArgumentStr="1"
	python3 "$SyncScriptFilePath" --testArgumentStr="2"
	python3 "$SyncScriptFilePath" --testArgumentStr="3"
	python3 "$SyncScriptFilePath" --testArgumentStr="4"

# script was not found
else

	# inform user
	echo "Python script not found: $SyncScriptFilePath"
fi
