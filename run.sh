#!/bin/bash

cd src
python setup.py build_ext --inplace
python -O main.py "$@"