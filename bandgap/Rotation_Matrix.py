import numpy as np

def Rotation_Matrix(theta):
    c = np.cos(theta)
    s = np.sin(theta)
    
    R = np.array([[c, -s, 0, 0],
                  [s, c, 0, 0],
                  [0, 0, c, -s],
                  [0, 0, s, c]])
    
    return R