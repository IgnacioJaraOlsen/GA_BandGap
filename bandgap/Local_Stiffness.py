import numpy as np

def Local_Stiffness(xm, xa, E, A, L):
    delta_E = E[1] - E[0]
    E_avg = (E[0] + E[1]) / 2
    delta_A = A[1] - A[0]
    A_avg = (A[0] + A[1]) / 2

    factor = ((delta_E * xm + E[0]) * (delta_A * xa + A[0])) / L
    
    Ke = factor * np.array([[1.0, 0.0, -1.0, 0.0],
                             [0.0, 0.0, 0.0, 0.0],
                             [-1.0, 0.0, 1.0, 0.0],
                             [0.0, 0.0, 0.0, 0.0]])
    
    return Ke