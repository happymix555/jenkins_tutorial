#!/bin/bash

# This is a Bash script to run a Python script.

# path to python scritp
testSyncScriptProductionPath="test_sync_script_production.py"

# Check if test_sync_script_production.py exists
if [ -f "$testSyncScriptProductionPath" ]; then

	# inform user
	echo "Running the Python script: $testSyncScriptProductionPath"

	# run python script
	python3 "$testSyncScriptProductionPath" --testArgumentStr="argument from bash"

# script was not found
else

	# inform user
	echo "Python script not found: $testSyncScriptProductionPath"
fi