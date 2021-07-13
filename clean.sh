#!/bin/bash

cd src
python setup.py clean -a
# My Horrific script to remove other compiled files
find . -name "*.pyx" | sed "s/pyx$/*/" | xargs -L1 find . \( -name "*.c" -o -name "*.cpython*" \) -wholename | xargs rm -v