import fire
import sys, os, glob, subprocess, logging
from datetime import datetime

SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))

DEFAULT_CONFIG_LOCATION=SCRIPT_DIR+"/authorConfigFiles/"
DEFAULT_ACADEMIC_TRACKER_LOCATION="academic_tracker"
DEFAULT_ARGUMENTS=["--test", "--no-ORCID", "--verbose"]
DEFAULT_OUTFILE_LOCATION="./logFiles/"
RECURSION_LIMIT=1


def logInfo(message,logFile=None):
	'''
	I know I know I know that logging exists, but it is so finnicky
	and I got frustrated
	So here we are with my own simple logger
	'''
	print(message)
	if logFile is not None:
		with open(logFile, "a") as log:
			log.write(message)


def updatePubs(author="all",arguments=DEFAULT_ARGUMENTS,script_loc=DEFAULT_ACADEMIC_TRACKER_LOCATION,config_loc=DEFAULT_CONFIG_LOCATION,depth=0):
	date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	logfile_name=f'{DEFAULT_OUTFILE_LOCATION}{author}-{date}.log'
	if not os.path.isdir(DEFAULT_OUTFILE_LOCATION):
		os.mkdir(DEFAULT_OUTFILE_LOCATION)

	if depth > RECURSION_LIMIT:
		logInfo("RECURSION LIMIT HIT. SOMETHING IS WRONG WITH AUTHOR LIST.",logfile_name)
		return
	if author == "all":
		configFiles = glob.glob(f'{config_loc}*.json')
		for file in configFiles:
			name = os.path.basename(file).replace('.json','')
			updatePubs(name,arguments,script_loc,config_loc,depth+1)
		return

	# Configure logging
	

	logInfo(f'Running pub search for {author}',logfile_name)

	

	arguments = ["author_search", f"{config_loc}{author}.json"] + arguments
	runCommand = [script_loc] + arguments
	logInfo(f'Run command: {runCommand}',logfile_name)
	result = subprocess.run(runCommand, text=True, capture_output=True)

	logInfo(f'Standard output: {result.stdout}',logfile_name)
	logInfo(f'Standard Error: {result.stderr}',logfile_name)






if __name__=="__main__":
	fire.Fire({'update':updatePubs})