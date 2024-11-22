import numpy as np

def Symmetry_Map_FBZ(n):
    n2 = n // 2
    barnumber = (n * (n + 1)) + (n * (n + 1)) + 2 * n * n
    varnumber = 2 * n2 * (n2 + 1)
    MAP = np.zeros((barnumber, varnumber))

    # ----- Primer cuadrante
    # Barras horizontales
    k = 1
    number = 1
    for j in range(1, n2+1):
        for i in range(number, n2 + 1):
            MAP[i + n*(j - 1) -1, k - 1] = 1
            k += 1
        number += 1



    # Barras Verticales
    number = 1
    for j in range(1, n2+1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + 1 + i + (j - 1)*(n + 1) - 1, k - 1] = 1 #n*(n+1)+1+i+(j-1)*(n+1)
            k += 1
        number += 1
    
    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + i + (j - 1)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n + i + (j - 1)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # ------ Segundo cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n + 1 - i + n*(j - 1) - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + n + 1 - i + (j - 1)*(n + 1) - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n + n + (1 - i) + (j - 1)*n - 1, k - 1] = 1
            k += 1
        number += 1
    
    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n + (1 - i) + (j - 1)*n - 1, k - 1] = 1
            k += 1
        number += 1 

    # ------ Tercer cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + (i)*(n + 1) + 1 - j - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n + n + 1 - j + (i - 1)*n - 1,k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n + n + (i - 1)*n + (1 - j) - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n + (i - 1)*n + (1 - j) - 1,k - 1] = 1
            k += 1
        number += 1

    # ------ Cuarto cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + n*(n + 1)+(1 - j)+(1 - i)*(n + 1) - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*n + (1 - i)*n + (1 - j) - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n + (1 - i)*n + (1 - j) - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + 2*n*n + (1 - i)*n + (1 - j) - 1, k - 1] = 1
            k += 1
        number += 1

    # ------ Quinto cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + (1 - i) + (1 - j)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + n*(n + 1) + (-i) + (1 - j)*(n + 1) - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n + (1 - i) + (1 - j)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + 2*n*n + (1 - i) + (1 - j)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # ------ Sexto cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*n + i + (1 - j)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1)+ n*(n + 1) - n + i + (1 - j)*(n + 1) - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + 2*n*n - n + i + (1 - j)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n - n + i + (1 - j)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # ------ Séptimo cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*n + n*(n + 1) + (1 - i)*(n + 1) + (j - 1) - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n - 1) + (1 - i)*n + j - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + 2*n*n - n + (1 - i)*n + j - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n - n + (1 - i)*n + j - 1,k - 1] = 1
            k += 1
        number += 1

    # ------ Octavo cuadrante
    # Barras horizontales _
    k = 1
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n*(n + 1) + (i - 1)*(n + 1)+ j - 1, k - 1] = 1
            k += 1
        number += 1

    # Barras Verticales |
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[n + (i - 1)*(n) + j - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas /
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + j + (i - 1)*n - 1, k - 1] = 1
            k += 1
        number += 1

    # Inclinadas \
    number = 1
    for j in range(1, n2 + 1):
        for i in range(number, n2 + 1):
            MAP[2*n*(n + 1) + n*n + j + (i - 1)*n - 1, k - 1] = 1
            k += 1
        number += 1

    return MAP

