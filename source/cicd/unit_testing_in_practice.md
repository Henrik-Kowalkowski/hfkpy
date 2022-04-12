# Unit Testing in practice

## Why do it?
Unit testing allows the creators of this package to know that their functions do what they expect. Additionally, during decentralized package development, integration of unit tests with CICD allows for tests to run automatically whenever code is pushed. This means that pull requests cannot be merged unless tests pass.

## How to do it
Unit testing should be done as functions are written. Whenever a person writes a function, as they build it out they test the increments of analysis manually to ensure that when it all comes together it does what they expect. Writing unit tests is just a natural extension of this practice to ensure that function logic is consistent. For more info, see this great [resource](https://py-pkgs.org/05-testing)!