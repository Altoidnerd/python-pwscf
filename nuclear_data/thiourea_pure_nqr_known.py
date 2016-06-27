#!/usr/bin/env python3
# from smith, cotts, j. chem phys 41.8 1964 for pure thiourea
# at T = 77K

from calculate_frequencies import *

site1, site2 = [3.1216, .3954], [3.0996, .3930]

print("\n\n","site 1:\t",spin_1_nqr(*site1), "\n\n","site 2:\t", spin_1_nqr(*site2))


# 	site 1:	 [2.6497701599999997, 2.03262984, 0.6171403199999999] 
#	site 2:	 [2.6292357, 2.0201643, 0.6090714000000004]




#(c) 2015 A. Majewsk and M. Walker
