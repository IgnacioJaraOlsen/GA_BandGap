import numpy as np

from bandgap.eig_bands import eig_bands
from bandgap.mec_prop import mec_prop
from bandgap.Truss_mesh import Truss_mesh
from bandgap.Symmetry_Map_FBZ import Symmetry_Map_FBZ
from bandgap.wave_vector import wave_vector

import numba as nb


def bands(Prop, n, Lx, Ly, nx, ny, ne, coord, connect, x_expanded, nav, theta_x, theta_y):
    rho, E, A = mec_prop(ne, Prop)
    opt_band_diagram = eig_bands(Lx, Ly, nx, ny, ne, coord, connect, E, A, rho, np.round(x_expanded), nav, theta_x, theta_y) / (2 * np.pi)
    data = opt_band_diagram / 1000

    band1 = data.T
    band2 = band1.copy()

    maximo = np.max(band2[:, n - 1])
    minimo = np.min(band2[:, n])
    delta = minimo - maximo
    
    return delta, data

def band_gap(struct):
    Lac = 0.025
    Lpc = Lac
    nc = 4
    nx = nc
    ny = nc
    Lc = Lpc*nc
    Lx = Lc
    Ly = Lc
    
    nn, ne, coord, connect = Truss_mesh(Lx,nx,Ly,ny)
    
    S = Symmetry_Map_FBZ(nc)
    nxred = S.shape[1]
    
    xa = struct.gens[0,:]
    xm = struct.gens[1,:]
    
    xm = np.array([xm])
    xa = np.array([xa])
    
    xm = xm.T
    xa = xa.T
    
    xf = np.vstack((xm, xa))
    
    x = np.round(xf)
    
    xm = x[:nxred]
    xa = x[nxred:2*nxred]
    x_mat = np.dot(S, xm)
    x_area = np.dot(S, xa)
    x_expanded = np.hstack((x_mat, x_area))
    
    n = struct.n
    
    nav = n + 3
    
    NINT = struct.nint
    
    theta_x, theta_y = wave_vector(NINT,Lx,Ly,0)
    
    struct.data_plot = ne,connect,coord,x_area,x_mat
    
    delta, data = bands(struct, n, Lx, Ly, nx, ny, ne, coord, connect, x_expanded, nav, theta_x, theta_y)
    
    return delta, data