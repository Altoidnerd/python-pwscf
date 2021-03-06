#!/usr/bin/env python3
#
#
# This script will rip the ith positions 
# out of an md run and place them into 
# individual scf.$i.in files with parameters
# specified in fstring
# 
# Specify CELL_PARAMETERS input card
# as variable cell_parameters,
# default values are from p-cl2phi cif 
#
#
#

import md as md
import numpy as np
import os







fstring="""
    &CONTROL
calculation  = 'scf'
restart_mode = 'from_scratch'
prefix       ='scf-{}'
pseudo_dir   ='/global/cscratch1/sd/almno10/.data/PSEUDOPOTENTIALS'
outdir       ='./scratch'
dt           = 60
tstress      =.false.
tprnfor      =.true.
!forc_conv_thr=1.0d-4
verbosity    = 'high'
nstep        = 2000
/

&system
    ibrav=0
    celldm(1)=1.889726
    nat={}
    ntyp={}
    ecutwfc=100
    ecutrho=1000
!   spline_ps=.true.
!   nosym=.true.
/

&electrons

    electron_maxstep  = 200
!   scf_must_converge = .true.
    conv_thr          = 1e-7
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
!   ion_dynamics      = 'verlet'
!   ion_positions     = 'default'
!   pot_extrapolation = 'atomic'
!   wfc_extrapolation = 'none'
!   remove_rigid_rot  = .false.
!
!-------------------------------------------
!    !!!Molecular Dynamics only!!!         -
!-------------------------------------------
    ion_temperature   = 'initial'
    tempw             = 586.D0
    tolp              = 100.D0
    delta_t           = 1.D0
    nraise            = 1
!    refold_pos
!------------------------------------------
!    !!!BFGS only!!!
!------------------------------------------
!   upscale           = 100.D0
!   bfgs_ndim         = 1
!   trust_radius_max  = 0.8D0
!   trust_radius_min  = 1.D-3
!   trust_radius_ini  = 0.5D0

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
  N  14.0067  N.pbe-n-kjpaw_psl.1.0.0.UPF
  C  12.0110  C.pbe-n-kjpaw_psl.1.0.0.UPF
  H   1.0079  H.pbe-kjpaw_psl.1.0.0.UPF
  O  15.9994  O.pbe-n-kjpaw_psl.1.0.0.UPF

CELL_PARAMETERS (alat)
{}

ATOMIC_POSITIONS (crystal)
{}

K_POINTS automatic
4 2 4 1 1 1
"""



def main():
  dest_dir='./scfs'
  try:
    os.mkdir(dest_dir)
  except FileExistsError:
      pass
  x     = md.Md('md.in','md.out')
  nat   = x.nat
  ntyp  = x.ntyp
  traj  = x.get_trajectory1()
  latvex= x.latvex_string
  for i in range(len(traj)):
    positions = ''
    for line in traj[i]:
      positions += line+'\n'
    scfinput = fstring.format(i, nat, ntyp, latvex, positions)
    f=open('{}/scf.{}.in'.format(dest_dir,i),'w')
    f.write(scfinput)
    f.close()
    #print(scfinput)

if __name__ == '__main__':
  main()


