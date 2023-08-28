import argparse

# program description
ProgramDescriptionStr = 'This script is used in production'

# parse argument
parser = argparse.ArgumentParser( description=ProgramDescriptionStr )
parser.add_argument( '--testArgumentStr', type=str,
					help='input any word you want...',
					default='test argument of production script' )

# assert some error to investigate the behavior when jenkins found error
if 'string' == 1:
	print( 'error was found' )

# get argument
args = parser.parse_args()
testArgumentStr = args.testArgumentStr

# open config file 
with open( 'test_config_production.txt' ) as productionConfigFile:

	# store every line of config file as list
	allConfigLineList = productionConfigFile.readlines()

# inform user
print( '[production script] argument: {}, config: {}'.format( testArgumentStr, allConfigLineList[ 0 ] ) )