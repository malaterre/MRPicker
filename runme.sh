#!/bin/bash

#set -x
in=$1
for i in {1..10000}; do ./unz.py "$in" bla.txt $i > o 2>&1 && echo $i; done
