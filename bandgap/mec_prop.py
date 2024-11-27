import numpy as np

def mec_prop(ne, Prop):
    # Use the aluminum properties in material 1 and the tungsten as 2.
    # A1 = Prop['A1']  # [m²]
    # Young_Modulus1 = Prop['ym1']  # [Pa]
    # Density1 = Prop['d1']  # [Kg/m³]
    # A2 = Prop['A2']  # [m²]
    # Young_Modulus2 = Prop['ym2']  # [Pa]
    # Density2 = Prop['d2']  # [Kg/m³]
    D1 = Prop.D1
    Young_Modulus1 = Prop.ym1
    Density1 = Prop.d1

    D2 = Prop.D2
    Young_Modulus2 = Prop.ym2
    Density2 = Prop.d2

    E = np.ones((ne, 2))
    D = np.ones((ne, 2))
    rho = np.ones((ne, 2))
    
    var = Prop.var if Prop.var != None else 0
    
    
    distribution = lambda x, var : np.random.uniform(x* (1 - var), x * (1 + var), ne)

    E[:, 0] = distribution(Young_Modulus1, var)
    rho[:, 0] = distribution(Density1, var)
    D[:, 0] = distribution(D1, var)
    
    E[:, 1] = distribution(Young_Modulus2, var)
    rho[:, 1] = distribution(Density2, var)
    D[:, 1] = distribution(D2, var)
    
    A = np.pi * D**2 / 4
    
    return rho, E, A
