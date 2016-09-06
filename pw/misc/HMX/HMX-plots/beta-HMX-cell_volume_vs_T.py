#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

Temps   = [ 123, 173, 198, 223, 248, 273, 293, 303 ]
Vols    = [ 505.97, 508.91, 509.93, 512.45, 513.53, 514.20, 516.63, 517.45 ]
Ays     = [ 1 ]
Bees    = [ 1 ]
Cees    = [ 1 ]
Betas   = [ 1 ]

ays     = [ thing/Ays[0]   for thing in Ays   ]
bees    = [ thing/Bees[0]  for thing in Bees  ]
cees    = [ thing/Cees[0]  for thing in Cees  ]
betas   = [ thing/Betas[0] for thing in Betas ]
temps 	= [ thing/Temps[0] for thing in Temps ]
vols    = [ thing/Vols[0]  for thing in Vols  ]

plt.scatter(temps, vols)
plt.show()
























