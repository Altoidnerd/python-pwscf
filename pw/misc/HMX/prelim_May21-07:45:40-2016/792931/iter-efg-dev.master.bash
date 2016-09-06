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
fil_bin="gipaw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"


##### PWSCF PARAMS #####
job='efg'
job_upper="$(echo $job | tr '[:lower:]' '[:upper:]')"
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
xcfunc='pbe'
note_str="default-conv-thr"
kp_str="444"
kp_mesh="automatic"
k_points_pw="4 4 4 1 1 1"

#### OS PARAMS ####
np=8
niceness=19

#### STRUCTURE PARAMS ####
structure="HMX"
structure_prefix="792931"


$e "$(date): $0\n"              >> "$fil_log"
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


for ecut in 140; do
    fil_pref="$job.pbe.ec-$ecut-$note_str"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
&inputgipaw
        job = '$job'
        prefix='$job.$xcfunc.ec-$ecut.kp-$kp_str.$structure-$structure_prefix.np-$np.$note_str'
        tmp_dir = '$tmp_dir'
        verbosity = 'high'
        spline_ps = .true.
        q_gipaw     = 0.01	
        q_efg(1) = 2.044
/

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

   
