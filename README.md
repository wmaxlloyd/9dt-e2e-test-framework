This repository is a test framework for the app `9dt` from 98point6. To download the app you can follow [this link](https://98point6-homework-assets.s3-us-west-2.amazonaws.com/9dt-test.zip).

# Usage Instructions
If you haven't already you will need to download `Docker` ([Mac](https://docs.docker.com/docker-for-mac/install/)) ([Windows](https://docs.docker.com/docker-for-windows/install/))

To run the suite of e2e tests, use the `Makefile` to `build` and `run`:
```sh
$ make build run
```

If you want to clean your environment by deleting all images, containers and artifacts use:
```sh
$ make clean
```

If you want to copy the test results out of the container to an `artifacts` directory, use:
```sh
$ make archive
```

# Setting up your environment for local development
## Dev Dependencies:
* python3
* pip
* curl
* unzip
* python2 (Used by the 9dt app)
* pip2 (Used by the 9dt app)

## Setup
To set up your environment and install the 9dt app, run the setup script:
```sh
$ ./setup
```

You will then be able to invoke tests directly by using:
```
$ python e2e_tests.py
```