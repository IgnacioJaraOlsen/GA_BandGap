import numpy as np

def mec_prop(ne, Prop):
    # Use the aluminum properties in material 1 and the tungsten as 2.
    # A1 = Prop['A1']  # [m²]
    # Young_Modulus1 = Prop['ym1']  # [Pa]
    # Density1 = Prop['d1']  # [Kg/m³]
    # A2 = Prop['A2']  # [m²]
    # Young_Modulus2 = Prop['ym2']  # [Pa]
    # Density2 = Prop['d2']  # [Kg/m³]
    A1 = Prop.A1
    Young_Modulus1 = Prop.ym1
    Density1 = Prop.d1

    A2 = Prop.A2
    Young_Modulus2 = Prop.ym2
    Density2 = Prop.d2

    E = np.ones((ne, 2))
    A = np.ones((ne, 2))
    rho = np.ones((ne, 2))

    E[:, 0] = Young_Modulus1 * np.ones(ne)
    rho[:, 0] = Density1 * np.ones(ne)
    A[:, 0] = A1 * np.ones(ne)
    E[:, 1] = Young_Modulus2 * np.ones(ne)
    rho[:, 1] = Density2 * np.ones(ne)
    A[:, 1] = A2 * np.ones(ne)
    
    return rho, E, A
