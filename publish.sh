#! /bin/bash

echo Updating poetry.lock
poetry update || { echo "Failed to update poetry.lock"; exit 1; }

echo Updating package installation
pip install -e . || { echo "Failed to update package installation"; exit 1; }

echo Running tests
poetry run pytest || { echo "Failed to run tests"; exit 1; }

echo Building the package
poetry build || { echo "Failed to build the package"; exit 1; }

echo Checking the package
poetry check || { echo "Failed to check the package"; exit 1; }

echo Publishing the package to PyPI
poetry publish || { echo "Failed to publish the package to PyPI"; exit 1; }
