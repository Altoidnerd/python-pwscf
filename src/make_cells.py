#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data            = [ line.split() for line in open('wheeler1976_thermal_expansion.txt','r').readlines() ]

cell_parameters = pd.DataFrame( [ list(map(float, li)) for li in data[1:] ], columns=data[0] )  

df              = cell_parameters
