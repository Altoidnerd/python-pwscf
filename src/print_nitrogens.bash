#!/bin/bash

nitrogen_indices=$(cat efg.*| grep Cq | grep 'N  ' | awk '{print $2}' | sort | uniq)
uniq_freqs=$(cat efg.* | grep Cq | grep 'N  ' | awk '{print $8}' | cut -b2- | sort | uniq)

echo -en "N indices:\t"
for ind in $nitrogen_indices; do
    echo -n "$ind "
done

echo -ne "\nunique Cq's:\t"
for cq in $uniq_freqs; do
    echo -n "$cq "
done

echo -e


for fil in efg.*; do
        if grep Cq $fil &>/dev/null; then
		echo -e "\n\nfile:\t$fil"
		for freq in $uniq_freqs; do
        		sfreq=$(echo $freq | sed 's/\./\\\./g')
			grep -E "$sfreq" $fil
		done
	fi	
done
