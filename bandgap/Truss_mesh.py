import numpy as np

def Truss_mesh(Lx, nx, Ly, ny):
    nn = (nx + 1) * (ny + 1)
    ne = nx * (ny + 1) + ny * (nx + 1) + 2 * nx * ny
    coord = np.zeros((nn, 2))
    connect = np.zeros((ne, 2),dtype= int)

    dx = Lx / nx
    dy = Ly / ny

    x = -dx
    y = -dy

    cont = 0
    for i in range(ny + 1):
        y += dy
        for j in range(nx + 1):
            x += dx
            cont += 1
            coord[cont - 1, 0] = x
            coord[cont - 1, 1] = y
        x = -dx

    no1 = 0
    no2 = 1
    cont = 0
    for i in range(ny + 1):
        for j in range(nx):
            no1 += 1
            no2 += 1
            cont += 1
            connect[cont - 1, 0] = no1
            connect[cont - 1, 1] = no2
        no1 += 1
        no2 += 1

    no1 = 0
    no2 = nx + 1
    for i in range(ny):
        for j in range(nx + 1):
            no1 += 1
            no2 += 1
            cont += 1
            connect[cont - 1, 0] = no1
            connect[cont - 1, 1] = no2

    no1 = 0
    no2 = nx + 2
    for i in range(ny):
        for j in range(nx):
            no1 += 1
            no2 += 1
            cont += 1
            connect[cont - 1, 0] = no1
            connect[cont - 1, 1] = no2
        no1 += 1
        no2 += 1

    no1 = 1
    no2 = nx + 1
    for i in range(ny):
        for j in range(nx):
            no1 += 1
            no2 += 1
            cont += 1
            connect[cont - 1, 0] = no1
            connect[cont - 1, 1] = no2
        no1 += 1
        no2 += 1

    return nn, ne, coord, connect-1