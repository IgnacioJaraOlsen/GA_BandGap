import numpy as np

from bandgap.Bands import Bands
from bandgap.mec_prop import mec_prop

import numba as nb


def band_gap(Prop, n, Lx, Ly, nx, ny, ne, coord, connect, x_expanded, nav, theta_x, theta_y):
    rho, E, A = mec_prop(ne, Prop)
    opt_band_diagram = Bands(Lx, Ly, nx, ny, ne, coord, connect, E, A, rho, np.round(x_expanded), nav, theta_x, theta_y) / (2 * np.pi)
    data = opt_band_diagram / 1000

    band1 = data.T
    band2 = band1.copy()

    maximo = np.max(band2[:, n - 1])
    minimo = np.min(band2[:, n])
    delta = minimo - maximo
    
    return delta, data