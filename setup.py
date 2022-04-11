from setuptools import setup, find_packages
from definitions import version

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1.4.1", "fitbit>=0.3.1", "cherrypy>=18.6.0"]

setup(
    name="hfkpy",
    version=version,
    author="Henrik Kowalkowski",
    author_email="henrikkowalkowski@gmail.com",
    description="A package of helper functions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Henrik-Kowalkowski/hfkpy",
    packages=find_packages(include=["hfkpy.*"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
