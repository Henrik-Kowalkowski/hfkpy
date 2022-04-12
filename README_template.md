# hfkpy
An example of a tested and installable package of helper functions.

## To install from Git
`pip install git+https://github.com/Henrik-Kowalkowski/hfkpy@v{version}`

## To document
1. `conda install sphinx` in git bash
2. `sphinx-quickstart` in git bash
3. `pip install sphinx-rtd-theme` in git bash
4. `conda install pandoc` in git bash
5. `make html` in cmd (if on Windows)

## Git actions
`python conda_env_export.py > envhfkpy.yml`  
`python conda_env_export.py > test_envhfkpy.yml`  
`conda env create envhfkpy.yml --prefix place_to_store_env/env_name`