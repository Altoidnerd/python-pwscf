#!/usr/bin/env python3

# how much magnetic field is requried
# to observe electron paramagnetic
# resonance at some frequency v?
# simplest: hv = ge uB Beff
# ge: g-factor of electron = 2.002...
# uB: bohr magneton
# uB = e h/(2 pi me)
# me: electron mass

si_bohr_magneton	= 9.27400968e-24
g_factor 		= 2.0023193043617
si_planck 		= 6.6260704e-34

# suppose v is 5 MHz
v = 5e6

B = si_planck * v / (g_factor * si_bohr_magneton)

print(B*10*10*10*10
)
#Bgauss = B * 10^4
#print("The required field is {} tesla which is {} gauss".format(B, Bgauss))
