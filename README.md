# postgrad_physics_tutorial

A demonstration of various useful tools

![Tests](https://github.com/paddyroddy/postgrad_physics_tutorial/workflows/Tests/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Install python packages

Run `pip install -r requirements.txt`.

## pre-commit

Execute `pre-commit install` to install hooks in your `.git/` directory

## To build script

Run `pip install -e .` in the top level directory.
Then you can run `woo` in the command line (and pass any arguments you want).

## Tests

To run tests with `pytest` run `pytest -v .`.
Personally I run `pytest -v .` locally and `pytest -v --runslow .` on the CI.
That way you can have longer tests which are only ran when you want them to.
