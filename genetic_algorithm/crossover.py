import numpy as np
import random

def horizontal_crossover(ind1, ind2):
    """Realiza cruza horizontal entre dos padres."""
    crossover_point = np.random.randint(1, ind1.gens.shape[1] - 1, size=2)
    
    child1 = ind1.clone()
    child2 = ind2.clone()
    
    # Use np.hstack for horizontal concatenation
    child1.gens[0,:] = np.hstack((ind1.gens[0, :crossover_point[0]], ind2.gens[0, crossover_point[0]:]))
    child2.gens[0,:] = np.hstack((ind2.gens[0, :crossover_point[0]], ind1.gens[0, crossover_point[0]:]))
    
    child1.gens[1,:] = np.hstack((ind1.gens[1, :crossover_point[1]], ind2.gens[1, crossover_point[1]:]))
    child2.gens[1,:] = np.hstack((ind2.gens[1, :crossover_point[1]], ind1.gens[1, crossover_point[1]:]))
    
    return child1, child2

def vertical_crossover(ind1, ind2):
    """Realiza cruza vertical entre dos padres."""
    mask1 = np.random.randint(0, 2, ind1.gens.shape[1])
    mask2 = np.random.randint(0, 2, ind1.gens.shape[1])
    masks = [mask1, mask2]
    child1 = ind1.clone()
    child2 = ind2.clone()
    
    cross1 = lambda x : np.array([p1 if m else p2 for p1, p2, m in zip(ind1.gens[x,:], ind2.gens[x,:], masks[x])])
    cross2 = lambda x : np.array([p2 if m else p1 for p1, p2, m in zip(ind1.gens[x,:], ind2.gens[x,:], masks[x])])
    
    for i in range(2):
        child1.gens[i,:] = cross1(i)
        child2.gens[i,:] = cross2(i)
        
    return child1, child2

def mix_crossover(ind1, ind2):
    pc = min(ind1.pc, ind2.pc)
    delta = random.random()

    if delta < pc:
        if random.random() > 0.5:  # cruza horizontal
            child1, child2 = horizontal_crossover(ind1, ind2)
        else:  # cruza vertical
            child1, child2 = vertical_crossover(ind1, ind2)
    else:
        child1, child2 = ind1.clone(), ind2.clone() 
    
    return child1, child2