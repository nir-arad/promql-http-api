#! /bin/bash

echo Updating poetry.lock
poetry update

echo update package installation
pip install -e .

echo Running tests
poetry run pytest

echo Building the package
poetry build

echo Checking the package
poetry check

echo Publishing the package to PyPI
poetry publish
