import random

def select_individuals_elitist(individuals, k):
    """Selecciona individuos basados en competencia por pares aleatorios dobles."""
    selected = []
    for _ in range(k):
        c1, c2 = random.sample(individuals, 2)
        c1_prime, c2_prime = random.sample(individuals, 2)
        
        best_of_c1_c2 = c1 if c1.fitness > c2.fitness else c2
        best_of_c1_prime_c2_prime = c1_prime if c1_prime.fitness > c2_prime.fitness else c2_prime
        
        selected.append(best_of_c1_c2 if best_of_c1_c2.fitness > best_of_c1_prime_c2_prime.fitness else best_of_c1_prime_c2_prime)
    
    return selected