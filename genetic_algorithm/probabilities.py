import numpy as np
import random

def adaptive_crossover_probability(f):
    # Convierte la lista a un array de NumPy
    f = np.array(f)
    f_max = np.max(f)
    f_mean = np.mean(f)
    
    num = f_max - f
    den = f_max - f_mean
    
    # Evitar divisiones por cero ajustando el denominador con un valor muy pequeño
    den = np.where(np.isclose(den, 0, atol=1e-10), 1e-10, den)
    
    # Calcular las probabilidades de cruzamiento
    p = 0.3 * np.divide(num, den)
    
    # Manejar casos donde f >= f_mean y f < f_mean
    pc = np.where(f >= f_mean, p, 0.9)
    
    return pc

def adaptive_mutation_probability(f, pm, _lambda = 0.5):
    f = list(f)
    f = np.squeeze(f)
    
    x = - _lambda * (f[-1] - np.max(f[:-1]))/np.max(f[:-1])
    
    factor = (2/ (1 + np.exp(-x))) - 1
    
    #  sum_num/sum_den *
    
    pm = (1 -  factor ) * pm  if pm < 0.10 else pm
    
    
    return min(pm, 1)