# Import Data

```cmda.import_data``` library has handful modules to import continuous data from local disk or Physionet databases.

The availabe modules are as follows:

## ImportWFDB
```cmda.import_data.ImportWFDB``` is a module, which utilizes [*wfdb*](https://wfdb.readthedocs.io/en/latest/index.html) package to import [**WFDB Physionet**](https://physionet.org/about/database/) databases. An example of using this module is shown [here].

## RollingWindowWFDB
```cmda.import_data.RollingWindowWFDB``` is a module similar to ```cmda.import_data.ImportWFDB``` for reading [**WFDB Physionet**](https://physionet.org/about/database/) databases and segementing the data sequence in a rolling window manner. A tutorial of using this module can be found [here].

## ImportCSV
```cmda.import_data.ImportCSV``` is a module to read *CSV* files. An example of using this module can be found [here].
!!! note
    the csv files must constain signals as columns and temporal instances as rows.

## RollingWindowCSV
```cmda.import_data.ImportCSV``` is a module similar to ```cmda.import_data.RollingWindowCSV``` for importing *CSV* files and segementing the data sequence in a rolling window manner. A tutorial of using this module can be found [here].
!!! note
    the csv files must constain signals as columns and temporal instances as rows.

