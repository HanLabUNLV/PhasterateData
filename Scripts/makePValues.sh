#!/bin/bash

# Given a Likelihoods file (computedLikelihoods.txt) from the output of phyloP we will
# compare the null and alt model with 1 degree of freedom and print the p-values per line
# to standard output.

awk '{print $1}' $1 > null.txtTemp &&
    awk '{print $2}' $1 > alt.txtTemp &&
    python lrtTest.py  alt.txtTemp null.txtTemp  computedLrt.txtTemp &&
    python pValues.py computedLrt.txtTemp 1 pValues.txt &&
    rm null.txtTemp alt.txtTemp computedLrt.txtTemp
