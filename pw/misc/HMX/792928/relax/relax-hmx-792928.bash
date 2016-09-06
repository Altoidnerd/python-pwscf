#!/bin/bash
#
#
# Copyright (c) 2016 altoidnerd                                                 
#################################################################################
#                      								#
# Permission is hereby granted, free of charge, to any person obtaining a 	#
# copy of this software and associated documentation files (the "Software"),	#
# to deal in the Software without restriction, including without limitation 	#
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 	#
# and/or sell copies of the Software, and to permit persons to whom the 	#
# Software is furnished to do so, subject to the following conditions:		#
#										#
# The above copyright notice and this permission notice shall be included 	#
# in all copies or substantial portions of the Software.			#
#										#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 	#
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 	#
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 	#
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 	#
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,	#
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE	#
# THE SOFTWARE.									#
#################################################################################

e="echo -e"

$e
$e "$cwd : starting $0 as $BASHPID"
$e

##### MAKE SURE YOU EDIT DATA_DIR ON ############
##### HIPERGATOR TO $HOME/scratch/.data/ ########
#		!MUY IMPORTANTO!		#
#						#
	    data_dir="$HOME/.data"
#						#
#						#
#################################################
#
#
##### PWSCF ENV ######
bin_dir="$HOME/espresso-5.3.0/bin"
fil_bin="pw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"
#
##### PWSCF PARAMS #####
job="relax"
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch/"
dft="pbe"
note_str="default-conv-thr"
kp_str="4x2x4"
kp_mesh="automatic"
k_points_pw="4 2 4 1 1 1"
ecutwfc=""
ecutrho=""
#
#### OS PARAMS ####
np=32
niceness=19
#
#### STRUCTURE PARAMS ####
structure="HMX"
structure_prefix="792928"

# create terse global log entry
$e "$(date): $0"		>> "$fil_log"
$e "$HOSTNAME:\n\t$PWD\n\n"	>> "$fil_log"

# user message
$e "bin_dir:\t:" 	"$bin_dir"
$e "fil_bin:\t" 	"$fil_bin"
$e "pseudo_dir"		"$pseudo_dir"
$e "tmp_dir:\t" 	"$tmp_dir"
$e "job:\t" 		"$job"
$e "np:\t" 		"$np"
$e "structure:\t"	"$structure\t$stucture_prefix"
$e "calculation:\t"	"$job"
$e "program:\t"		"$fil_bin"


# specify loop params and pw input file
for ecut in 80; do
    fil_pref="$job.$dft.ec-$ecut-$note_str"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
    &CONTROL 
calculation ='$job'
title='$structure-$job-$ecfunc-kp-$kp_str-ec-$ecut-$note_str'
prefix='$job.$dft.ec-$ecut.kp-$kp_str.$structure-$structure_prefix.np-$np.$note_str'
pseudo_dir = '$pseudo_dir'
outdir='$tmp_dir'
verbosity='high'
tstress=.true.
tprnfor = .true.
!forc_conv_thr=1.0d-4
!nstep=200
/

    &SYSTEM 
ibrav=0
celldm(1)=1.889726
nat=56
ntyp=4 
ecutwfc=$ecut
ecutrho=${ecut}0
/ 

    &ELECTRONS
mixing_beta=0.7
conv_thr =  1.0d-6 ! is default value
electron_maxstep=200
startingwfc='atomic+random'
/

   &IONS
trust_radius_max=0.2
/
    &CELL
cell_dynamics='bfgs'
/

ATOMIC_SPECIES
  N  14.0067  N.pbe-n-kjpaw_psl.1.0.0.UPF
  C  12.0110  C.pbe-n-kjpaw_psl.1.0.0.UPF
  H   1.0079  H.pbe-kjpaw_psl.1.0.0.UPF
  O  15.9994  O.pbe-n-kjpaw_psl.1.0.0.UPF


CELL_PARAMETERS (alat) 
   6.5245000000    0.0000000000    0.0000000000
   0.0000000000   11.0240000000    0.0000000000
  -1.6112148849    0.0000000000    7.1834224576

ATOMIC_POSITIONS (crystal)
 N      -0.018700000     0.622520000     0.461700000
 O       0.271100000     0.719410000     0.437300000
 N       0.140100000     0.702750000     0.531900000
 N      -0.142600000     0.524740000     0.705200000
 O      -0.271100000     0.428460000     0.921600000
 N      -0.301300000     0.500970000     0.793500000
 O       0.140500000     0.746850000     0.683500000
 C      -0.190400000     0.614580000     0.553900000
 H      -0.319700000     0.590500000     0.463500000
 H      -0.215200000     0.694900000     0.605500000
 O      -0.463100000     0.559920000     0.738600000
 C      -0.022000000     0.566130000     0.282600000
 H      -0.158200000     0.528200000     0.240000000
 H      -0.002000000     0.624600000     0.189000000
 H       0.498000000    -0.124600000     0.689000000
 H       0.341800000    -0.028200000     0.740000000
 C       0.478000000    -0.066130000     0.782600000
 O       0.036900000    -0.059920000     1.238600000
 H       0.284800000    -0.194900000     1.105500000
 H       0.180300000    -0.090500000     0.963500000
 C       0.309600000    -0.114580000     1.053900000
 O       0.640500000    -0.246850000     1.183500000
 N       0.198700000    -0.000970000     1.293500000
 O       0.228900000     0.071540000     1.421600000
 N       0.357400000    -0.024740000     1.205200000
 N       0.640100000    -0.202750000     1.031900000
 O       0.771100000    -0.219410000     0.937300000
 N       0.481300000    -0.122520000     0.961700000
 H       0.002000000     0.375400000     0.811000000
 H       0.158200000     0.471800000     0.760000000
 C       0.022000000     0.433870000     0.717400000
 O       0.463100000     0.440080000     0.261400000
 H       0.215200000     0.305100000     0.394500000
 H       0.319700000     0.409500000     0.536500000
 C       0.190400000     0.385420000     0.446100000
 O      -0.140500000     0.253150000     0.316500000
 N       0.301300000     0.499030000     0.206500000
 O       0.271100000     0.571540000     0.078400000
 N       0.142600000     0.475260000     0.294800000
 N      -0.140100000     0.297250000     0.468100000
 O      -0.271100000     0.280590000     0.562700000
 N       0.018700000     0.377480000     0.538300000
 H       0.502000000     0.124600000     1.311000000
 H       0.658200000     0.028200000     1.260000000
 C       0.522000000     0.066130000     1.217400000
 O       0.963100000     0.059920000     0.761400000
 H       0.715200000     0.194900000     0.894500000
 H       0.819700000     0.090500000     1.036500000
 C       0.690400000     0.114580000     0.946100000
 O       0.359500000     0.246850000     0.816500000
 N       0.801300000     0.000970000     0.706500000
 O       0.771100000    -0.071540000     0.578400000
 N       0.642600000     0.024740000     0.794800000
 N       0.359900000     0.202750000     0.968100000
 O       0.228900000     0.219410000     1.062700000
 N       0.518700000     0.122520000     1.038300000
K_POINTS $kp_mesh
$k_points_pw

EOF

# create verbose log entry in ./debug.log
    delim='######################'
    job_upper="$(echo $job | tr '[:lower:]' '[:upper:]')"
    $e  					>> debug.log
    $e "$delim $job_upper LOG ENTRY $delim"	>> debug.log 
    $e "$(date +%b%d-%T-%Y)" 			>> debug.log	
    $e "$0 ($BASHPID) running on $HOSTNAME"  	>> debug.log
    $e "user:\t\t 	$USER"	 		>> debug.log	
    $e "cwd:\t		$(pwd)"			>> debug.log
    $e "fil_bin:\t	$fil_bin"		>> debug.log
    $e "infile:\t\t	$infile"		>> debug.log
    $e "outfile:\t	$outfile"		>> debug.log
    $e "pseudo_dir:\t	$pseudo_dir"		>> debug.log
    $e "tmp_dir:\t	$tmp_dir"		>> debug.log
    $e "job/calc:\t	${job}/${calc}"		>> debug.log
    $e "nproc:\t\t	$np cores"		>> debug.log
    $e "ecutwfc:\t	$ecut Ry"		>> debug.log
    $e "ecutrho:\t	${ecut}0 Ry"		>> debug.log
    $e "k_points:\t 	$k_points_pw"		>> debug.log
    $e "conv_thr:\t	default"		>> debug.log
    $e "data dir:\t	$data_dir" 		>> debug.log
    $e

# do the calculation
    mpirun -n "$np" nice -n "$niceness" "$fil_bin" < "$infile" >> "$outfile"

done

# exit message
$e 
$e "$(date +%b%d-%T-%Y)"			>> debug.log
$e "$0 has finished and is exiting now ..." 	>> debug.log
$e

# bye

