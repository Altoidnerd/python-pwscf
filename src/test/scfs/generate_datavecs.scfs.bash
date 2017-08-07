#!/bin/bash

max=$(ls "efg."*".out" | grep -c .)
echo $max

cl1s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl   1'|awk '{print $8}'; done)
echo "Cl1=["
for cq in $cl1s; do
	echo -en "$cq,\n"
done
echo "]"

cl12s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl  12'|awk '{print $8}'; done)

echo "Cl12=["
for cq in $cl12s; do
	echo -en "$cq,\n"
done
echo "]"

cl18s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl  18'|awk '{print $8}'; done)

echo "Cl18=["
for cq in $cl18s; do
	echo -en "$cq,\n"
done
echo "]"

cl24s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl  24'|awk '{print $8}'; done)

echo "Cl24=["
for cq in $cl24s; do
	echo -en "$cq,\n"
done
echo "]"

eta1s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl   1'|awk '{print $11}'; done)
echo "eta1=["
for eta in $eta1s; do
	echo -en "$eta,\n"
done
echo "]"

eta12s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl  12'|awk '{print $11}'; done)
echo "eta12=["
for eta in $eta12s; do
	echo -en "$eta,\n"
done
echo "]"


eta18s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl  18'|awk '{print $11}'; done)
echo "eta18=["
for eta in $eta18s; do
	echo -en "$eta,\n"
done
echo "]"

eta24s=$(for i in $(seq 0 $max); do grep "Cq" "efg.$i.out" | grep 'Cl  24'|awk '{print $11}'; done)
echo "eta24=["
for eta in $eta24s; do
	echo -en "$eta,\n"
done
echo "]"




e='echo -e'
infile="../md.out"
outfile="$infile.datafile.py"


$e -e '"""generating temperatures, kinetic energies, total energies"""'

$e "temperatures = ["

for item in $(cat $infile |grep temperature | awk '{print $3}' |  sed 's/set//g'|sed 's/\=//g'); do 
	$e "$item"','; 
done 

$e ']'  
$e -e "\n\n\n" 
$e "Ekins = [ " 



for item in $(cat $infile | grep 'kinetic energy ' | awk '{print $5}'); do 
	$e "$item"','; 
done

$e "]"

$e -e "\n\n\n"
$e 'Etots = ['

for item in $(cat $infile | grep Etot | awk '{print $6'}); 
	do $e "$item"','; 
done

$e ']'
$e 
