#!/usr/bin/env python3

import numpy as np
import datafile as d
import matplotlib.pyplot as plt
from scipy.constants import *
import get_thetas as gt
import plot_thetas as pt


fft=np.fft

a0=4*pi*epsilon_0*hbar**2/(electron_mass*elementary_charge**2)
E_hartree=electron_mass*elementary_charge**4/(4*pi*epsilon_0*hbar)**2
t_hartree=hbar/E_hartree
t_au=2*t_hartree
dt  =160*t_au
c   =1/np.sqrt(epsilon_0*mu_0)
ccm =100*c

print(dt)

print("a0:\t{}\nE_hartree:\t{}\n1 a.u:\t{}\ndt: {} fs\nc:\t{}e10 cm/s".format(a0,E_hartree,t_au,dt/1e-15,ccm/1e10))

# get thetas
thetas  = pt.get_all_thetas(2524)
THETA_X, THETA_Y, THETA_X_SQ, THETA_Y_SQ = thetas[0], thetas[1], thetas[2], thetas[3]

# generate THETA_X signal
signal1  = THETA_X
signal1  = signal1 - np.average(signal1)
signal1  = signal1/max(signal1)

# generate THETA_Y signal
signal2  = THETA_Y
signal2  = signal2 - np.average(signal2)
signal2  = signal2/max(signal2)

# fourier
fourier1 = np.absolute(fft.rfft(signal1))
fourier2 = np.absolute(fft.rfft(signal2))


# configure horizontal azxis
freqs = fft.rfftfreq(len(signal1), dt)
wavenumbers = freqs/ccm



#plt.plot(wavenumbers[:150], 1/(fourier1.size)*fourier1[:150])
#plt.plot(wavenumbers[:150], 1/(fourier2.size)*fourier2[:150])
#plt.plot(wavenumbers, 1/(fourier1.size)*fourier1)
#plt.plot(wavenumbers, 1/(fourier2.size)*fourier2)

def main():
  fsize=500
  plt.plot(wavenumbers[:fsize], 1/fourier1.size*fourier1[:fsize], label="theta_x", color='r', linewidth=2)
  plt.plot(wavenumbers[:fsize], 1/fourier2.size*fourier2[:fsize], label="theta_y", color='g', linewidth=2)
  plt.xlabel("wavenumber (1/cm)")
  plt.ylabel("Intensity (arb. units)")
  plt.legend(loc=1)
  plt.title('Vibrational Spectrum of Cl1 in monoclinic paradichlorobenzene')
  
  width_inches=7
  height_inches=3.5
  aspect=width_inches/height_inches
 
  fig = plt.gcf()
  fig.set_size_inches(20,6, forward=True)
  fig.savefig("fft_THETA_X_THETA_Y.{:.3f}.pdf".format(aspect))

  plt.show()  

if __name__=='__main__':
  main()



  #plt.scatter(range(ley), THETA_Y, color='g', label='theta_y', marker=',',s=2 )
  #plt.scatter(range(lex), THETA_X , color='r', label='theta_x', marker='.',s=4 )


