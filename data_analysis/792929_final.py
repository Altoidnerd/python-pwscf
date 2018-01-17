#!/usr/bin/env python3

import efg
import md
import sys
import numpy as np
import os
import nqr_parser as nqr


def theta_x(xi,yi,zi,xf,yf,zf):
    return np.arcsin(zf@yi)

def theta_y(xi,yi,zi,xf,yf,zf):
    thetax = theta_x(xi,yi,zi,xf,yf,zf)
    return zf@xi/np.cos(thetax)

def normalize(vector):
    return vector/np.linalg.norm(vector)

def ntheta_x(xi,yi,zi,xf,yf,zf):
    n=normalize
    xi,yi,zi,xf,yf,zf=n(xi),n(yi),n(zi),n(xf),n(yf),n(zf)
    return np.arcsin(zf@yi)

def ntheta_y(xi,yi,zi,xf,yf,zf):
    n=normalize
    xi,yi,zi,xf,yf,zf=n(xi),n(yi),n(zi),n(xf),n(yf),n(zf)
    thetax = theta_x(xi,yi,zi,xf,yf,zf)
    return zf@xi/np.cos(thetax)
#theta_x=ntheta_x
#theta_y=ntheta_y

os.chdir('/Users/altoidnerd/Desktop/nitroamines3/hmx/dt80N6/792929/scfs') 
print("\nWorking dir:\t{}".format(os.getcwd())) 
ls = os.listdir('.') 
efgfiles = [ thing for thing in ls if thing.startswith('efg') and thing.endswith('out') ]
numfiles= len(efgfiles) 
print("There are {} efg files in this directory.".format(numfiles))

efgs=[] 

for i in range(numfiles): 
    infile='efg.{}.out'.format(i) 
    efgs.append(efg.Efg(infile))

print("The indices of nitrogen atoms are:") 
nitrogen_labels=[] 

for label in efgs[0].atom_labels: 
    if 'N' in label: 
        new_index = efgs[0].atom_labels.index(label)+1 
        nitrogen_labels.append(new_index) 
        sys.stdout.write(str(new_index)+' ') 

print()

av_theta_xs = [] 
av_theta_ys = [] 
av_theta_y2s = [] 
av_theta_x2s = [] 
cq_coef0s = [] 
cq_coef1s = [] 
eta_coefs = [] 
cq0s = [] 
cqprime0s = [] 
cqprime1s = [] 
eta0s = [] 
etaprimes = [] 
fq0s = [] 
fqprimes = []

for atnum in nitrogen_labels: 
    efg0 = efgs[0] 
    specie=atnum 
    k=specie 
    print("\nWorking on atomic specie:\t{}".format(specie)) 
    
    
    this_nucleus=efg0.atom(k) 
    cq0=this_nucleus.cq 
    cq0s.append(cq0) 
    eta0=this_nucleus.eta
    
    
    xi=efg0.atom(k).x
    yi=efg0.atom(k).y
    zi=efg0.atom(k).z



    theta_x_vec=[]
    theta_y_vec=[]


    print("Fetching the angles in file efg.{}.out")
    for i in range(1,901):
        try:
            nucleus=efgs[i].atom(k)
            nuc=nucleus
            xf,yf,zf=nuc.x,nuc.y,nuc.z
            args=(xi,yi,zi,xf,yf,zf)
            #print("thetaX{}\t".format(i),"\t", theta_x(xi,yi,zi,xf,yf,zf),"\t", "thetaY{}\t".format(i), theta_y(xi,yi,zi,xf,yf,zf))
            theta_x_vec.append(theta_x(*args))
            theta_y_vec.append(theta_y(*args))
            sys.stdout.write("{} \r".format(i))
        except IndexError:
            sys.stdout.write("skipped:{}\n".format(i))
        
  
                 # theta_x squareds and theta_y squareds
    theta_x2_vec=[angle**2 for angle in theta_x_vec]
    theta_y2_vec=[angle**2 for angle in theta_y_vec]

    av=np.average
    av_theta_x  = av(theta_x_vec)
    av_theta_y  = av(theta_y_vec)
    av_theta_x2 = av(theta_x2_vec)
    av_theta_y2 = av(theta_y2_vec)

    av_theta_xs.append(av_theta_x)
    av_theta_ys.append(av_theta_y)
    av_theta_x2s.append(av_theta_x2)
    av_theta_y2s.append(av_theta_y2)

    print("\nReport for atomic specie:\t{}".format(k))
    print("Working Dir:\t{}".format(os.getcwd()))
    print("<tx>:\t",av_theta_x,"\t<ty>:\t",   av_theta_y,"\n",
      "<tx^2>\t:",av_theta_x2,"\t<ty^2>:", av_theta_y2,"\n")

    print("cq0=\t{}".format(cq0))
    print("eta0=\t{}".format(eta0))

    cq_coef0 = 1 - 3/2*(av_theta_x2 + av_theta_y2)
    cq_coef0s.append(cq_coef0)
    cq_coef1 = 1 - 3/2*(av_theta_x2 + av_theta_y2 - 1/2*eta0*(av_theta_x2 - av_theta_y2))
    cq_coef1s.append(cq_coef1)

    print("==================================")
    print("792929:\tT=248K, nuclear site: {}  =".format(specie))
    print("==================================")


    print("1-3/2(<tx^2>+<ty^2>)\t\t={}".format(cq_coef0))
    print("1-3/2(<tx^2>+<ty^2>-1/2eta0*(<tx^2>-<ty^2>)\t={}".format(cq_coef1))
    print()


    cqprime0=cq0*cq_coef0
    cqprime0s.append(cqprime0)
    cqprime1=cq0*cq_coef1
    cqprime1s.append(cqprime1)


    print("Cq0:\t\t{}".format(cq0))
    print("Cq' from coefficient 1-3/2(<>+<>):\t\t{}".format(cqprime0))
    print("Cq' from coefficient 1-3/2(<>+<>)+1/2eta(<>-<>)):\t{}".format(cqprime1))
    nuclear_spin=1
    freq_function=nqr.f1
    print(
    "Computing NQR frequencies for spin:\t{}\nusing function {}\tand simple coefficient".format(nuclear_spin, freq_function)
    )
    print("WARNING:\t eta not adjusted.  Using eta0.")
    fq=freq_function(cqprime0,eta0)
    fq0s.append(fq)
    print("fqs={}".format(freq_function(cqprime0, eta0)))
    print()
    print()

print("##################################"*2)
print("##################################"*2)
print()
print("==================================")
print("          FINAL REPORT            ")
print("==================================")
print("""
nitrogen_labels:\t{}
av_theta_xs:\t{}    
av_theta_ys:\t{}  
av_theta_y2s:\t{}
av_theta_x2s:\t{} 
cq_coef0s =:\t{}
cq_coef1s:\t{}
eta_coefs:\t{}
cq0s:\t{} 
cqprime0s:\t{}
cqprime1s:\t{} 
eta0s:\t{} 
etaprimes:\t{}
fq0s:\t{} 
fqprimes:\t{}


    """.format(
    nitrogen_labels,
    av_theta_xs,
    av_theta_ys, 
    av_theta_y2s, 
    av_theta_x2s, 
    cq_coef0s, 
    cq_coef1s, 
    eta_coefs, 
    cq0s, 
    cqprime0s, 
    cqprime1s, 
    eta0s, 
    etaprimes, 
    fq0s, 
    fqprimes))



