#!/usr/bin/env bash

for script in 792927*.py; do
	output="${script}.txt";
	echo "running $script"
	echo -ne "\nRunning $script on $(date)\n" >> $output;
	python3 $script >> $output;
done



