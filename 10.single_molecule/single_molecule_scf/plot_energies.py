#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
from datafile import *



#########################################################
# 	This plotter script requires a file named
#	datafile.py to exist in the working dir which 
#	must contain three vectors of equal length
#	
#	temperatures = [ ... ]
#	Ekins = [ ... ]
#	Etots = [ ... ]
#	
########################################################


dt=10
scale_factor = 1.0
ry_atomic_time=4.8378e-17 #seconds per a.u.
timestep_SI = dt*ry_atomic_time
tempw=584

if (len(temperatures) == len(Ekins)) and (len(Ekins) == len(Etots)):
  nstep = len(temperatures)
else:
  sys.stdout.write("\nERROR:\t legnths of temp, KE, and E vectors do not match. Exiting now.\n\n\tgoodbye\n\n")
  sys.exit()


def get_mean(li):
  summe = 0
  for item in li:
    summe += item
  return int(summe/len(li))


Epots = [ Etots[i] - Ekins[i] for i in range(len(Ekins)) ] 
norm_Etots = [ thing/Etots[0] for thing in Etots ]
diff_Etots = [ thing - Etots[0] for thing in Etots ]
diff_Etots_scaled = [ scale_factor*(thing - Etots[0]) for thing in Etots ]
average_temp = get_mean(temperatures)
inds = range(len(Ekins))
times = [ ind*dt*ry_atomic_time for ind in inds ]
nefgstep = len(Cl1)


def main():
  print("""
	
	len(temperatures):	{}
	len(Ekins):		{}
	len(Etots):		{}

        """.format(len(temperatures), len(Ekins), len(Etots))
	)


  #plt.scatter(inds, Ekins, color='k', marker='>', s=25, label='Kinetic Energy (Ry)')
  plt.plot(inds, Ekins, color='g', label='E_kinetic (Ry), joined')
  plt.scatter(inds, Ekins, color='k', marker='.',  label='E_kinetic (Ry), data')
  #plt.plot(inds, norm_Etots, color='r', label='E_total[t]/(-548.00599230 Ry)')
  #plt.plot(inds, diff_Etots, color='k', label='E_total[t] - E_total[0] = E_total[t] + 548.00599230 Ry')
  plt.plot(inds, diff_Etots_scaled, color='m', label='E_total[t] - E_total[0] = E_total[t] + 548.00599230 Ry', linewidth=1)
#  plt.scatter(times, diff_Etots_scaled, color='k', marker='.')


  #plt.scatter(ecut, etas_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF')
  #plt.plot(ecut, etas)

  plt.title("Kinetic Energy in p-Cl_2-benzene MD\n tempw={}K, dt={} a.u., nstep={}, T_avg={}K".format(tempw, dt, nstep,  get_mean(temperatures)))
  plt.ylabel("Ry (13.6 eV)")
  plt.xlabel("timestep \ndt = {}a.u./step; 1 a.u. = {} s/step; {}s total time".format(dt, dt*ry_atomic_time, nstep*dt*ry_atomic_time))


  print(average_temp)
  plt.legend(loc=1)

  #plt.ylim(ymin=-547.5)
  plt.savefig("Ekin_and_Etot_dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))
  plt.show()  




if __name__ == '__main__':
  main()



