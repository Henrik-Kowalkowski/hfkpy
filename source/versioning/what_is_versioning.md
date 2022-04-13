# What is Versioning?

## Background
Versioning allows us to set stable release points in the code base for users to pull our package from. This way, a user can always find the version of our package that they used in their previous work to replicate that work. More information on versioning can be found in this [awesome resource](https://py-pkgs.org/07-releasing-versioning).

## How to do it here
To version this package, from the root directory of hfkpy run:
- `python version_it.py`
  - follow the onscreen prompts
- `make html`
- on GitHub go to [releases](https://github.com/Henrik-Kowalkowski/hfkpy/releases) and draft a [new release](https://github.com/Henrik-Kowalkowski/hfkpy/releases/new)
  - be sure to add release notes
  - the release name should be `Version x.x.x some lower case short description`
  - add a binary to the release like vx.x.x with contents "vx.x.x track" so that the package downloads can be tracked via git API
  - the badge link in the `README.md` needs to be a `.png` to work properly