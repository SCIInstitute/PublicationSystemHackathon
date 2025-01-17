import fire
import sys, os, glob, subprocess, logging
from datetime import datetime

SCRIPT_DIR=os.path.dirname(os.path.realpath(__file__))

DEFAULT_CONFIG_LOCATION=SCRIPT_DIR+"/authorConfigFiles/"
DEFAULT_ACADEMIC_TRACKER_LOCATION="academic_tracker"
DEFAULT_ARGUMENTS=["--test", "--no-ORCID", "--verbose"]
DEFAULT_OUTFILE_LOCATION="./logFiles/"

def updatePubs(author="all",arguments=DEFAULT_ARGUMENTS,script_loc=DEFAULT_ACADEMIC_TRACKER_LOCATION,config_loc=DEFAULT_CONFIG_LOCATION):
	if author == "all":
		configFiles = glob.glob(f'{config_loc}*.json')
		for file in configFiles:
			name = os.path.basename(file).replace('.json','')
			updatePubs(author=name)
		return

	print(f'Running pub search for {author}')

	# Configure logging
	date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
	logfile_name=f'{DEFAULT_OUTFILE_LOCATION}{author}-{date}.log'
	logging.basicConfig(
	    level=logging.INFO,     # Log level
	    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
	    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
	    handlers=[
        logging.FileHandler(logfile_name),  # Log to file
        logging.StreamHandler()            # Log to terminal
    ]
	)

	arguments = ["author_search", f"{config_loc}{author}.json"] + arguments
	runCommand = [script_loc] + arguments
	logging.info(f'Run command {runCommand}')
	result = subprocess.run(runCommand, text=True, capture_output=True)

	
	logging.info("Standard Output:", result.stdout)
	logging.info("Standard Error:", result.stderr)







if __name__=="__main__":
	fire.Fire({'update':updatePubs})