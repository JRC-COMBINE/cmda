from setuptools import setup, find_packages


req_packs = [
    'pandas',
    'numpy',
    'tqdm',
    'scipy',
    'sklearn',
    'wfdb',
    'PyWavelets',
    'pathos'
]


setup(name='CMDA',
      version='0.0.12',
      description='Continuous Monitoring Data Analysis',
      author='Pejman Farhadi Ghalati',
      author_email='farhadi@combine.rwth-aachen.de',
      packages =find_packages(),
      install_requires = req_packs,
      package_data = {'cmda':['data/*.csv']}
     )