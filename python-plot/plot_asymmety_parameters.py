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

# members as the first N
# fixes a problem with generate_datafile.bash
def fix_broken_vector(li, N):
  fixed = li[-N:] + li[:-N]
  return fixed



Epots = [ Etots[i] - Ekins[i] for i in range(len(Ekins)) ] 
norm_Etots = [ thing/Etots[0] for thing in Etots ]
diff_Etots = [ thing - Etots[0] for thing in Etots ]
diff_Etots_scaled = [ scale_factor*(thing - Etots[0]) for thing in Etots ]
average_temp = get_mean(temperatures)
efg_step_0 = 6
nefgstep = len(Cl1)
inds = range(len(Ekins))
efg_inds = range(efg_step_0, efg_step_0 + len(Cl1)) 
times = [ ind*dt*ry_atomic_time for ind in inds ]
efg_times = times[ -len(Cl1): ]

#norm_Cl1   = [ float(item)/float( Cl1[0]  )  for item in Cl1  ]
#norm_Cl12  = [ float(item)/float( Cl12[0] )  for item in Cl12 ]
#norm_Cl18  = [ float(item)/float( Cl18[0] )  for item in Cl18 ]
#norm_Cl24  = [ float(item)/float( Cl24[0] )  for item in Cl24 ]

aCl1 = np.array(  [ np.abs(cq) for cq in Cl1 ])
aCl12= np.array(  [ np.abs(cq) for cq in Cl12])
aCl18= np.array(  [ np.abs(cq) for cq in Cl18])
aCl24= np.array(  [ np.abs(cq) for cq in Cl24])

aeta1 = np.array(  [ np.abs(cq) for cq in eta1 ])
aeta12= np.array(  [ np.abs(cq) for cq in eta12])
aeta18= np.array(  [ np.abs(cq) for cq in eta18])
aeta24= np.array(  [ np.abs(cq) for cq in eta24])

def main():
  print("""
	
	len(temperatures):	{}
	len(Ekins):		{}
	len(Etots):		{}
        len(Cl[1,12,18,24]	{} {} {} {}
        """.format(len(temperatures), len(Ekins), len(Etots), len(Cl1)  , len(Cl12)  , len(Cl18),  len(Cl24)   )
	)

  #plt.scatter(inds, Ekins, color='k', marker='>', s=25, label='Kinetic Energy (Ry)')
  #plt.plot(times, Ekins, color='g', label='E_kinetic (Ry), joined')
  #plt.scatter(times, Ekins, color='k', marker='.',  label='E_kinetic (Ry), data')
  #plt.plot(inds, norm_Etots, color='r', label='E_total[t]/(-548.00599230 Ry)')
  #plt.plot(inds, diff_Etots, color='k', label='E_total[t] - E_total[0] = E_total[t] + 548.00599230 Ry')
  #plt.plot(times, diff_Etots_scaled, color='m', label='E_total[t] - E_total[0] = E_total[t] + 548.00599230 Ry', linewidth=2)
 



  # plot of Cq's for Cl1, Cl12, Cl18, Cl24; horiztonal axis is time
  #plt.plot(   efg_times, Cl1 , color='r', label='Cl1  (MHz)', linewidth=1)
  #plt.scatter(efg_times, Cl1 , color='r', label='Cl1  (MHz)', marker='.' )
  #plt.plot(   efg_times, Cl12, color='c', label='Cl12 (MHz)', linewidth=1)
  #plt.scatter(efg_times, Cl12, color='c', label='Cl12 (MHz)', marker='.' ) 
  #plt.plot(   efg_times, Cl18, color='y', label='Cl18 (MHz)', linewidth=1)
  #plt.scatter(efg_times, Cl18, color='y', label='Cl18 (MHz)', marker=',' )
  #plt.plot(   efg_times, Cl24, color='g', label='Cl24 (MHz)', linewidth=1)
  #plt.scatter(efg_times, Cl24, color='g', label='Cl24 (MHz)', marker=',' )


  # good view of Cq's absolute vals, horizontal axis left in 10 a.u. divisions
  #plt.plot(   efg_inds, aCl1 , color='r',                     linewidth=1)
#  plt.scatter(efg_inds, aCl1 , color='r', label='Cl1  (MHz)', marker='.' )
  #plt.plot(   efg_inds, aCl12, color='g',                     linewidth=1)
#  plt.scatter(efg_inds, aCl12, color='g', label='Cl12 (MHz)', marker='.' ) 
  #plt.plot(   efg_inds, aCl18, color='b',                     linewidth=1)
#  plt.scatter(efg_inds, aCl18, color='b', label='Cl18 (MHz)', marker=',' )
  #plt.plot(   efg_inds, aCl24, color='m',                     linewidth=1)
#  plt.scatter(efg_inds, aCl24, color='m', label='Cl24 (MHz)', marker=',' )


## nice visualization of eta!
  plt.scatter(efg_inds, aeta1 , color='r', label='Cl1 (MHz)', marker='.',s=5 )
  plt.scatter(efg_inds, aeta12, color='g', label='Cl12 (MHz)', marker=',',s=5 )
  plt.scatter(efg_inds, aeta18, color='b', label='Cl18 (MHz)', marker='>',s=5 )
  plt.scatter(efg_inds, aeta24, color='m', label='Cl24 (MHz)', marker='<',s=5 )

  #plt.scatter(ecut, etas_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF')
  #plt.plot(ecut, etas)

  plt.title("Asymmetry parameters in p-Cl_2-benzene through MD run\n tempw={}K, dt={} a.u., nstep={}, T_avg={}K".format(tempw, dt, nefgstep,  get_mean(temperatures)))
  plt.ylabel("35Cl asymmetry parameter (|Vyy| - |Vxx|)/|Vzz| ")
  plt.xlabel("simulation step (dt = {} a.u./step) \n{} total steps; {} a.u. =  {} s/step; {}s total time".format(dt, nefgstep, dt, dt*ry_atomic_time, nefgstep*dt*ry_atomic_time))

  

  print(average_temp)
  plt.legend(loc=2)

  #plt.ylim(ymin=-547.5)
  #if sys.argv[1] == "save":
   # if not(sys.argv[2]):
    #  plt.savefig("eta-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))
  #  else:
   #   plt.savefig("{}.pdf".format(sys.argv[2]))
    #sys.exit()

  plt.savefig("eta-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))
  plt.show()  




if __name__ == '__main__':
  main()




