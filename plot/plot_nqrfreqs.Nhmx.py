#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys
from datafile import *
from nqr_parser6 import f1

#
# hmx 
#nitrogen indices
#
# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51 53  54  56
#
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


dt=20
scale_factor = 1.0
ry_atomic_time=4.8378e-17 #seconds per a.u.
timestep_SI = dt*ry_atomic_time
tempw=246


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


def get_fmean(li):
  summe = 0
  for item in li:
    summe += item
  return float(summe/len(li))



def avg_to_ind(li, ind):
  return get_fmean(li[0:ind+1])



def get_rolling_avgs(li):
  rollings = []
  for item in range(len(li)):
    rollings.append(avg_to_ind(li,item))
  return rollings


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
efg_step_0 = 0
nefgstep = len(N1)
inds = range(len(Ekins))
efg_inds = range(efg_step_0, efg_step_0 + len(N1)) 
times = [ ind*dt*ry_atomic_time for ind in inds ]
efg_times = times[ -len(N1): ]


aN1 = np.array( [ np.abs(cq) for cq in N1  ])
aN3 = np.array( [ np.abs(cq) for cq in N3  ])
aN4 = np.array( [ np.abs(cq) for cq in N4  ])
aN6 = np.array( [ np.abs(cq) for cq in N6  ])
aN23= np.array( [ np.abs(cq) for cq in N23 ])
aN25= np.array( [ np.abs(cq) for cq in N25 ])
aN26= np.array( [ np.abs(cq) for cq in N26 ])
aN28= np.array( [ np.abs(cq) for cq in N28 ])
aN37= np.array( [ np.abs(cq) for cq in N37 ])
aN39= np.array( [ np.abs(cq) for cq in N39 ])
aN40= np.array( [ np.abs(cq) for cq in N40 ])
aN42= np.array( [ np.abs(cq) for cq in N42 ])
aN51= np.array( [ np.abs(cq) for cq in N51 ])
aN53= np.array( [ np.abs(cq) for cq in N53 ])
aN54= np.array( [ np.abs(cq) for cq in N54 ])
aN56= np.array( [ np.abs(cq) for cq in N56 ])



# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51 53  54  56

aeta1 = np.array(  [ np.abs(cq) for cq in eta1 ])
aeta3 = np.array(  [ np.abs(cq) for cq in eta3 ])
aeta4 = np.array(  [ np.abs(cq) for cq in eta4 ])
aeta6 = np.array(  [ np.abs(cq) for cq in eta6 ])

aeta23= np.array(  [ np.abs(cq) for cq in eta23])
aeta25= np.array(  [ np.abs(cq) for cq in eta25])
aeta26= np.array(  [ np.abs(cq) for cq in eta26])
aeta28= np.array(  [ np.abs(cq) for cq in eta28])

aeta37= np.array(  [ np.abs(cq) for cq in eta37])
aeta39= np.array(  [ np.abs(cq) for cq in eta39])
aeta40= np.array(  [ np.abs(cq) for cq in eta40])
aeta42= np.array(  [ np.abs(cq) for cq in eta42])

aeta51= np.array(  [ np.abs(cq) for cq in eta51])
aeta53= np.array(  [ np.abs(cq) for cq in eta53])
aeta54= np.array(  [ np.abs(cq) for cq in eta54])
aeta56= np.array(  [ np.abs(cq) for cq in eta56])

nqrfreqs1  = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN1 , aeta1 ) ]
nqrfreqs3  = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN3 , aeta3 ) ]
nqrfreqs4  = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN4 , aeta4 ) ]
nqrfreqs6  = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN6 , aeta6 ) ]

nqrfreqs23 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN23, aeta23) ]
nqrfreqs25 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN25, aeta25) ]
nqrfreqs26 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN26, aeta26) ]
nqrfreqs28 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN28, aeta28) ]

nqrfreqs37 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN37, aeta37) ]
nqrfreqs39 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN39, aeta39) ]
nqrfreqs40 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN40, aeta40) ]
nqrfreqs42 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN42, aeta42) ]

nqrfreqs51 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN51, aeta51) ]
nqrfreqs53 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN53, aeta53) ]
nqrfreqs54 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN54, aeta54) ]
nqrfreqs56 = [ f1(cq,eta)[-1] for (cq,eta) in zip(aN56, aeta56) ]


# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51 53  54  56

def main():
  print("""
	
	len(temperatures):	{}
	len(Ekins):		{}
	len(Etots):		{}
        len(N[1,3,4,6,23,25,26,28,37,39,40,42,51,53,54,56]:\n{} {} {} {}	{} {} {} {} 	{} {} {} {} 	{} {} {} {} 
        """.format(
            len(temperatures), 
            len(Ekins), 
            len(Etots), 
            len(N1 ), 
            len(N3 ), 
            len(N4 ),  
            len(N6 ), 
            len(N23), 
            len(N25), 
            len(N26),  
            len(N28), 
            len(N37), 
            len(N39), 
            len(N40),  
            len(N42), 
            len(N51), 
            len(N53), 
            len(N54),  
            len(N26)
            )	
  )


  # good view of Cq's absolute vals, horizontal axis left in 10 a.u. divisions

#  plt.scatter(efg_inds, get_rolling_avgs(aN1 ), color='r', label='N1  (MHz)', marker='.' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN3 ), color='b', label='N3  (MHz)', marker='.' ) 
#  plt.scatter(efg_inds, get_rolling_avgs(aN4 ), color='g', label='N18 (MHz)', marker='.' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN6 ), color='c', label='N24 (MHz)', marker='.' )
#
#  plt.scatter(efg_inds, get_rolling_avgs(aN23), color='m', label='N23 (MHz)', marker=',' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN25), color='y', label='N25 (MHz)', marker=',' ) 
#  plt.scatter(efg_inds, get_rolling_avgs(aN26), color='k', label='N26 (MHz)', marker=',' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN28), color='r', label='N28 (MHz)', marker=',' )
 
#  plt.scatter(efg_inds, get_rolling_avgs(aN37), color='g', label='N37 (MHz)', marker='o' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN39), color='b', label='N39 (MHz)', marker='o' ) 
#  plt.scatter(efg_inds, get_rolling_avgs(aN40), color='c', label='N40 (MHz)', marker='o' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN42), color='m', label='N42 (MHz)', marker='o' )
# 
#  plt.scatter(efg_inds, get_rolling_avgs(aN51), color='y', label='N51 (MHz)', marker='^' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN53), color='k', label='N53 (MHz)', marker='^' ) 
#  plt.scatter(efg_inds, get_rolling_avgs(aN54), color='r', label='N54 (MHz)', marker='^' )
#  plt.scatter(efg_inds, get_rolling_avgs(aN26), color='g', label='N56 (MHz)', marker='^' )


# 1  3  4  6
#23 25 26 28
#37 39 40 42
#51 53  54  56

  plt.scatter(efg_inds,  nqrfreqs1, color='r', label='N1  ', marker='.' )
  plt.scatter(efg_inds,  nqrfreqs3, color='g', label='N12 ', marker='.' )
  plt.scatter(efg_inds,  nqrfreqs4, color='b', label='N18 ', marker='.' )
  plt.scatter(efg_inds,  nqrfreqs6, color='m', label='N24 ', marker='.' )

  plt.scatter(efg_inds, nqrfreqs23, color='m', label='N1  ', marker=',' )
  plt.scatter(efg_inds, nqrfreqs25, color='y', label='N12 ', marker=',' )
  plt.scatter(efg_inds, nqrfreqs26, color='k', label='N18 ', marker=',' )
  plt.scatter(efg_inds, nqrfreqs28, color='r', label='N24 ', marker=',' )

  plt.scatter(efg_inds, nqrfreqs37, color='g', label='N1  ', marker='o' )
  plt.scatter(efg_inds, nqrfreqs39, color='b', label='N12 ', marker='o' )
  plt.scatter(efg_inds, nqrfreqs40, color='c', label='N18 ', marker='o' )
  plt.scatter(efg_inds, nqrfreqs42, color='m', label='N24 ', marker='o' )

  plt.scatter(efg_inds, nqrfreqs51, color='y', label='N1  ', marker='^' )
  plt.scatter(efg_inds, nqrfreqs53, color='k', label='N12 ', marker='^' )
  plt.scatter(efg_inds, nqrfreqs54, color='r', label='N18 ', marker='^' )
  plt.scatter(efg_inds, nqrfreqs56, color='b', label='N24 ', marker='^' )



  plt.title("Rolling average NQR frequencies in HMX (structure@123K)\ntempw={}K, dt={} a.u., nstep={}, T_avg={}K".format(tempw, dt, nefgstep,  get_mean(temperatures)))
  plt.ylabel("14N NQR frequency (MHz)")
  plt.xlabel("simulation step (dt = {} a.u./step) \n{} total steps; {} a.u. =  {} s/step; {}s total time".format(dt, nefgstep, dt, dt*ry_atomic_time, nefgstep*dt*ry_atomic_time))

#  

  print(average_temp)
  plt.legend(loc=3)
  #plt.savefig("cqs-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))
  #plt.ylim(ymin=-547.5)

  plt.show()  




if __name__ == '__main__':
  main()



