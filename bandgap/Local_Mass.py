import numpy as np

def Local_Mass(xm, xa, dens, A, L):
    delta_dens = dens[1] - dens[0]
    dens_avg = (dens[0] + dens[1]) / 2
    delta_A = A[1] - A[0]
    A_avg = (A[0] + A[1]) / 2
    
    factor = (1/6) * ((delta_dens * xm + dens[0]) * (delta_A * xa + A[0]) * L)
    
    Me = factor * np.array([[2, 0, 1, 0],
                             [0, 2, 0, 1],
                             [1, 0, 2, 0],
                             [0, 1, 0, 2]])
    
    return Me