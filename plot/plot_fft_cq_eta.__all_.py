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
signal1  = (cq1)# + cq12 + cq18 + cq24)
signal1  = signal1 - np.average(signal1)
signal1  = signal1/max(signal1)
# fourier
fourier1 = np.absolute(fft.rfft(signal1))

signal12  = (cq12)# + cq12 + cq18 + cq24)
signal12  = signal1 - np.average(signal1)
signal12  = signal12/max(signal1)
# fourier
fourier12 = np.absolute(fft.rfft(signal12))

signal18  = (cq18)# + cq12 + cq18 + cq24)
signal18  = signal18 - np.average(signal18)
signal18  = signal18/max(signal18)
# fourier
fourier18 = np.absolute(fft.rfft(signal18))

signal24  = (cq24)# + cq12 + cq18 + cq24)
signal24  = signal24 - np.average(signal24)
signal24  = signal24/max(signal24)
# fourier
fourier24 = np.absolute(fft.rfft(signal1))
# get etas
eta1  = np.array(d.eta1)
eta12 = np.array(d.eta12)
eta18 = np.array(d.eta18)
eta24 = np.array(d.eta24)


# add and normalize
esignal1  = (eta1)# + eta12 + eta18 +eta24)
esignal1  = esignal1 - np.average(esignal1)
esignal1  = esignal1/max(esignal1)
# fourier
efourier1 = np.absolute(fft.rfft(esignal1))


esignal12  = (eta12)# + eta12 + eta18 +eta24)
esignal12  = esignal12 - np.average(esignal12)
esignal12  = esignal12/max(esignal12)
# fourier
efourier12 = np.absolute(fft.rfft(esignal12))

esignal18  = (eta18)# + eta12 + eta18 +eta24)
esignal18  = esignal18 - np.average(esignal18)
esignal18  = esignal18/max(esignal18)
# fourier
efourier18 = np.absolute(fft.rfft(esignal18))

esignal24  = (eta24)# + eta12 + eta18 +eta24)
esignal24  = esignal24 - np.average(esignal24)
esignal24  = esignal24/max(esignal24)
# fourier
efourier24 = np.absolute(fft.rfft(esignal24))
# configure horizontal azxis
freqs = fft.rfftfreq(len(esignal1), dt)
wavenumbers = freqs/ccm



#plt.plot(wavenumbers[:150], 1/(fourier1.size)*fourier1[:150])
#plt.plot(wavenumbers[:150], 1/(fourier2.size)*fourier2[:150])
#plt.plot(wavenumbers, 1/(fourier1.size)*fourier1)
#plt.plot(wavenumbers, 1/(fourier2.size)*fourier2)

def main():
  # colors=bgrcmykw
  plt.plot(wavenumbers[:1000],     1/fourier1.size*fourier1[:1000],	label="Cq Cl1" , color="b")
  plt.plot(wavenumbers[:1000],   1/fourier12.size*fourier12[:1000],	label="Cq Cl12", color="g")
  plt.plot(wavenumbers[:1000],   1/fourier18.size*fourier18[:1000],	label="Cq Cl18", color="r")
  plt.plot(wavenumbers[:1000],   1/fourier24.size*fourier24[:1000],	label="Cq Cl24", color="k")
  plt.plot(wavenumbers[:1000],   1/efourier1.size*efourier1[:1000],	label="eta Cl1", color="b", linestyle='--', linewidth=1)
  plt.plot(wavenumbers[:1000], 1/efourier12.size*efourier12[:1000], 	label="eta Cl12",color="g",  linestyle='--', linewidth=1)
  plt.plot(wavenumbers[:1000], 1/efourier18.size*efourier18[:1000], 	label="eta Cl1", color="r", linestyle='--', linewidth=1)
  plt.plot(wavenumbers[:1000], 1/efourier24.size*efourier24[:1000], 	label="eta Cl24",color="k", linestyle='--', linewidth=1)
  plt.xlabel("wavenumber (1/cm)")
  plt.ylabel("Intensity (arb. units)")
  plt.legend(loc=1)
  plt.title('spectrum of Cq, eta time series for each Cl site')  
  width_inches=7
  height_inches=3.5
  aspect=width_inches/height_inches
 
  fig = plt.gcf()
  fig.set_size_inches(20,8, forward=True)
  fig.savefig("fft_cq_eta.{:.3f}.__all_Clsites_individually__.pdf".format(aspect))

  plt.show()  

if __name__=='__main__':
  main()





