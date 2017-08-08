

# get lattice vectors from scf.in
get_lattice_vectors() {
	cat $1 | grep CELL_PARAM --color=never -A3 | tail -n3
}

getlv(){
	get_lattice_vectors $1
}


# from scf.in or md.out
# eg:
# getpos md.out 24
#
get_atomic_positions() {
	fstring="--color=never ATOMIC_POS -A$2"
	cat $1 | grep $fstring
}

getpos() { 
	get_atomic_positions $1 $2 
}




