import numpy as np
import numba as nb

def wave_vector(NINT, Lx, Ly, type):
    Minv = 1e-4
    X_0_L = np.linspace(Minv / Lx, np.pi / Lx, NINT)
    X_L_0 = np.linspace(np.pi / Lx, Minv / Lx, NINT)
    X_0_nL = np.linspace(Minv / Lx, -np.pi / Lx, NINT)
    X_nL_0 = np.linspace(-np.pi / Lx, Minv / Lx, NINT)

    Y_0_L = np.linspace(Minv / Ly, np.pi / Ly, NINT)
    Y_L_0 = np.linspace(np.pi / Ly, Minv / Ly, NINT)
    Y_0_nL = np.linspace(Minv / Ly, -np.pi / Ly, NINT)
    Y_nL_0 = np.linspace(-np.pi / Ly, Minv / Ly, NINT)

    X_0 = np.full(NINT, Minv / Lx)
    Y_0 = np.full(NINT, Minv / Ly)

    X_L = np.full(NINT, np.pi / Lx)
    Y_L = np.full(NINT, np.pi / Ly)

    X_nL = np.full(NINT, -np.pi / Lx)
    Y_nL = np.full(NINT, -np.pi / Ly)

    if type == 0:
        thetax = np.concatenate((X_0_L, X_L, X_L_0))
        thetay = np.concatenate((Y_0, Y_0_L, Y_L_0))
    elif type == 1:
        thetax = np.concatenate((X_0_L, X_L, X_L_0, X_0))
        thetay = np.concatenate((Y_0, Y_0_L, Y_L, Y_0_L))
    elif type == 2:
        thetax = np.concatenate((X_L_0, X_0_L, X_L, X_L_0, X_0, X_0_nL, X_nL, X_nL_0, X_0, Y_L, Y_L_0, X_0_nL, X_nL, X_nL_0, X_0, X_0_nL, X_nL_0, X_0_L, X_L, X_L_0, X_0, X_0_L))
        thetay = np.concatenate((Y_L_0, Y_0, Y_0_L, Y_L, Y_L_0, Y_0, Y_0_L, Y_L_0, Y_0_L, X_0_nL, X_nL_0, Y_0_nL, Y_nL_0, Y_0, Y_0_nL, Y_nL, Y_nL_0, Y_0_nL, Y_nL_0, Y_0, Y_0_nL, Y_L))
    
    return thetax, thetay