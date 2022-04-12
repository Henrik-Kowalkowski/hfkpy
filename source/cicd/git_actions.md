# How this package uses Git Actions

## Background
Git Actions are a way to automatically run code whenever an event like a pull or push happens via Git. This [example action](https://github.com/Henrik-Kowalkowski/hfkpy/blob/main/.github/workflows/unit-test-hfkpy.yml) runs our unit tests whenever we push. 

## Notes on usage
You can [skip running the CICD](https://github.blog/changelog/2021-02-08-github-actions-skip-pull-request-and-push-workflows-with-skip-ci/) by adding `[skip ci]` to the commit message of your commit. This CICD uses a smaller version of `envhfkpy`, called `test_envhfkpy` in order to run more quickly.