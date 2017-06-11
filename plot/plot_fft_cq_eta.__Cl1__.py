#!/usr/bin/env python3

import numpy as np
import datafile as d
import matplotlib.pyplot as plt
from scipy.constants import *

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

# get cqs
cq1  = np.array(d.Cl1)
cq12 = np.array(d.Cl12)
cq18 = np.array(d.Cl18)
cq24 = np.array(d.Cl24)
# add and normalize
signal1  = (cq1 )#+ cq12 + cq18 + cq24)
signal1  = signal1 - np.average(signal1)
signal1  = signal1/max(signal1)
# fourier
fourier1 = np.absolute(fft.rfft(signal1))



# get etas
eta1  = np.array(d.eta1)
eta12 = np.array(d.eta12)
eta18 = np.array(d.eta18)
eta24 = np.array(d.eta24)
# add and normalize
signal2  = (eta1 )#+ eta12 + eta18 +eta24)
signal2  = signal2 - np.average(signal2)
signal2  = signal2/max(signal2)
# fourier
fourier2 = np.absolute(fft.rfft(signal2))



# configure horizontal azxis
freqs = fft.rfftfreq(len(signal1), dt)
wavenumbers = freqs/ccm



#plt.plot(wavenumbers[:150], 1/(fourier1.size)*fourier1[:150])
#plt.plot(wavenumbers[:150], 1/(fourier2.size)*fourier2[:150])
#plt.plot(wavenumbers, 1/(fourier1.size)*fourier1)
#plt.plot(wavenumbers, 1/(fourier2.size)*fourier2)

def main():
  plt.plot(wavenumbers[:800], 1/fourier1.size*fourier1[:800], label="coupling constants", linewidth=2)
  plt.plot(wavenumbers[:800], 1/fourier2.size*fourier2[:800], label="asymmetry params", linewidth=2)
  plt.xlabel("wavenumber (1/cm)")
  plt.ylabel("Intensity (arb. units)")
  plt.legend(loc=1)
  plt.title('Sprectrum of Cq and eta timeseries in Cl1') 
  width_inches=7
  height_inches=3.5
  aspect=width_inches/height_inches
 
  fig = plt.gcf()
  fig.set_size_inches(20,8, forward=True)
  fig.savefig("fft_cq_eta.{:.3f}.__Cl1__.pdf".format(aspect))

  plt.show()  

if __name__=='__main__':
  main()





