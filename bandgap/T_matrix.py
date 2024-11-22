import numpy as np
from scipy.sparse import csc_matrix, coo_matrix
import os

import numba as nb

def T_matrix(Lx, Ly, nx, ny, theta_a, theta_b):
    ndofs = 2 * (nx + 1) * (ny + 1)
    ncols = ndofs - 6 - 2 * (nx - 1) - 2 * (ny - 1)
    
    exphia = np.exp(1j * theta_a * Lx)
    exphib = np.exp(1j * theta_b * Ly)
    exphiab = np.exp(1j * (theta_a * Lx + theta_b * Ly))
    #print(f'{exphia =}')
    #print(f'{exphib =}')
    #print(f'{exphiab =}')
    
    hint = 2 * (2 * (nx - 1) + 2 * (ny - 1) + (nx - 1) * (ny - 1))
    VI = []
    VJ = []
    VV = []
    
    C2 = (nx + 1)
    C3 = (nx + 1) * ny + 1
    C4 = (nx + 1) * (ny + 1)
    col = 1
    
    # X direction, 1-1
    VI.extend([col])
    VJ.extend([col])
    VV.extend([1])

    # X direction, 1-C2
    VI.extend([2 * (C2 - 1) + 1])
    VJ.extend([col])
    VV.extend([exphia])

    # X direction, 1-C3
    VJ.extend([col])
    VI.extend([2 * (C3 - 1) + 1])
    VV.extend([exphib])

    # X direction, 1-C4
    VJ.extend([col])
    VI.extend([2 * (C4 - 1) + 1])
    VV.extend([exphiab])

    col = col + 1

    # Y direction, 1-1
    VI.extend([col])
    VJ.extend([col])
    VV.extend([1.0])

    # Y direction, 1-C2
    VJ.extend([col])
    VI.extend([2 * (C2 - 1) + 2])
    VV.extend([exphia])

    # Y direction, 1-C3
    VJ.extend([col])
    VI.extend([2 * (C3 - 1) + 2])
    VV.extend([exphib])

    # Y direction, 1-C4
    VJ.extend([col])
    VI.extend([2 * (C4 - 1) + 2])
    VV.extend([exphiab])

    node_top = C3 + 1
    for node_bottom in range(2, nx + 1):
        col = col + 1

        # X direction, node_bottom - node_bottom
        VI.extend([2 * (node_bottom - 1) + 1])
        VJ.extend([col])
        VV.extend([1.0])

        # X direction, node_bottom - node_top
        VI.extend([2 * (node_top - 1) + 1])
        VJ.extend([col])
        VV.extend([exphib])

        col = col + 1

        # Y direction, node_bottom - node_bottom
        VI.extend([2 * (node_bottom - 1) + 2])
        VJ.extend([col])
        VV.extend([1.0])

        # Y direction, node_bottom - node_top
        VI.extend([2 * (node_top - 1) + 2])
        VJ.extend([col])
        VV.extend([exphib])

        node_top = node_top + 1

    node_rigth = C2 + nx + 1
    for node_left in range(C2 + 1, C3 - nx + 1, nx + 1):
        col = col + 1

        # X direction, left node - left node
        VI.extend([2 * (node_left - 1) + 1])
        VJ.extend([col])
        VV.extend([1.0])

        # X direction, left node - rigth node
        VI.extend([2 * (node_rigth - 1) + 1])
        VJ.extend([col])
        VV.extend([exphia])

        col = col + 1

        # Y direction, node_bottom - node_bottom
        VI.extend([2 * (node_left - 1) + 2])
        VJ.extend([col])
        VV.extend([1.0])

        # Y direction, node_bottom - node_top
        VI.extend([2 * (node_rigth - 1) + 2])
        VJ.extend([col])
        VV.extend([exphia])

        node_rigth = node_rigth + (nx + 1)

    node = C2 + 2
    for _ in range(1, nx):
        for _ in range(1, ny):
            col = col + 1

            # X direction
            VI.extend([2 * (node - 1) + 1])
            VJ.extend([col])
            VV.extend([1.0])

            col = col + 1

            # Y direction
            VI.extend([2 * (node - 1) + 2])
            VJ.extend([col])
            VV.extend([1.0])

            node = node + 1

        node = node + 2

    # Create the sparse matriz
    VI = np.array(VI) - 1
    VJ = np.array(VJ) - 1
    VV = np.array(VV)

    T = coo_matrix((VV, (VI, VJ)), shape=(ndofs, ncols)).toarray()

    return T


if __name__ == "__main__":
    os.system('cls')
    Lx = 0.1000
    Ly = 0.1000
    nx = 1
    ny = 1
    theta_a = 1.0000e-03
    theta_b = 1.0000e-03

    T = T_matrix(Lx, Ly, nx, ny, theta_a, theta_b)
    print(T)


