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
`conda env export --from-history > envhfkpy.yml`  -- for developing the package
`conda env export --from-history > test_envhfkpy.yml`  -- for CICD testing purposes
https://autobencoder.com/2020-08-24-conda-actions/