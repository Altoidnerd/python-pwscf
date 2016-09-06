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

# required executables and pseudopotentials
bin_list="pw.x"
structure="HMX"

hmxprefix="792827"

pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
bin_dir="$HOME/espresso-5.3.0/bin"
np=32

$e
$e "  executables directory: $bin_dir"
$e "  pseudo directory:      $pseudo_dir"
$e "  temporary directory:   $tmp_dir"
$e "  checking that needed directories and files exist..."
$e
$e " OK"
$e

for ecut in 180 220 260 300; do
    cat > scf.pbe.kp444.ec-$ecut.hmx-$hmxprefix.in << EOF
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
   6.5289000000    0.0000000000    0.0000000000
   0.0000000000   10.9875000000    0.0000000000
  -1.6043292838    0.0000000000    7.1679536577

ATOMIC_POSITIONS (crystal)
 N      -0.018440000     0.622930000     0.461910000
 O       0.272140000     0.719880000     0.437660000
 N       0.140210000     0.702810000     0.532030000
 N      -0.142820000     0.525120000     0.705750000
 O      -0.271800000     0.428390000     0.922310000
 N      -0.301700000     0.501610000     0.793390000
 O       0.141020000     0.747080000     0.683200000
 C      -0.190100000     0.615360000     0.554060000
 H      -0.316700000     0.591800000     0.465100000
 H      -0.214000000     0.694300000     0.604700000
 O      -0.464000000     0.560710000     0.738420000
 C      -0.022400000     0.565610000     0.282240000
 H      -0.154200000     0.523100000     0.239100000
 H      -0.007000000     0.624900000     0.188600000
 H       0.493000000    -0.124900000    -0.311400000
 H       0.345800000    -0.023100000    -0.260900000
 C       0.477600000    -0.065610000    -0.217760000
 O       0.036000000    -0.060710000     0.238420000
 H       0.286000000    -0.194300000     0.104700000
 H       0.183300000    -0.091800000    -0.034900000
 C       0.309900000    -0.115360000     0.054060000
 O       0.641020000    -0.247080000     0.183200000
 N       0.198300000    -0.001610000     0.293390000
 O       0.228200000     0.071610000     0.422310000
 N       0.357180000    -0.025120000     0.205750000
 N       0.640210000    -0.202810000     0.032030000
 O       0.772140000    -0.219880000    -0.062340000
 N       0.481560000    -0.122930000    -0.038090000
 H       0.007000000     0.375100000     0.811400000
 H       0.154200000     0.476900000     0.760900000
 C       0.022400000     0.434390000     0.717760000
 O       0.464000000     0.439290000     0.261580000
 H       0.214000000     0.305700000     0.395300000
 H       0.316700000     0.408200000     0.534900000
 C       0.190100000     0.384640000     0.445940000
 O      -0.141020000     0.252920000     0.316800000
 N       0.301700000     0.498390000     0.206610000
 O       0.271800000     0.571610000     0.077690000
 N       0.142820000     0.474880000     0.294250000
 N      -0.140210000     0.297190000     0.467970000
 O      -0.272140000     0.280120000     0.562340000
 N       0.018440000     0.377070000     0.538090000
 H       0.507000000     0.124900000     0.311400000
 H       0.654200000     0.023100000     0.260900000
 C       0.522400000     0.065610000     0.217760000
 O       0.964000000     0.060710000    -0.238420000
 H       0.714000000     0.194300000    -0.104700000
 H       0.816700000     0.091800000     0.034900000
 C       0.690100000     0.115360000    -0.054060000
 O       0.358980000     0.247080000    -0.183200000
 N       0.801700000     0.001610000    -0.293390000
 O       0.771800000    -0.071610000    -0.422310000
 N       0.642820000     0.025120000    -0.205750000
 N       0.359790000     0.202810000    -0.032030000
 O       0.227860000     0.219880000     0.062340000
 N       0.518440000     0.122930000     0.038090000
K_POINTS automatic
 4 4 4  1 1 1 

EOF
    $e " " >> debug.log
    $e "############SCF LOG ENTRY############" >> debug.log 
    $e "$0 by $(whoami) running on $HOSTNAME " >> debug.log
    $e "$(date +%b%d-%T-%Y)" >> debug.log
    $e "$structure $hmxprefix" >>debug.log
    $e " ...running pw.x on $np cores ... ecut = $ecut" >> debug.log
    $e " " >> debug.log

    mpirun -n $np nice -n 19 pw.x < scf.pbe.kp444.ec-$ecut.hmx-$hmxprefix.in > scf.pbe.kp444.ec-$ecut.hmx-$hmxprefix.out

done
    
    

