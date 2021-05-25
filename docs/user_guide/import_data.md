# Import Data

```cmda.import_data``` library has handful modules to import continuous data from different sources, such as local disk, server or Physionet database.

The availabe modules are as follows:

## ImportWFDB
```cmda.import_data.ImportWFDB``` is a module built over [*wfdb*](https://wfdb.readthedocs.io/en/latest/index.html) package to import [**WFDB Physionet**](https://physionet.org/about/database/) databases. An example of using this module is shown [here].

## ImportCSV
```cmda.import_data.ImportCSV``` is a module to read *csv* files. An example of using this module can be found [here].
!!! note
    the csv files must constains signals as columns and temporal instances as rows.

## ImportFeather
```cmda.import_data.ImportCSV``` is a module to read *feather* files. An example of using this module can be found [here].
!!! note
    the csv files must constains signals as columns and temporal instances as rows.

