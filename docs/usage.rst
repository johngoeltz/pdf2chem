=====
Usage
=====

To use pdf2chem in a project::

    import pdf2chem as p2c
    !cde data download
    (or run cde data download from a command line interface)

    Place pdf files of interest (typically journal articles) in an accessible folder.
    In python run the function p2c.curate_folder()
    If the files are not in the current directory, pass the directory to the function
    as an argument, e.g., p2c.curate_folder('C:/Users/kfrog/literature')
    The files will then be analyzed internally before a list of words and phrases
    suspected to be known chemicals is sent to NIH's servers to be resolved.
    Chemicals found and their SMILES strings will be aggregated in a csv file for each pdf.
    After each pdf is processed, the data from each csv file will be combined to an
    aggregated csv file for all the papers in that run.

    Please note: this program depends on stable internet access and uptime at NIH's servers.
    They are often slower or down entirely on the weekends, and sometimes this
    is seen during the week as well.
    We appreciate the team there making the databases as accessible as they do.
