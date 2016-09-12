#!/bin/bash

files=("bnu-esm" "ccsm4" "cnrm-cm5" "hadgem2-es" "noresm1-m")

for i in "${files[@]}"
do
	echo $i
	mkdir $i/r1i1p1/pr/
	mv cambodia/$i/r1i1p1/historical/pr/* $i/r1i1p1/pr/
	mv cambodia/$i/r1i1p1/rcp85/pr/* $i/r1i1p1/pr/
done
