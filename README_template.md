# hfkpy
https://img.shields.io/github/v/release/Henrik-Kowalkowski/hfkpy https://img.shields.io/github/workflow/status/Henrik-Kowalkowski/hfkpy/Unit%20Test%20hfkpy https://img.shields.io/github/downloads/Henrik-Kowalkowski/hfkpy/v{version}/total https://img.shields.io/badge/code%20style-black-%23000000

## What is it?
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