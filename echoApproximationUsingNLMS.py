import numpy as np 
from signalGeneration import dn,un

def updatewk(wk,n,u,xn,en,eps = 1e-12):
    wk = wk + (u * xn) / (abs(xn) ** 2 + eps) * en
    return wk



def Calmu_opt(wk,wk1,un,en,mu_fix,eps = 1e-12):
    deviation = np.linalg.norm(wk1 - wk)**2
    Pin = np.abs(un) ** 2
    Pe = np.abs(en) ** 2 + eps
    mu_opt = deviation * (Pin/Pe)
    mu_opt = mu_opt if (mu_opt <= 0.5 * mu_fix) else mu_fix
    return deviation * (Pin / Pe)


def compute_y(w,x,n):
    sum = 0
    for k in range (len(w)):
        sum = sum +  w[k] * x[n-k]
    return sum 




#Parameters
M = 4
mufix = 0.02

#Inputs
Fs = 44100          #sampling freq of the input signal 
t = 2               #input signal duration in seconds
N = int(44100 * t)



y = []
w = [0 for k in range (M)]
e = []
mu_opt = mufix
for n in range (N):
    y.append(compute_y(w,un,n))
    e.append(dn[n] - y[n])
    temp = w
    w = updatewk(w,n,mu_opt,un[n],e[n])
    mu_opt = Calmu_opt(temp,w,un[n],e[n],mufix) 


    
