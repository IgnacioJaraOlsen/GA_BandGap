import numpy as np
import random

def adaptive_crossover_probability(f):
    # calcula las probabilidades de cruzamiento de los individuos 
    f = list(f)
    f_max = np.max(f)
    f_mean = np.mean(f)
    
    num = f_max - f
    den = f_max - f_mean
    
    if np.isclose(den, 0, atol=1e-3):
        p = lambda f : 0.3 * np.divide(num, den)
    else:
        p = lambda f: 0.3
    
    pc = np.where(f >= f_mean, 
                  p(f), 
                  0.9)
    return pc

def adaptive_mutation_probability(f, pm, _lambda = 0.7):
    f = list(f)
    f = np.squeeze(f)
    #_lambda = random.random()
    # calcula las probabilidades de mutación
    sum_num  = 0
    sum_den = 0
    n = len(f)
    std = np.std(f)
    for k in range(n - 1):
        lambda_k = _lambda ** k
        diff_f = f[n-1-k] - f[n-1-k-1]
        abs_diff_f = np.abs(diff_f)
        sum_num += lambda_k * diff_f
        sum_den += lambda_k * abs_diff_f
    
    pm = (1 - sum_num/sum_den) * pm if sum_den != 0 else pm
    
    
    return min(pm, 1)