#!/bin/bash

for x in `ls posts`; do
    python3 scripts/identicon.py posts/$x
    echo generated for posts/$x
done
site watch
