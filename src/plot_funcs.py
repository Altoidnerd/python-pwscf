#!/usr/bin/env python3
#
#
#
#
#

####################################
def fix_broken_vector(li, N):
  fixed = li[-N:] + li[:-N]
  return fixed



####################################
def avg_to_ind(li, ind):
  return get_fmean(li[0:ind+1])



####################################
def get_mean(li):
  summe = 0
  for item in li:
    summe += item
  return int(summe/len(li))


####################################
def get_fmean(li):
  summe = 0
  for item in li:
    summe += item
  return float(summe/len(li))





#####################################
def get_rolling_avgs(li):
  """ Takes a list as an argument,
  returns a list that is the running
  average for all previous members
  of the input list"""
  rollings = []
  for item in range(len(li)):
    rollings.append(avg_to_ind(li,item))
  return rollings

