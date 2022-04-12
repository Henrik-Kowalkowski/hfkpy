# Envrionment management

## Background
There are 3 environments at play in this package to keep in mind:
- development environment `envhfkpy`
- CICD environment `test_envhfkpy`
- user environment `unknown` but augmented by `setup.py`

The development environment is used by the developers of this package. It requires everything needed to execute the package plus the packages required to document the package. The CICD environment contains only the packages required to test the environment. The user environment is unknown, so it is important to set the requirements in [setup.py](https://github.com/Henrik-Kowalkowski/hfkpy/blob/main/setup.py) such that the user can run the package functions if they do not have the required packages already. When installing hfkpy with pip, pip will automatically download the dependencies listed in `setup.py`.

## For devlopers
If you are adding packages to `env_hfkpy`, or `test_envhfkpy`, make sure that you run `python conda_env_export.py > [env_name].yml` so that the environments are up to date for other users. Also be sure to keep in mind `setup.py` as well. [conda_env_export.py](https://github.com/Henrik-Kowalkowski/hfkpy/blob/main/conda_env_export.py) is a custom script that builds the yml for the conda environment from the active conda environment in a way that is OS agnostic so developers can build on Mac OS, Windows, and Linux without concern. The development environment can be refreshed with `conda env remove -n [env_name] --all` followed by `conda env create -f [env_name].yml --prefix [location_of_env]/[env_name]`