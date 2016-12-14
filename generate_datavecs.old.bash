#!/usr/bin/env bash

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

for i in '   1' '  12' '  18' '  24'; do 
  $e $($e 'Cl'$i'=['|sed s/\ //g)
  for thing in $(grep Cq efgs/* | grep "Cl$i" | awk '{print $9}'); do
    $e "$thing"','
  done
  $e ']'
done



for i in '   1' '  12' '  18' '  24'; do 
  $e $($e 'eta'$i'=['|sed s/\ //g)
  for thing in $(grep Cq efgs/* | grep "Cl$i" | awk '{print $12}'); do
    $e "$thing"','
  done
  $e ']'
done


$e -e "\"\"\"\n\n\n\t... goodbye.\"\"\""
