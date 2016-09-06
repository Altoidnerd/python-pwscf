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
job='relax'
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
np=8

structure="HMX"
structure_prefix="792929"
xcfunc='pbe'
note_str="default-conv-thr"
kp_str="gamma"
kp_mesh="gamma"

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


for ecut in 100; do
    fil_pref="$job.pbe-n-kjpaw.ec-$ecut-$note_str"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
    &CONTROL 
calculation ='$job'
title='$structure-scf-pbe-n-kjpaw-kp242-ec-$ecut-nofor-nostress-conv-em4'
prefix='scf.pbe-ec-$ecut-kp444.HMX-$hmxprefix-nofor.nostress'
pseudo_dir = '$HOME/.data/PSEUDOPOTENTIALS'
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
   6.5254000000    0.0000000000    0.0000000000
   0.0000000000   10.9702000000    0.0000000000
  -1.6011646355    0.0000000000    7.1737843500

ATOMIC_POSITIONS (crystal)
 N      -0.018730000     0.622810000     0.460810000
 O       0.271600000     0.719740000     0.436100000
 N       0.140100000     0.703130000     0.530900000
 N      -0.142700000     0.525430000     0.705700000
 O      -0.272400000     0.428710000     0.922550000
 N      -0.302100000     0.501430000     0.793600000
 O       0.140900000     0.747620000     0.683200000
 C      -0.190800000     0.615220000     0.553200000
 H      -0.318500000     0.590800000     0.463800000
 H      -0.215500000     0.695300000     0.603600000
 O      -0.464690000     0.560380000     0.738000000
 C      -0.021900000     0.565870000     0.281700000
 H      -0.157600000     0.527200000     0.239000000
 H      -0.003000000     0.624600000     0.188200000
 H       0.497000000    -0.124600000     0.688200000
 H       0.342400000    -0.027200000     0.739000000
 C       0.478100000    -0.065870000     0.781700000
 O       0.035310000    -0.060380000     1.238000000
 H       0.284500000    -0.195300000     1.103600000
 H       0.181500000    -0.090800000     0.963800000
 C       0.309200000    -0.115220000     1.053200000
 O       0.640900000    -0.247620000     1.183200000
 N       0.197900000    -0.001430000     1.293600000
 O       0.227600000     0.071290000     1.422550000
 N       0.357300000    -0.025430000     1.205700000
 N       0.640100000    -0.203130000     1.030900000
 O       0.771600000    -0.219740000     0.936100000
 N       0.481270000    -0.122810000     0.960810000
 H       0.003000000     0.375400000     0.811800000
 H       0.157600000     0.472800000     0.761000000
 C       0.021900000     0.434130000     0.718300000
 O       0.464690000     0.439620000     0.262000000
 H       0.215500000     0.304700000     0.396400000
 H       0.318500000     0.409200000     0.536200000
 C       0.190800000     0.384780000     0.446800000
 O      -0.140900000     0.252380000     0.316800000
 N       0.302100000     0.498570000     0.206400000
 O       0.272400000     0.571290000     0.077450000
 N       0.142700000     0.474570000     0.294300000
 N      -0.140100000     0.296870000     0.469100000
 O      -0.271600000     0.280260000     0.563900000
 N       0.018730000     0.377190000     0.539190000
 H       0.503000000     0.124600000     1.311800000
 H       0.657600000     0.027200000     1.261000000
 C       0.521900000     0.065870000     1.218300000
 O       0.964690000     0.060380000     0.762000000
 H       0.715500000     0.195300000     0.896400000
 H       0.818500000     0.090800000     1.036200000
 C       0.690800000     0.115220000     0.946800000
 O       0.359100000     0.247620000     0.816800000
 N       0.802100000     0.001430000     0.706400000
 O       0.772400000    -0.071290000     0.577450000
 N       0.642700000     0.025430000     0.794300000
 N       0.359900000     0.203130000     0.969100000
 O       0.228400000     0.219740000     1.063900000
 N       0.518730000     0.122810000     1.039190000
K_POINTS $kp_mesh


EOF

    $e " " >> debug.log
    $e "############$job LOG ENTRY############" >> debug.log 
    $e "$0 by $(whoami) running on $HOSTNAME " >> debug.log
    $e "working dir:\t$(pwd)" >> debug.log
    $e "$(date +%b%d-%T-%Y)" >> debug.log
    $e "$structure $structure_prefix" >>debug.log
    $e " ...running pw.x on $np cores ... ecut = $ecut" >> debug.log
    $e " " >> debug.log
    mpirun -n $np nice -n 19 $fil_bin < $infile > $outfile

done

echo -e " "
echo -e "$(date +%b%d-%T-%Y)" >> debug.log
echo -e "$0 has finished and is exiting now ..." >> debug.log

    &CONTROL 
calculation ='scf'
title='$structure-scf-pbe-n-kjpaw-kp242-ec-$ecut-nofor-nostress-conv-em4'
prefix='scf.pbe-ec-$ecut-kp444.HMX-$hmxprefix-nofor.nostress'
pseudo_dir = '$HOME/.data/PSEUDOPOTENTIALS'
outdir='$tmp_dir'
verbosity='high'
!tstress=.true.
!tprnfor = .true.
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
