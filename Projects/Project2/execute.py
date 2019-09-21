'''
This file is a script that solves for the steady-state in the two-
period-lived overlapping generations model given some parameter values.
'''
# Put import commands below here
import sys, os
ppath = os.getcwd()
sys.path.append(os.path.join(ppath,'Projects','Project2'))
import FirmsMC
import household
import euler
import scipy.optimize as opt
import numpy as np
# Set parameter values


# Household parameters
n1 = 1.0
n2 = 0.2
nvec = np.array([n1, n2])
gamma = 2.2
beta_an = .96
beta = beta_an ** 30

# Firm parameters
A = 1.0
alpha = .33
delta_an = 0.05
delta = 1-(1 - delta_an) ** (1/30)

# Solve for b2 given parameters

args = nvec, alpha, A, delta, beta, gamma

def execute(args):

    # Load functions:
    b_init = 0

    b2 = euler.get_b2(euler.eul_err(b_init,*args))
    c1 = household.get_c1(b2, args)
    c2 = household.get_c2(b2, args)
    r  = FirmsMC.get_r(b2, args)
    w = FirmsMC.get_w(b2, args)
    K = FirmsMC.get_K(b2)
    L = FirmsMC.get_L(b2)
    C = c1 + c2
    Y = A * K**alpha * L ** (1-alpha)
    I = Y - C

    return c1, c2, r, w, K, L, Y, C, I

c1, c2, r, w, K, L, Y, C, I = execute(args)


# Solve for all the other endogenous variables given parameter values
# and optimal b2




# Print steady-state equilibrium endogenous variables
