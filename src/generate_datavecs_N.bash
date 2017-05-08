#!/bin/bash

#max=$(ls efgs/efg.*.out | grep -c .)
max=48


# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51 53 54  56



N1s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    1'|awk '{print $8}'; done)
echo "N1=["
for cq in $N1s; do
	echo -en "$cq,\n"
done
echo "]"

N3s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    3'|awk '{print $8}'; done)

echo "N3=["
for cq in $N3s; do
	echo -en "$cq,\n"
done
echo "]"

N4s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    4'|awk '{print $8}'; done)

echo "N4=["
for cq in $N4s; do
	echo -en "$cq,\n"
done
echo "]"

N6s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    6'|awk '{print $8}'; done)

echo "N6=["
for cq in $N6s; do
	echo -en "$cq,\n"
done
echo "]"


N23s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   23'|awk '{print $8}'; done)
echo "N23=["
for cq in $N23s; do
	echo -en "$cq,\n"
done
echo "]"

N25s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   25'|awk '{print $8}'; done)

echo "N25=["
for cq in $N25s; do
	echo -en "$cq,\n"
done
echo "]"

N26s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   26'|awk '{print $8}'; done)

echo "N26=["
for cq in $N26s; do
	echo -en "$cq,\n"
done
echo "]"

N28s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   28'|awk '{print $8}'; done)

echo "N28=["
for cq in $N28s; do
	echo -en "$cq,\n"
done
echo "]"


N37s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   37'|awk '{print $8}'; done)
echo "N37=["
for cq in $N37s; do
	echo -en "$cq,\n"
done
echo "]"

N39s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   39'|awk '{print $8}'; done)

echo "N39=["
for cq in $N39s; do
	echo -en "$cq,\n"
done
echo "]"

N40s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   40'|awk '{print $8}'; done)

echo "N40=["
for cq in $N40s; do
	echo -en "$cq,\n"
done
echo "]"

N42s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   42'|awk '{print $8}'; done)

echo "N42=["
for cq in $N42s; do
	echo -en "$cq,\n"
done
echo "]"



N51s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   51'|awk '{print $8}'; done)
echo "N51=["
for cq in $N51s; do
	echo -en "$cq,\n"
done
echo "]"

N53s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   53'|awk '{print $8}'; done)

echo "N53=["
for cq in $N53s; do
	echo -en "$cq,\n"
done
echo "]"

N54s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   54'|awk '{print $8}'; done)

echo "N54=["
for cq in $N54s; do
	echo -en "$cq,\n"
done
echo "]"

N56s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   56'|awk '{print $8}'; done)

echo "N56=["
for cq in $N56s; do
	echo -en "$cq,\n"
done
echo "]"


# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51 53 54  56


eta1s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    1'|awk '{print $11}'; done)
echo "eta1=["
for eta in $eta1s; do
	echo -en "$eta,\n"
done
echo "]"

eta3s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    3'|awk '{print $11}'; done)
echo "eta3=["
for eta in $eta3s; do
	echo -en "$eta,\n"
done
echo "]"


eta4s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    4'|awk '{print $11}'; done)
echo "eta4=["
for eta in $eta4s; do
	echo -en "$eta,\n"
done
echo "]"

eta6s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N    6'|awk '{print $11}'; done)
echo "eta6=["
for eta in $eta6s; do
	echo -en "$eta,\n"
done
echo "]"


eta23s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   23'|awk '{print $11}'; done)

echo "eta23=["
for eta in $eta23s; do
	echo -en "$eta,\n"
done
echo "]"

eta25s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   25'|awk '{print $11}'; done)
echo "eta25=["
for eta in $eta3s; do
	echo -en "$eta,\n"
done
echo "]"


eta26s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   26'|awk '{print $11}'; done)
echo "eta26=["
for eta in $eta26s; do
	echo -en "$eta,\n"
done
echo "]"

eta28s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   28'|awk '{print $11}'; done)
echo "eta28=["
for eta in $eta28s; do
	echo -en "$eta,\n"
done
echo "]"



eta37s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   37'|awk '{print $11}'; done)
echo "eta37=["
for eta in $eta37s; do
	echo -en "$eta,\n"
done
echo "]"

eta39s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   39'|awk '{print $11}'; done)
echo "eta39=["
for eta in $eta39s; do
	echo -en "$eta,\n"
done
echo "]"

eta40s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   40'|awk '{print $11}'; done)
echo "eta40=["
for eta in $eta40s; do
	echo -en "$eta,\n"
done
echo "]"

eta42s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   42'|awk '{print $11}'; done)
echo "eta42=["
for eta in $eta42s; do
	echo -en "$eta,\n"
done
echo "]"

# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51  53  54  56



eta51s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   51'|awk '{print $11}'; done)
echo "eta51=["
for eta in $eta51s; do
	echo -en "$eta,\n"
done
echo "]"

eta53s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   53'|awk '{print $11}'; done)
echo "eta53=["
for eta in $eta53s; do
	echo -en "$eta,\n"
done
echo "]"

eta54s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   54'|awk '{print $11}'; done)
echo "eta54=["
for eta in $eta54s; do
	echo -en "$eta,\n"
done
echo "]"

eta56s=$(for i in $(seq 1 $max); do grep "Cq" "efgs/efg.step-$i.out" | grep 'N   56'|awk '{print $11}'; done)
echo "eta56=["
for eta in $eta56s; do
	echo -en "$eta,\n"
done
echo "]"






e='echo -e'
infile=$( ls *.out)
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
