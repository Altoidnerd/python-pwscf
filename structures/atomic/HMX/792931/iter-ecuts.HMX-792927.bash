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

hmxprefix="792829"

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

for ecut in 60 100 140 180 220 260 300; do
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
   6.5334000000    0.0000000000    0.0000000000
   0.0000000000   10.9419000000    0.0000000000
  -1.5879953132    0.0000000000    7.1683124440

ATOMIC_POSITIONS (crystal)
 N       0.981570000     0.623000000     0.460650000
 O       1.272030000     0.720210000     0.436000000
 N       1.140380000     0.703340000     0.530410000
 N       0.857340000     0.525710000     0.706230000
 O       0.727280000     0.428860000     0.923080000
 N       0.697210000     0.502080000     0.793450000
 O       1.141430000     0.747950000     0.683110000
 C       0.808820000     0.615680000     0.552870000
 H       0.681500000     0.590900000     0.463300000
 H       0.783700000     0.696000000     0.602800000
 O       0.534690000     0.560960000     0.737680000
 C       0.978000000     0.565390000     0.280970000
 H       0.842500000     0.526400000     0.240700000
 H       0.995400000     0.624000000     0.186400000
 H       0.495400000    -0.124000000    -0.313600000
 H       0.342500000    -0.026400000    -0.259300000
 C       0.478000000    -0.065390000    -0.219030000
 O       0.034690000    -0.060960000     0.237680000
 H       0.283700000    -0.196000000     0.102800000
 H       0.181500000    -0.090900000    -0.036700000
 C       0.308820000    -0.115680000     0.052870000
 O       0.641430000    -0.247950000     0.183110000
 N       0.197210000    -0.002080000     0.293450000
 O       0.227280000     0.071140000     0.423080000
 N       0.357340000    -0.025710000     0.206230000
 N       0.640380000    -0.203340000     0.030410000
 O       0.772030000    -0.220210000    -0.064000000
 N       0.481570000    -0.123000000    -0.039350000
 H       1.004600000     0.376000000     0.813600000
 H       1.157500000     0.473600000     0.759300000
 C       1.022000000     0.434610000     0.719030000
 O       1.465310000     0.439040000     0.262320000
 H       1.216300000     0.304000000     0.397200000
 H       1.318500000     0.409100000     0.536700000
 C       1.191180000     0.384320000     0.447130000
 O       0.858570000     0.252050000     0.316890000
 N       1.302790000     0.497920000     0.206550000
 O       1.272720000     0.571140000     0.076920000
 N       1.142660000     0.474290000     0.293770000
 N       0.859620000     0.296660000     0.469590000
 O       0.727970000     0.279790000     0.564000000
 N       1.018430000     0.377000000     0.539350000
 H       0.504600000     0.124000000     0.313600000
 H       0.657500000     0.026400000     0.259300000
 C       0.522000000     0.065390000     0.219030000
 O       0.965310000     0.060960000    -0.237680000
 H       0.716300000     0.196000000    -0.102800000
 H       0.818500000     0.090900000     0.036700000
 C       0.691180000     0.115680000    -0.052870000
 O       0.358570000     0.247950000    -0.183110000
 N       0.802790000     0.002080000    -0.293450000
 O       0.772720000    -0.071140000    -0.423080000
 N       0.642660000     0.025710000    -0.206230000
 N       0.359620000     0.203340000    -0.030410000
 O       0.227970000     0.220210000     0.064000000
 N       0.518430000     0.123000000     0.039350000
K_POINTS {automatic}
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