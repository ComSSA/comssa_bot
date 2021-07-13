#!/bin/bash

cd src
python setup.py build_ext --inplace
python -m unittest discover -s tests/