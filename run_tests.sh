#!/bin/bash

# Exit immediately if a command fails
set -e

# Activate virtual environment
source venv/Scripts/activate

# Run the test suite
pytest
