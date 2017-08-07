#!/bin/bash


for i in $(seq 0 2001); do 
	ls scf-$i.efg.magres 2>&1|grep "No such"|cut -b 24-|cut -b -4 | sed "s/\.//g";
done
