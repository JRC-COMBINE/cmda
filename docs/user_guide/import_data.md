# Import Data

```cmda.import_data``` library provides the modules to import multiple time-series data files from local disk.

The availabe modules are as follows:

## ImportCSV
[```cmda.import_data.ReadCSV```](../api/read_data/readCSV.md) is a module to read multiple *csv* files. An example of using this module can be found [here](../examples/pipeline.ipynb).

!!! note
    The csv files must constain signals as columns and temporal instances as rows.

## RollingWindowCSV
[```cmda.import_data.RollingWindowCSV```](../api/read_data/rollingCSV.md) is a module similar to [```cmda.import_data.ReadCSV```](../api/read_data/readCSV.md) for importing *csv* files and segementing the data sequence in a rolling window manner. The segmentation process allows the [pipeline](../user_guide/pipeline) module to distribute each segment on multiple CPU cores in case of parallel feature extraction, which reduces the computation time significantly.

!!! note
    The csv files must constain signals as columns and temporal instances as rows.

!!! note
    In case of uneven data sampling, a DateTime column is required for the segmentation step.

