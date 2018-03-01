# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def lmap(func, li):
  return list(map(func, li))

f = open('hmx-data.txt','r').readlines()[2:]

# rip the temperatures from every other line
exptT	  		= lmap(float, [ line.split()[0] for line in f ][::2])
# v+ for the two sites, axial is higher in frequency
expt_vplus_axial    	= lmap(float, [ line.split()[1] for line in f ][0::2])
expt_vplus_equitorial   = lmap(float, [ line.split()[1] for line in f ][1::2])

# v- for the two sites respectively
expt_vminus_axial  	= lmap(float, [ line.split()[2] for line in f ][0::2])
expt_vminus_equitorial  = lmap(float, [ line.split()[2] for line in f ][1::2])

# asymmetry parameter for the two sites
expt_eta_axial      	= lmap(float, [ line.split()[3] for line in f ][0::2])
expt_eta_equitorial     = lmap(float, [ line.split()[3] for line in f ][1::2])

# coupling constants for the two sites
expt_cq_axial       	= lmap(float, [ line.split()[4] for line in f ][0::2])
expt_cq_equitorial      = lmap(float, [ line.split()[4] for line in f ][1::2])


# GIPAW values here??
calcT	             = [ 123,    173,    198,    223,    248,    273,    293,      ]

calc_cq_axial        = [ 6218.1, 6213.4, 6222.4, 6225.1,  6237.6, 6233.2  ] # NEED THESE
calc_cq_equitorial   = [ 6076.9, 6081.4, 6083.6, 6095.1,  6088.1, 6104.2  ] # NEED THESE

calc_eta_axial       = [.51103, .50995, .50811, .5076,   .50852,  .50189, .50603   ]
calc_eta_equitorial  = [.47346, .47237, .47316, .47615,  .47132,  .47091, .46757   ]

calc_vplus_axial     = [5457.9, 5452.2, 5457.2, 5458.8,  5453.4,  5460.8, 5463.5   ] 
calc_vplus_equitorial= [5276.9, 5279.2, 5282.3, 5290.0,  5300.5,  5282.8, 5291.7   ]

def main():
  
  #beta = unichr(0x3b2).encode('utf-8')
  beta = 'beta'
  title = "Calculated and exptl. NQR transition frequencies \naxial and equitorial 14N sites \nin  beta-HMX vs Temperature at 1 atm\n"
  plt.scatter(exptT, expt_vplus_axial,      marker='^', color='b', s=46, label='expt\'l v+, axial sites')
  plt.scatter(exptT, expt_vplus_equitorial, marker='<', color='k', s=46, label='expt\'l v+, equitorial sites')
  plt.scatter(calcT, calc_vplus_axial,      marker="s", color='g', s=46, label='GIPAW v+, axial sites') 
  plt.scatter(calcT, calc_vplus_equitorial, marker="o", color='r', s=46, label='GIPAW v+, equitorial sites') 

  plt.title(title)
  plt.xlabel("T (K)")
  plt.ylabel("KHz")
  plt.legend(loc=3)
  plt.show()

if __name__ == '__main__':
  main()

