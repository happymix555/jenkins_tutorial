import argparse
import time

# program description
ProgramDescriptionStr = 'This script is used in production'

# config file path
ConfigFilePathStr = 'config_file.txt'

# parse argument
parser = argparse.ArgumentParser( description=ProgramDescriptionStr )
parser.add_argument( '--testArgumentStr', type=str,
					help='input any word you want...',
					default='test argument of production script' )

# get argument
args = parser.parse_args()
testArgumentStr = args.testArgumentStr

# open config file 
with open( ConfigFilePathStr ) as productionConfigFile:

	# store every line of config file as list
	allConfigLineList = productionConfigFile.readlines()

# store timestamp of previous loop
previousLoopTimeSec = time.time()

# loop counter
loopCounterInt = 0

# loop forever
while True:

	# for each 1 second
	if time.time() - previousLoopTimeSec >= 1:

		# reach designed number of loop
		if loopCounterInt == 2:

			# exit loop
			break

		# inform user
		print( 'we are in the loop of {}'.format( testArgumentStr ) )

		# update last loop time
		previousLoopTimeSec = time.time()

		# update loop counter
		loopCounterInt += 1

# inform user
print( '[production script] argument: {}, config: {}'.format( testArgumentStr, allConfigLineList[ 0 ] ) )