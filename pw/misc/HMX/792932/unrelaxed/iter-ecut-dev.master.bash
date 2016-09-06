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

cwd=`pwd`

# check whether echo has the -e option
e="echo -e"

$e
$e "$cwd : starting $0"
$e

$e  
$e "...setting the needed environment variables..."
$e

#. ./environment_variables

$e "done."
$e

##### MAKE SURE YOU EDIT DATA_DIR ON ############
##### HIPERGATOR TO $HOME/scratch/.data/ ########
#		!MUY IMPORTANTO!		#
#						#
	    data_dir="$HOME/.data"
#						#
#						#
################################################

##### PWSCF ENV ######
bin_dir="$HOME/espresso-5.3.0/bin"
fil_bin="pw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"


##### PWSCF PARAMS #####
job='scf'
job_upper="$(echo $job | tr '[:lower:]' '[:upper:]')"
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
xcfunc='pbe'
note_str="default-conv-thr"
kp_str="444"
kp_mesh='automatic'
k_points_pw="4 4 4 1 1 1"

#### OS PARAMS ####
np=8
niceness=19

#### STRUCTURE PARAMS ####
structure="HMX"
structure_prefix="792932"


$e "$(date): $0"		>> "$fil_log"
$e "$HOSTNAME:\n\t$PWD\n\n"	>> "$fil_log"
$e
$e "bin_dir:\t:" 	"$bin_dir"
$e "fil_bin:\t" 	"$fil_bin"
$e "pseudo_dir"		"$pseudo_dir"
$e "tmp_dir:\t" 	"$tmp_dir"
$e "job:\t" 		"$job"
$e "np:\t" 		"$np"
$e "structure:\t"	"$structure\t$stucture_prefix"
$e "calculation:\t"	"$job"
$e "program:\t"		"$fil_bin"


for ecut in 60 100 140 180; do
    fil_pref="$job.pbe.ec-$ecut-$note_str"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
    &CONTROL 
calculation ='$job'
title='$structure-$job-$ecfunc-kp-$kp_str-ec-$ecut-$note_str'
prefix='$job.$xcfunc.ec-$ecut.kp-$kp_str.$structure-$structure_prefix.np-$np.$note_str'
pseudo_dir = '$pseudo_dir'
outdir='$tmp_dir'
verbosity='high'
tstress=.true.
tprnfor = .true.
!forc_conv_thr=1.0d-4
nstep=200
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
!conv_thr =  1.0d-4
electron_maxstep=200
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
   6.5206000000    0.0000000000    0.0000000000
   0.0000000000   10.9123000000    0.0000000000
  -1.5844312374    0.0000000000    7.1664382997

ATOMIC_POSITIONS (crystal)
 N      -0.018800000     0.623100000     0.460000000
 O       0.272300000     0.720030000     0.435100000
 N       0.140600000     0.703630000     0.530200000
 N      -0.143100000     0.526230000     0.706400000
 O      -0.274000000     0.429010000     0.923090000
 N      -0.303200000     0.501920000     0.793700000
 O       0.141500000     0.748370000     0.682800000
 C      -0.191200000     0.615900000     0.552800000
 H      -0.320200000     0.590800000     0.462700000
 H      -0.216500000     0.697400000     0.603000000
 O      -0.466020000     0.560910000     0.737400000
 C      -0.021800000     0.565600000     0.280700000
 H      -0.157900000     0.527100000     0.238000000
 H      -0.002000000     0.624400000     0.187000000
 H       0.498000000    -0.124400000    -0.313000000
 H       0.342100000    -0.027100000    -0.262000000
 C       0.478200000    -0.065600000    -0.219300000
 O       0.033980000    -0.060910000     0.237400000
 H       0.283500000    -0.197400000     0.103000000
 H       0.179800000    -0.090800000    -0.037300000
 C       0.308800000    -0.115900000     0.052800000
 O       0.641500000    -0.248370000     0.182800000
 N       0.196800000    -0.001920000     0.293700000
 O       0.226000000     0.070990000     0.423090000
 N       0.356900000    -0.026230000     0.206400000
 N       0.640600000    -0.203630000     0.030200000
 O       0.772300000    -0.220030000    -0.064900000
 N       0.481200000    -0.123100000    -0.040000000
 H       0.002000000     0.375600000     0.813000000
 H       0.157900000     0.472900000     0.762000000
 C       0.021800000     0.434400000     0.719300000
 O       0.466020000     0.439090000     0.262600000
 H       0.216500000     0.302600000     0.397000000
 H       0.320200000     0.409200000     0.537300000
 C       0.191200000     0.384100000     0.447200000
 O      -0.141500000     0.251630000     0.317200000
 N       0.303200000     0.498080000     0.206300000
 O       0.274000000     0.570990000     0.076910000
 N       0.143100000     0.473770000     0.293600000
 N      -0.140600000     0.296370000     0.469800000
 O      -0.272300000     0.279970000     0.564900000
 N       0.018800000     0.376900000     0.540000000
 H       0.502000000     0.124400000     0.313000000
 H       0.657900000     0.027100000     0.262000000
 C       0.521800000     0.065600000     0.219300000
 O       0.966020000     0.060910000    -0.237400000
 H       0.716500000     0.197400000    -0.103000000
 H       0.820200000     0.090800000     0.037300000
 C       0.691200000     0.115900000    -0.052800000
 O       0.358500000     0.248370000    -0.182800000
 N       0.803200000     0.001920000    -0.293700000
 O       0.774000000    -0.070990000    -0.423090000
 N       0.643100000     0.026230000    -0.206400000
 N       0.359400000     0.203630000    -0.030200000
 O       0.227700000     0.220030000     0.064900000
 N       0.518800000     0.123100000     0.040000000
K_POINTS $kp_mesh
$k_points_pw


EOF

delim='######################'

    $e  					>> debug.log
    $e "$delim $job_upper LOG ENTRY $delim"	>> debug.log 
    $e "$(date +%b%d-%T-%Y)" 			>> debug.log	
    $e "$0 by $(whoami)	running on $HOSTNAME "  >> debug.log
    $e "fil_bin:\t	$fil_bin"		>> debug.log
    $e "infile:\t\t	$infile"		>> debug.log
    $e "outfile:\t	$outfile"		>> debug.log
    $e "pseudo_dir:\t	$pseudo_dir"		>> debug.log
    $e "tmp_dir:\t	$tmp_dir"		>> debug.log
    $e "job:\t\t	$job"			>> debug.log
    $e "nproc:\t\t	$np cores"		>> debug.log
    $e "ecutwfc:\t	$ecut Ry"		>> debug.log
    $e "ecutrho:\t	${ecut}0 Ry"		>> debug.log
    $e "k_points:\t 	$k_points_pw"		>> debug.log
    $e "conv_thr:\t	default"		>> debug.log
    $e "cwd:\t\t	$(pwd)"			>> debug.log
    $e "infile:\t\t   	$infile" 		>> debug.log
    $e "outfile:\t	$outfile" 		>> debug.log
    $e  					>> debug.log
   
     mpirun -n $np nice -n $niceness $fil_bin < $infile > "$outfile"
done

    $e 
    $e "$(date +%b%d-%T-%Y)" >> debug.log
    $e "$0 has finished and is exiting now ..." >> debug.log
    $e

   
