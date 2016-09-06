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
note_str="300K"
kp_str="444"
kp_mesh='automatic'
k_points_pw="4 4 4 1 1 1"

#### OS PARAMS ####
np=8
niceness=19

#### STRUCTURE PARAMS ####
structure="HMX"
structure_prefix="792930"


$e "$(date): $0\n"		>> "$fil_log"
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
   6.5255000000    0.0000000000    0.0000000000
   0.0000000000   11.0369000000    0.0000000000
  -1.6151857792    0.0000000000    7.1846830757

ATOMIC_POSITIONS (crystal)
 N      -0.018510000     0.622390000     0.461900000
 O       0.270700000     0.719420000     0.437400000
 N       0.139800000     0.702700000     0.531800000
 N      -0.142400000     0.524520000     0.705100000
 O      -0.270400000     0.428390000     0.921760000
 N      -0.300900000     0.500880000     0.793500000
 O       0.140600000     0.746710000     0.683900000
 C      -0.190300000     0.614340000     0.553800000
 H      -0.316900000     0.590700000     0.465100000
 H      -0.214600000     0.692900000     0.604400000
 O      -0.462770000     0.559850000     0.739100000
 C      -0.021900000     0.566240000     0.282900000
 H      -0.157600000     0.527600000     0.241000000
 H      -0.004000000     0.624700000     0.189300000
 H       0.496000000    -0.124700000     0.689300000
 H       0.342400000    -0.027600000     0.741000000
 C       0.478100000    -0.066240000     0.782900000
 O       0.037230000    -0.059850000     1.239100000
 H       0.285400000    -0.192900000     1.104400000
 H       0.183100000    -0.090700000     0.965100000
 C       0.309700000    -0.114340000     1.053800000
 O       0.640600000    -0.246710000     1.183900000
 N       0.199100000    -0.000880000     1.293500000
 O       0.229600000     0.071610000     1.421760000
 N       0.357600000    -0.024520000     1.205100000
 N       0.639800000    -0.202700000     1.031800000
 O       0.770700000    -0.219420000     0.937400000
 N       0.481490000    -0.122390000     0.961900000
 H       0.004000000     0.375300000     0.810700000
 H       0.157600000     0.472400000     0.759000000
 C       0.021900000     0.433760000     0.717100000
 O       0.462770000     0.440150000     0.260900000
 H       0.214600000     0.307100000     0.395600000
 H       0.316900000     0.409300000     0.534900000
 C       0.190300000     0.385660000     0.446200000
 O      -0.140600000     0.253290000     0.316100000
 N       0.300900000     0.499120000     0.206500000
 O       0.270400000     0.571610000     0.078240000
 N       0.142400000     0.475480000     0.294900000
 N      -0.139800000     0.297300000     0.468200000
 O      -0.270700000     0.280580000     0.562600000
 N       0.018510000     0.377610000     0.538100000
 H       0.504000000     0.124700000     1.310700000
 H       0.657600000     0.027600000     1.259000000
 C       0.521900000     0.066240000     1.217100000
 O       0.962770000     0.059850000     0.760900000
 H       0.714600000     0.192900000     0.895600000
 H       0.816900000     0.090700000     1.034900000
 C       0.690300000     0.114340000     0.946200000
 O       0.359400000     0.246710000     0.816100000
 N       0.800900000     0.000880000     0.706500000
 O       0.770400000    -0.071610000     0.578240000
 N       0.642400000     0.024520000     0.794900000
 N       0.360200000     0.202700000     0.968200000
 O       0.229300000     0.219420000     1.062600000
 N       0.518510000     0.122390000     1.038100000
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
