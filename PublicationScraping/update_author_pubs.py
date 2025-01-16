import fire, sys, os, glob, subprocess, logging
from datetime import datetime

DEFAULT_CONFIG_LOCATION="./authorConfigFiles/"
DEFAULT_ACADEMIC_TRACKER_LOCATION="academic_tracker"
DEFAULT_ARGUMENTS="--test --no-ORCID --verbose"
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

	logging.basicConfig(
	    filename=f'{DEFAULT_OUTFILE_LOCATION}{author}-{date}.log',  # Log file name
	    level=logging.INFO,     # Log level
	    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
	    datefmt='%Y-%m-%d %H:%M:%S',  # Date format
	    handlers=[
        logging.FileHandler(log_filename),  # Log to file
        logging.StreamHandler()            # Log to terminal
    ]
	)

	arguments = [f"{config_loc}{author}.json"] + arguments
	runCommand = [script_loc] + arguments
	logging.info(f'Run command {runCommand}')
	result = subprocess.run(runCommand, text=True, capture_output=True)

	
	logging.info("Standard Output:", result.stdout)
	logging.info("Standard Error:", result.stderr)







if __name__=="__main__":
	fire.fire({'update':updatePubs})