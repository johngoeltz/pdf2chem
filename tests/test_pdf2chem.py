from pdf2chem import pdf2chem as p2c
from pdf2chem import __version__
import os
import re
from datetime import datetime

def test_version():
    assert __version__ == '0.1.5'

def test_curate_folder():
    # Currently tests function by asserting whether files were output by the function with today's date in the filename
    # The function curate_folder() uses all other functions in the package and outputs csv files with the date in the filename.
    # future work will involve checking the expected output, though this depends on NIH's sevrers and other externalities
    # expected_output = [['', 'Name', 'SMILES'], ['0', 'choline chloride', 'Check'], ['1', 'urea', 'Check']]
    p2c.curate_folder()
    todays_files = [filename for filename in os.listdir(os.getcwd()) if re.search(datetime.today().strftime('%Y%m%d'), filename)]
    assert todays_files
