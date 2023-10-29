# CMDA

**CMDA**  is a Python package specifically tailored for time series data research. It streamlines tasks related to temporal data, encompassing importing, preprocessing, and feature extraction for comprehensive analysis.

This tool has been developed by ***Joint Research Center for Computational Biomedicine (JRC-COMBINE)***, a research institute of RWTH Aachen University.

The key features are:

* **Data Import**: Read high resolution signals from local files, server or Physionet Database.
* **Data Pre-processing**: Outlier removal, noise filtering and missing value imputation.
* **Feature Extraction**: Extract features from the imported signals using built-in features or user-defined features.
* **Feature Engineering Pipeline**: Build an automated pipeline for importing data, pre-processing and feature extraction.


## Installation

### Requirements
* Python (>=3.8)
* NumPy (>=1.13.3)
* Pandas (>=1.2.2)
* Scipy (>=0.19.1)
* WFDB (>= 4.0.0)
* pathos (>= 0.2.9)
* tqdm
* PyWavelets

### User Installation
#### with pip
CMDA can be installed with pip:
```bash
pip install git+https://github.com/JRC-COMBINE/cmda
```
This will automatically install compatible versions of all dependencies.

#### with git
CMDA can be directly used from GitHub by cloning the repository into a subfolder of your project root.
```bash
git clone https://github.com/JRC-COMBINE/cmda
```
When cloning from git, all required dependencies must be installed as follows:

```bash
pip install -r cmda/requirements.txt
```

