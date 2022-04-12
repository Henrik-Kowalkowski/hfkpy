# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

from definitions import version


# -- Project information -----------------------------------------------------

project = "hfkpy"
copyright = "2022, Henrik Kowalkowski"
author = "Henrik Kowalkowski"

# The full version, including alpha/beta/rc tags
release = f"v{version}"


# -- General configuration ---------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- User added options ------------------------------------------------------

# Extensions to govern site creation
extensions = [
    "sphinx.ext.autodoc",  # to automatically document
    "sphinx.ext.coverage",  # report on how the documentation went
    "sphinx.ext.napoleon",  # support google and numpy docstrings
    "sphinx.ext.viewcode",  # add source code refs on function doc
    "sphinx.ext.duration",  # to time build
    "nbsphinx",  # for ipynb
    "myst_parser",  # for md/txt
]

# Settings for automatic documentation
autodoc_default_options = {
    "member-order": "bysource",
    "undoc-members": True,
}

# To remove warning
## WARNING: html_static_path entry '_static' does not exist
html_static_path = []

# To enable the building of markdown pages
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}
