#!/usr/bin/env python3 
#########################################
#					#
#					#
#  version 0.1				#
#  Nov 3, 2016				#
#   Copyright Allen Majewski 2016	#
#					#
#########################################


import numpy as np
import sys
import scipy.constants as const



def main():
  if len(sys.argv) > 1:
    nu_cm = float(sys.argv[1])
  else:
    nu_cm = 34 #inverse cm

  t_au		= 4.8378e-17 # number of seconds in Ry a.u.
  pi		= const.pi
  c 		= const.c
  hbar 		= const.hbar
  kb		= const.k

  lam_cm 	= 1/nu_cm

  lam 		= lam_cm/100

  nu 		= 1/lam

  k 		= 2*pi/lam

  k_cm		= 2*pi/lam_cm

  f 		= c/lam

  T 		= 1/f
  T_steps	= T/t_au

  omega 	= 2*pi*f

  f_thz 	= f/(10**12)

  T_fs 		= T*10**12
  
  temp		= hbar*omega/kb

  print("""

input:		{}

v:		{}			cm-1
		{} 	m-1
k:		{} 	rad/m
		{} 	rad/cm
f:		{} 	Hz
		{} 	THz
T:		{} 	s
		{} 	fs
		{} 	a.u.
lambda:		{} 	cm
		{}	m
omega:		{} 	rad/s
Temperature:	{} 	K

""".format(sys.argv[1], nu_cm, nu, k, k_cm, f, f_thz, T, T_fs, T_steps,lam_cm, lam, omega, temp))

if __name__ == '__main__':
  main()






