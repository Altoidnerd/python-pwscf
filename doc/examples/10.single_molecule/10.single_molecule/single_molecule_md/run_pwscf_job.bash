#!/bin/bash -l
#SBATCH -N 8
#SBATCH -p regular
#SBATCH -t 48:00:00
#SBATCH -L SCRATCH
#SBATCH --mem-per-cpu 256

module load espresso


#export OMP_NUM_THREADS=1 # only needed for hybrid MPI/OpenMP codes built with "-qopenmp" flag

cd $SLURM_SUBMIT_DIR


# Copyright (c) 2016 Allen Majewski                                                 
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



source environment_variables.bash
source input_cards.bash


# create terse global log entry
$e "########LOG ENTRY########\n"		>> "$fil_log"
$e "$(date): $0\n"             			>> "$fil_log"
$e "WD:\t$this_dir_pwd\n"			>> "$fil_log"
$e "$HOSTNAME:\n\t$PWD\n" 			>> "$fil_log"

# start md

prefix="tempw-$tempw-dt$dt.$structure-$structure_prefix-$note_str"
infile="md.$prefix.in"
outfile="md.$prefix.out"

cat > $infile << EOF
    &CONTROL
calculation  = '$calculation'
restart_mode = '$restart_mode'
prefix       ='$prefix'
pseudo_dir   = '$pseudo_dir'
outdir       ='$outdir'
dt           = $dt
tstress      =$tstress
tprnfor      =.true.
!forc_conv_thr=1.0d-4
verbosity    = 'high'
nstep        = $nstep
!max_seconds  = $max_seconds
/

&system
    ibrav=0
    celldm(1)=1.889726
    nat=$nat
    ntyp=$ntyp
    ecutwfc=$ecutwfc
    ecutrho=$ecutrho
    spline_ps=$spline_ps
    nosym=$nosym
/

&electrons

    electron_maxstep  = $electron_maxstep
!   scf_must_converge = .true.
    conv_thr          = $conv_thr
!   adaptive_thr      = 1.D-6
!   conv_thr_init     = 1.D-3

    mixing_mode       = 'plain'
    mixing_beta       = 0.7
!   mixing_ndim       = 8
!   mixing_fixed_ns   = 0
!
    diagonalization   = 'david'
!   ortho_para        = 0
    diago_thr_init    = 1.D-4
!   diago_cg_maxiter  = 2?
!   diago_david_ndim  = 4
!   diago_full_ac     = .false.
!
!
!   efield            = 0.D0
!   efield_cart(i)    = (0.D0, 0.D0, 0.D0) ! need lelfield=.true., K_POINTS automatic
!   startingpot       = 'atomic'
!   startingwfc       = 'atomic+random'
!   tqr               = .false.
!
/


&ions
    ion_dynamics      = 'verlet'
    ion_positions     = 'default'
!   pot_extrapolation = 'atomic'
!   wfc_extrapolation = 'none'
!   remove_rigid_rot  = .false.
!
!-------------------------------------------
!    !!!Molecular Dynamics only!!!         -
!-------------------------------------------
    ion_temperature   = 'initial'
    tempw             = $tempw
    tolp              = 100.D0
    delta_t           = 1.D0
    nraise            = 1
!    refold_pos
!------------------------------------------
!    !!!BFGS only!!!
!------------------------------------------
!   upscale           = 100.D0
!   bfgs_ndim         = 1
    trust_radius_max  = 0.8D0
    trust_radius_min  = 1.D-3
    trust_radius_ini  = 0.5D0

!   w_1               = 0.01D0
!   w_2               = 0.5D0
!-------------------------------------------

/

&cell
!
    cell_dynamics     = 'bfgs'
!   press             = 0.D0
!   wmass             = !! fictitious cell mass
!                default:0.75*Tot_Mass/pi**2 for Parrinello-Rahman MD; 0.75*Tot_Mass/pi**2/Omega**(2/3) for Wentzcovitch MD
!   cell_factor       = 1.2D0
!   press_conv_thr    = 0.5D0
!   cell_dofree       = 'all'
/

ATOMIC_SPECIES
$atomic_species

CELL_PARAMETERS $cell_parameters_opt
$cell_parameters

ATOMIC_POSITIONS $atomic_positions_opt
$atomic_positions

K_POINTS $k_points_opt
$k_points


EOF

# create verbose log entry in ./debug.log
    delim='######################'
    job_upper="$(echo $job | tr '[:lower:]' '[:upper:]')"
    $e "\n"                           		 >> debug.log
    $e "$delim $job_upper LOG ENTRY $delim\n"    >> debug.log
    $e "$(date +%b%d-%T-%Y)\n"                   >> debug.log
    $e "$0 ($BASHPID) running on $HOSTNAME\n"    >> debug.log
    $e "user:\t\t       $USER\n"                 >> debug.log
    $e "cwd:\t          $(pwd)\n"                >> debug.log
    $e "fil_bin:\t      $fil_bin\n"              >> debug.log
    $e "infile:\t\t     $infile\n"               >> debug.log
    $e "outfile:\t      $outfile\n"              >> debug.log
    $e "pseudo_dir:\t   $pseudo_dir\n"           >> debug.log
    $e "tmp_dir:\t      $tmp_dir\n"              >> debug.log
    $e "calculation:\t  $calculation\n"  	 >> debug.log
    $e "nproc:\t\t      $np cores\n"             >> debug.log
    $e "ecutwfc:\t      $ecutwfc Ry\n"           >> debug.log
    $e "ecutrho:\t      $ecutrho Ry\n"           >> debug.log
    $e "k_points:\t     $k_points\n"             >> debug.log
    $e "conv_thr:\t     $conv_thr\n"             >> debug.log
    $e "data dir:\t     $data_dir\n"             >> debug.log


#   do the md calculation
    srun -N4 -n 96  pw.x < "$infile" >> "$outfile"  &


while true; do
	nstep=$(cat $outfile | grep POS -c)
	if ! [[ -a "efgs/efg.step-$nstep.in" ]]; then
		# create efg.step-N.in and run gipaw.x 
    		job="efg"
    		efginfile="efgs/efg.step-$nstep.in"
    		efgoutfile="efgs/efg.step-$nstep.out"
		
		$e "$(date):\tefg.step-$nstep.in not found! running gipaw in 20 seconds\n" >> "efg.log"
		sleep 20
		$e "\t...last 5 lines of $outfile are:\n" >> "efg.log"
		$e $(tail -n5 $outfile)			  >> "efg.log"

		$e "\twriting $efginfile now! Starting MPI!\n" >> "efg.log"

		cat > $efginfile << EOF
&inputgipaw
        job='$job'
        prefix='$prefix'
	tmp_dir='$outdir'
        verbosity='high'
  !     spline_ps=.true.
        q_gipaw=0.01
        q_efg(1)=2.044
/
EOF


#hangs here ...

		srun -N4 -n 96 gipaw.x < "$efginfile" >> "$efgoutfile" &
		
		$e "\tjob started ...  outfile:\t$efgoutfile\n"	>> "efg.log"
		$e "\tsleeping 5...\n"				>> "efg.log"
		sleep 5
	else
		$e "$(date):\tefg.step-$nstep.in exists! sleeping 30 seconds\n" >> "efg.log"
		sleep 30
	fi
done
		

# exit message
$e
$e "$(date):\t$0 has finished and is exiting now ...\n"     >> debug.log
$e

