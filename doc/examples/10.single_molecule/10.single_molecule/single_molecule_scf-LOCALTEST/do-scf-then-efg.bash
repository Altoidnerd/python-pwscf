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
################################################
#
#
##### PWSCF ENV ######
bin_dir="$HOME/espresso-5.3.0/bin"
fil_bin="pw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"
#
##### PWSCF PARAMS #####
job="scf"
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch/"
dft="pbe"
note_str="default-conv-thr"
kp_str="222"
kp_mesh="automatic"
k_points_pw="2 2 2 1 1 1"
ecutwfc=""
ecutrho=""
#
#### OS PARAMS ####
np=4
niceness=19
#
#### STRUCTURE PARAMS ####
structure="pcl2b"
structure_prefix="139"

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

prefix='001'
# specify loop params and pw input file
for ecut in 100; do
    fil_pref="$job.$prefix"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
    &CONTROL 
calculation ='$job'
title='$structure-$dft-$job-kp-$kp_str-ec-$ecut-$note_str'
prefix='$prefix'
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
nat=12
ntyp=3 
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
C    12.0110   C.pbe-n-kjpaw_psl.1.0.0.UPF
Cl   35.4527  Cl.pbe-n-kjpaw_psl.1.0.0.UPF
H    1.0079    H.pbe-kjpaw_psl.1.0.0.UPF

CELL_PARAMETERS (alat) 
  20.000000000    0.0000000000    0.0000000000
   0.000000000   20.0000000000    0.0000000000
   0.000000000    0.0000000000   20.0000000000

ATOMIC_POSITIONS (crystal)
C     0.50029811  0.49912275  0.43101635
C     0.50015863  0.56029247  0.46437584
C     0.49986178  0.56119159  0.53405942
C     0.49970189  0.50087725  0.56898365
C     0.49984137  0.43970753  0.53562416
C     0.50013822  0.43880841  0.46594058
H     0.50053083  0.60706304  0.43655014
H     0.50003945  0.60872864  0.56055585
H     0.49946917  0.39293696  0.56344986
H     0.49996055  0.39127137  0.43944415
Cl    0.50065351  0.49797664  0.34377231
Cl    0.49934649  0.50202336  0.65622769

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
    sleep 10

# do another
    fil_pref="efg.$dft.ec-$ecut-$note_str"
    infile="$fil_pref.in"
    outfile="$fil_pref.out"
    cat > $infile << EOF
&inputgipaw
        job='$job'
        prefix='$prefix'
        tmp_dir='$tmp_dir'
        verbosity='high'
  !     spline_ps=.true.
        q_gipaw=0.01
        q_efg(2)=-8.165
/
EOF

    mpirun -n "$np" nice -n "$niceness" gipaw.x < "$infile" >> "$outfile"


done




# exit message
$e 
$e "$(date +%b%d-%T-%Y)"			>> debug.log
$e "$0 has finished and is exiting now ..." 	>> debug.log
$e

# bye
