# -*- coding: utf-8 -*-

##########################
# RELAXED DATA UP IN HERE#
#			 #
##########################

import matplotlib.pyplot as plt

f = open('hmx-data.txt','r').readlines()[2:]

# rip the temperatures from every other line
# len(temperatures) == 34
temperatures  		= [ line.split()[0] for line in f ][::2]

# v+ for the two sites, axial is higher in frequency
vplus_axial    		= [ line.split()[1] for line in f ][0::2]
vplus_equitorial    	= [ line.split()[1] for line in f ][1::2]

# v- for the two sites respectively
vminus_axial  		= [ line.split()[2] for line in f ][0::2]
vminus_equitorial    	= [ line.split()[2] for line in f ][1::2]

# asymmetry parameter for the two sites
eta_axial      		= [ line.split()[3] for line in f ][0::2]
eta_equitorial       	= [ line.split()[3] for line in f ][1::2]

# coupling constants for the two sites
cq_axial       		= [ line.split()[4] for line in f ][0::2]
cq_equitorial        	= [ line.split()[4] for line in f ][1::2]


# GIPAW values here??
gipawtemps            = [ 123,    173,    198,    223,    248,    273,    293,    303   ]
#gipawtemps            = [ 123,    173,    198,    223,        273,    293,      ]
#ecut100
gipaw_cq_axial        = [ 6187.5, 6190.9, 6201.1, 6196.6, 6209.9, 6209.9, 6210.3, 6209.1 ] # NEED THESE
gipaw_cq_equitorial   = [ 5983.2, 5991.6, 5991.6, 6003.6, 6001.7, 6003.5, 6024.1, 6010.5 ] # NEED THESE

#gipaw_cq_axial        = [ 6218.1, 6213.4, 6222.4, 6225.1,  6237.6, 6233.2  ] # NEED THESE
#gipaw_cq_equitorial   = [ 6076.9, 6081.4, 6083.6, 6095.1,  6088.1, 6104.2  ] # NEED THESE

gipaw_eta_axial       = [.53135, .52763, .53035, .5272, .52909, .52829, .52724, .52627 ]
gipaw_eta_equitorial  = [.49608, .49617, .49537, .49588,.49374, .49376, .4895, .49393  ]

gipaw_vplus_axial     = [5462.5 , 5459.0, 5473.0, 5464.1, 5478.8, 5477.5, 5476.3, 5473.7] 
gipaw_vplus_equitorial= [5229.4 , 5236.9, 5235.7, 5246.9, 5242.1, 5243.7, 5255.3, 5250.1]

# From N1
Tcorr0_axial         = [.99501 ,.99186, .99197, .99066, .98938, .98843, .98712, .98704 ]
Tcorr_full_axial     = [.99491 ,.99191, .99249, .99074, .98390, .98884, .98756, .98672 ]
gipaw_Vcorr_Tcorr0_cq_axial          =  [ gipaw_cq_axial[i]*Tcorr0_axial[i]          for i in range(8) ]
gipaw_Vcorr_Tcorr_full_cq_axial      =  [ gipaw_cq_axial[i]*Tcorr_full_axial[i]      for i in range(8) ]

# From N4
Tcorr0_equitorial    = [.99468, .99240, .99315, .99196, .98911, .98893, .98857, .98619 ]
Tcorr_full_equitorial= [.99412, .99242, .99328, .99216, .98891, .98831, .98817, .98728 ]    
gipaw_Vcorr_Tcorr0_cq_equitorial     =  [ gipaw_cq_equitorial[i]*Tcorr0_equitorial[i]     for i in range(8) ]
gipaw_Vcorr_Tcorr_full_cq_equitorial =  [ gipaw_cq_equitorial[i]*Tcorr_full_equitorial[i] for i in range(8) ]




gc0_axial         = gipaw_Vcorr_Tcorr0_cq_axial 
gc_full_axial     = gipaw_Vcorr_Tcorr_full_cq_axial

gc0_equitorial    = gipaw_Vcorr_Tcorr0_cq_equitorial  
gc_full_equitorial= gipaw_Vcorr_Tcorr_full_cq_equitorial 

def main():
  
  #beta = unichr(0x3b2).encode('utf-8')
  beta = 'beta'
  title = "Calculated and exptl. Cq for 14N sites in \nbeta-HMX v.s. temperature @ 1 atm\nFully relaxed structures\nGGA(pbe) pseudo, Ecut=80Ry "
  plt.scatter(temperatures, cq_axial,      marker='^', color='b', s=60, label='expt\'l Cq, axial site')
  plt.scatter(temperatures, cq_equitorial, marker='<', color='k', s=60, label='expt\'l Cq, equitorial site')
  plt.scatter(gipawtemps, gc0_axial,     marker="s", color='r', s=60, label='GIPAW Cq, axial site (N1)') 
  #plt.scatter(gipawtemps, gc_full_axial,     marker="s", color='g', s=60, label='GIPAW Cq, axial sites, corr_full') 
  plt.scatter(gipawtemps, gc0_equitorial,     marker="s", color='g', s=60, label='GIPAW Cq, equitorial site (N4)') 
  #plt.scatter(gipawtemps, gc_full,     marker="s", color='g', s=60, label='GIPAW Cq, axial sites, corr_full') 
  #plt.scatter(gipawtemps, gipaw_cq_equitorial,     marker="o", color='r', s=60, label='GIPAW Cq, equitorial sites') 

  plt.title(title)
  plt.xlabel("T (K)")
  plt.ylabel("KHz")
  plt.legend(loc=3)
  plt.show()

if __name__ == '__main__':
  main()

