# CMDA

**CMDA** is a Python module for analysing continuous monitoring data.

This tool has been developed by ***Joint Research Center for Computational Biomedicine (JRC-COMBINE)***, a joint venture of RWTH Aachen University, and funded by ***Bayer AG***.

The key features are:

* **Data Import**: Read high resolution signals from local files, server or Physionet Database.
* **Data Pre-processing**: Outlier removal, noise filtering and missing value imputation.
* **Feature Extraction**: Extract features from the imported signals using built-in features or user-defined features.
* **Feature Engineering Pipeline**: Build an automated pipeline for importing data, pre-processing and feature extraction.
* **Clustering**: Clustering, clusters robustness and stability evaluation, enrichment analysis and importnat features selection.

## Installation

### Requirements
* Python (>=3.6)
* NumPy (>=1.13.3)
* Pandas (>=1.2.2)
* Scipy (>=0.19.1)
* Scikit-learn (>=0.2)

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
When cloning from git, you must install all required dependencies yourself:

```bash
pip install -r cmda/requirements.txt
```

