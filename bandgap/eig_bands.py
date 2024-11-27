import numpy as np
from joblib import Parallel, delayed
from tqdm import tqdm
from scipy.sparse.linalg import eigs
from numpy import linalg as LA
from numba import njit

from bandgap.T_matrix import T_matrix
from bandgap.Global_KM import Global_KM
from icecream import ic

import torch

import numba as nb

ic.disable()

def eig_bands(Lx, Ly, nx, ny, ne, coord, connect, E, A, dens, x, nav, theta_x, theta_y):
    
    bigk, bigm = Global_KM(ne, connect, coord, E, dens, A, x)

    tasks = ((theta_x[i], theta_y[i]) for i in range(len(theta_y)))
    
    bands = Parallel(n_jobs=-1)(delayed(compute_eig)(Lx, Ly, nx, ny, bigk, bigm, nav, x, y) for (x, y) in tasks)
    bands = np.array(bands).T
        
    ic(bands)
    ic(np.shape(bands))
    return bands

def compute_eig(Lx, Ly, nx, ny, bigk, bigm, nav, x, y):
    T_m = T_matrix(Lx, Ly, nx, ny, x, y)
    adT = np.matrix(T_m).H
    K = np.round(adT @ bigk @ T_m, 15)
    M = np.round(adT @ bigm @ T_m, 15)
    # Llamar a eigs con la tolerancia y el número máximo de iteraciones
    values, _ = eigs(K, k=nav, M=M, which='SM')
    vals = np.real(values)
    band = np.sort(np.sqrt(vals), axis=None)
    return band
