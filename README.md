# pdf2chem

![](https://github.com/johngoeltz/pdf2chem/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/johngoeltz/pdf2chem/branch/main/graph/badge.svg)](https://codecov.io/gh/johngoeltz/pdf2chem) ![Release](https://github.com/johngoeltz/pdf2chem/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/pdf2chem/badge/?version=latest)](https://pdf2chem.readthedocs.io/en/latest/?badge=latest)

A curator for chemistry-related pdf files

## Installation

```bash
$ pip install pdf2chem
$ cde data download
```

```Jupyter_or_Colab
in Jupyter or Colab
!pip install pdf2chem
!cde data download
import pdf2chem as p2c
```


## Features

- TODO

## Dependencies

- TODO

## Usage

- Place pdf files of interest (typically journal articles) in an accessible folder.
Execute p2c.curate_folder()
If the files are not in the current directory, pass the directory to the function as an argument, e.g.
p2c.curate_folder('C:/Users/kfrog/literature')
The files will then be analyzed internally before a list of words and phrases suspected to be known chemicals is sent to NIH's servers to be resolved.  Chemicals found and their SMILES strings will be aggregated in a csv file for each pdf.
After each pdf is processed, the data from each csv file will be combined to an aggregated csv file for all the papers in that run.

- Please note: this program depends on stable internet access and uptime at NIH's servers.  They are often slower or down entirely on the weekends, and sometimes this is seen during the week as well.  We appreciate the team there making the databases as accessible as they do.

## Documentation

The official documentation is hosted on Read the Docs: https://pdf2chem.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/johngoeltz/pdf2chem/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).

This package makes heavy use of ChemDataExtractor and CIRpy, packages developed by Swain and Cole and released under the MIT license.
Swain, M. C., & Cole, J. M. "ChemDataExtractor: A Toolkit for Automated Extraction of Chemical Information from the Scientific Literature", J. Chem. Inf. Model. 2016, 56 (10), pp 1894–1904 10.1021/acs.jcim.6b00207
