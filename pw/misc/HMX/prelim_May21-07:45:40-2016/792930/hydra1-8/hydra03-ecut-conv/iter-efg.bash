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
fil_bin="gipaw.x"
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
bin_dir="$HOME/espresso-5.3.0/bin"
np=8
hmxprefix="792830"

$e
$e "  executables directory: $bin_dir"
$e "  pseudo directory:      $pseudo_dir"
$e "  temporary directory:   $tmp_dir"
$e "  checking that needed directories and files exist..."
$e
$e " OK"
$e

for ecut in 70; do
    cat > efg.pbe.kp444.ec-$ecut.hmx-$hmxprefix.in  << EOF
&inputgipaw
        job = 'efg'
	prefix='scf.pbe-ec-70-kp444.HMX-792830-nofor.nostress'
        tmp_dir = './scratch/'
        verbosity = 'high'
        spline_ps = .true.
        q_gipaw     = 0.01	
        q_efg(1) = 2.044
/
EOF
    $e "########################LOG ENTRY########################" >> debug.log
    $e "$0 by $(whoami) running on $HOSTNAME " >> debug.log
    $e "$(date +%b%d-%T-%Y)" >> debug.log
    $e " ...running gipaw.x on $np cores ... ecut = $ecut" >> debug.log

    mpirun -n $np nice -n 19 $fil_bin < efg.pbe.kp444.ec-$ecut.hmx-$hmxprefix.in > efg.pbe.kp444.ec-$ecut.hmx-$hmxprefix.out

    $e "exited successful: ""$(date)"
    $e " " >> debug.log
done




