from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=1.4.1"]

setup(
    name="hfkpy",
    version="0.0.1",
    author="Henrik Kowalkowski",
    author_email="henrikkowalkowski@gmail.com",
    description="A package of helper functions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Henrik-Kowalkowski/hfkpy",
    packages=["hfkpy"],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
