#!/usr/bin/env python3

import math

def spin_1_nqr(cq, eta=0, debug=False, verbose=False):
    if verbose:
        print("3 transitions to return")
        print("v+- \t= 3/4 cq (1 +- eta/3)")
        print("dv \t= v+ - v-")
        print("returns:\t [v2, v1, v0]")
    v2 = 3/4*cq*(1 + eta/3)
    v1 = 3/4*cq*(1 - eta/3)
    v0 = v2 - v1
    v0_check = cq*eta/2
    if debug:
        print("v2 - v1 , cq*eta/2:\t", v0, v0_check)
        print("v2:\t", v2)
        print("v1:\t", v1)
    return [v2,v1,v0]

def spin_32_nqr(cq, eta=0, debug=False, verbose=False):
    if verbose:
        print("1 transition to return")
        print("v =\t", "Cq/2 * (1 + 1/3 eta^2)^.5")
        print("returns:\t","float")
    return cq/2*math.sqrt(1 + 1/3*eta**2)

def spin_52_nqr(cq, eta=0, debug=False, verbose=False):
    if verbose:
        print("2 transitions to return")
        print("v2 \t= 3/10 Cq (1 - 11/54 eta^2)")
        print("v1 \t= 3/20 Cq (1 - 5/54 eta^2)")
        print("returns:\t","[v2,v1]")
    v2 = 3/10*cq*(1 - 11/54*eta**2)
    v1 = 3/20*cq*(1 + 5/54*eta**2)
    return [v2, v1]





#(c) 2015 A. Majewsk and M. Walker
