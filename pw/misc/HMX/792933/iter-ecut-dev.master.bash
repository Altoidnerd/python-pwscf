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
#
#
#
# run from directory where this script is
# cd `echo $0 | sed 's/\(.*\)\/.*/\1/'` # extract pathname
#
#


example_dir=`pwd`

# check whether echo has the -e option
e="echo -e"

$e
$e "$example_dir : starting"
$e

$e  
$e "...setting the needed environment variables..."
$e

#. ./environment_variables

$e "done."
$e

#####PWSCF ENV#####
bin_dir="$HOME/espresso-5.3.0/bin"
fil_bin="pw.x"
job='scf'
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
np=8

structure="HMX"
structure_prefix="792934"
xcfunc='pbe'
note_str="default-conv-thr"
kp_str="444"
kp_mesh="automatic"
k_points_pw="4 4 4 1 1 1"

$e "$(date): BEGIN TEST\n"
$e
$e "bin_dir:\t:" 	"$bin_dir"
$e "fil_bin:\t" 	"$fil_bin"
$e "pseudo_dir"		"$pseudo_dir"
$e "tmp_dir:\t" 	"$tmp_dir"
$e "job:\t" 		"$job"
$e "np:\t" 		"$np"
$e 
$e " OK"
$e


for ecut in 100 140 180 220 260 300 360; do
    fil_pref="$job.pbe-n-kjpaw.ec-$ecut-$note_str"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
    &CONTROL 
calculation ='$job'
title='$structure-scf-$ecfunc-kp-$kp_str-ec-$ecut-$note_str'
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
   6.5288000000    0.0000000000    0.0000000000
   0.0000000000   10.8862000000    0.0000000000
  -1.5697221212    0.0000000000    7.1603586937

ATOMIC_POSITIONS (crystal)
 N      -0.018520000     0.623320000     0.459770000
 O       0.272710000     0.720470000     0.434930000
 N       0.140780000     0.703740000     0.529560000
 N      -0.143010000     0.526410000     0.706860000
 O      -0.274380000     0.429070000     0.923630000
 N      -0.303930000     0.502440000     0.793550000
 O       0.141780000     0.748700000     0.682660000
 C      -0.191690000     0.616340000     0.552220000
 H      -0.320100000     0.590800000     0.462000000
 H      -0.217400000     0.698100000     0.602000000
 O      -0.466690000     0.561420000     0.737050000
 C      -0.021860000     0.565150000     0.280130000
 H      -0.158100000     0.526700000     0.240000000
 H      -0.003900000     0.624100000     0.185500000
 H       0.496100000    -0.124100000    -0.314500000
 H       0.341900000    -0.026700000    -0.260000000
 C       0.478140000    -0.065150000    -0.219870000
 O       0.033310000    -0.061420000     0.237050000
 H       0.282600000    -0.198100000     0.102000000
 H       0.179900000    -0.090800000    -0.038000000
 C       0.308310000    -0.116340000     0.052220000
 O       0.641780000    -0.248700000     0.182660000
 N       0.196070000    -0.002440000     0.293550000
 O       0.225620000     0.070930000     0.423630000
 N       0.356990000    -0.026410000     0.206860000
 N       0.640780000    -0.203740000     0.029560000
 O       0.772710000    -0.220470000    -0.065070000
 N       0.481480000    -0.123320000    -0.040230000
 H       0.003900000     0.375900000     0.814500000
 H       0.158100000     0.473300000     0.760000000
 C       0.021860000     0.434850000     0.719870000
 O       0.466690000     0.438580000     0.262950000
 H       0.217400000     0.301900000     0.398000000
 H       0.320100000     0.409200000     0.538000000
 C       0.191690000     0.383660000     0.447780000
 O      -0.141780000     0.251300000     0.317340000
 N       0.303930000     0.497560000     0.206450000
 O       0.274380000     0.570930000     0.076370000
 N       0.143010000     0.473590000     0.293140000
 N      -0.140780000     0.296260000     0.470440000
 O      -0.272710000     0.279530000     0.565070000
 N       0.018520000     0.376680000     0.540230000
 H       0.503900000     0.124100000     0.314500000
 H       0.658100000     0.026700000     0.260000000
 C       0.521860000     0.065150000     0.219870000
 O       0.966690000     0.061420000    -0.237050000
 H       0.717400000     0.198100000    -0.102000000
 H       0.820100000     0.090800000     0.038000000
 C       0.691690000     0.116340000    -0.052220000
 O       0.358220000     0.248700000    -0.182660000
 N       0.803930000     0.002440000    -0.293550000
 O       0.774380000    -0.070930000    -0.423630000
 N       0.643010000     0.026410000    -0.206860000
 N       0.359220000     0.203740000    -0.029560000
 O       0.227290000     0.220470000     0.065070000
 N       0.518520000     0.123320000     0.040230000
K_POINTS $kp_mesh
$k_points_pw

EOF

    $e "############$job_upper LOG ENTRY############" >> debug.log 
    $e "$(date +%b%d-%T-%Y)" 			>> debug.log	
    $e "$0 by $(whoami) running on $HOSTNAME "  >> debug.log
    $e "fil_bin:\t  $fil_bin"			>> debug.log
    $e "infile:\t   $infile"			>> debug.log
    $e "outfile:\t  $outfile"			>> debug.log
    $e "pseudo_dir  $pseudo_dir"		>> debug.log
    $e "tmp_dir:\t  $tmp_dir"			>> debug.log
    $e "job:\t      $job"			>> debug.log			
    $e "nproc:\t    $np cores"			>> debug.log
    $e "k_points:\t $k_points_pw"		>> debug.log
    $e "ecutwfc:\t  $ecut Ry"			>> debug.log
    $e "ecutrho:\t  ${ecut}0 Ry"		>> debug.log
    $e "conv_thr:\t default"			>> debug.log
    $e "cwd:\t      $(pwd)"			>> debug.log
    $e "infile:\t   $infile" 			>> debug.log
    $e "outfile:\t  $outfile" 			>> debug.log
    $e  					>> debug.log
   
     mpirun -n $np nice -n 19 $fil_bin < $infile > $outfile


done

echo -e " "
echo -e "$(date +%b%d-%T-%Y)" >> debug.log
echo -e "$0 has finished and is exiting now ..." >> debug.log
