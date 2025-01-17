# Instructions for using the publication scraping features provided by the Academic Tracker python package

https://github.com/MoseleyBioinformaticsLab/academic_tracker/tree/main

install either via pip or source download

The general workflow is to call the update_author_pubs.py script and it will search through either all authors configured in the authorConfigFiles
folder or just ones specified in the --author argument

Example command:
python update_author_pubs.py update --author robmacleod --arguments "['--test','--no-ORCID','--no-Crossref']"

The "--test" should always be included in the arguments. Without this, academic_tracker will try to send an email report to whoever 
is configured in the config file.

Also, --no-ORCID should be used for now as, without an ORCID api key, all ORCID searches will fail.

Also, cross ref will occasionally time out causing the pull to fail.

The default options are:
["--test", "--no-ORCID", "--verbose"]

Output files will be generated for each author. Each will be in a time stamped folder called tracker-test-yymmddhhmm

Consol log files will be written to a log folder in the calling directory.



The json2bibtex.py is a first pass at converting the json output of academic tracker into a bibtex ready format.

python json2bibtex.py convert --inFile <input.json> --outFile <output.bib> --prefix SomePrefix:
