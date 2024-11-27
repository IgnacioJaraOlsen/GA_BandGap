from deap import tools, algorithms
from genetic_algorithm import probabilities
from collections import Counter
import numpy as np
import random
import tqdm


def eval(population):
    """
    esta función solo se puede utilizar si no hay variación 
    en los materiales que conforman la estructura debido a que
    se reutiliza los valores calculados si hay gens repetidos
    """
    todos_genes = []
    
    # Recopilar todos los genes de la población
    for ind in population:
        todos_genes.extend(ind.gens)

    # Contar las ocurrencias de los elementos
    contador_genes = Counter(todos_genes)

    # Filtrar los elementos que se repiten o aparecen solo una vez
    todos_genes_filtrados = [gen for gen, count in contador_genes.items() if count > 0]
    
    # Filtrar individuos con genes no calculados (invalidos)
    invalid_ind = [ind for ind in population if not ind.fitness.valid]

    # Buscar los individuos válidos que tengan los mismos genes
    for ind in invalid_ind:
        # Buscar un individuo válido con los mismos genes
        matching_valid_individual = next((valid_ind for valid_ind in population 
                                          if valid_ind.fitness.valid and valid_ind.gens == ind.gens), None)
        
        if matching_valid_individual:
            # Asignar el 'fitness' del individuo válido con los mismos genes
            ind.fitness.values = matching_valid_individual.fitness.values
            ind.fitness.valid = True  # Marcar el fitness como válido

    return population

def var(population, toolbox,):
    offspring = []
    for _ in range(len(population)*2):
        ind1, ind2 = [toolbox.clone(i) for i in random.sample(population, 2)]
        oldgens = ind1.gens
        
        ind1, ind2 = toolbox.mate(ind1, ind2)
        
        ind1, = toolbox.mutate(ind1)
        
        if not np.array_equal(oldgens, ind1.gens):
            del ind1.fitness.values
        
        offspring.append(ind1)

    return offspring

#__debug__
def ea(population, toolbox, ngen,
          stats=None, halloffame=None, verbose=False, _lambda = 0.9):
    
    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in population if not ind.fitness.valid]  if population[0].var == 0 else population
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)

    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    # Select the next generation population
    population[:] = toolbox.select(population, len(population)//2)
    
    if halloffame is not None:
        halloffame.update(population)

    logbook = tools.Logbook()
    logbook.header = ['gen', 'nevals', 'pm'] + (stats.fields if stats else [])
    
    record = stats.compile(population) if stats is not None else {}
    logbook.record(gen=0, nevals=len(invalid_ind), **record)
    if verbose:
        print(logbook.stream)    
    
    pc = 0.9
    pm = 0.05
    
    with tqdm.tqdm(total=ngen) as pbar:
        for gen in range(1, ngen + 1):
            
            selected_fitnesses = [ind.fitness.values for ind in population]
            
            pc = probabilities.adaptive_crossover_probability(selected_fitnesses) if gen != 1 else np.full(len(population), pc)
            pm = probabilities.adaptive_mutation_probability(selected_fitnesses, pm, _lambda = _lambda) if gen != 1 else pm
            
            for ind, pc_i in zip(population, pc):
                ind.pc = pc_i
                ind.pm = pm
            
            # Vary the population
            offspring = var(population, toolbox)
            
            # Evaluate the individuals with an invalid fitness
            invalid_ind = [ind for ind in offspring if not ind.fitness.valid] if offspring[0].var == 0 else offspring
            fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
            for ind, fit in zip(invalid_ind, fitnesses):
                ind.fitness.values = fit
            
            # Update the hall of fame with the generated individuals
            if halloffame is not None:
                halloffame.update(offspring)
            
            # Select the next generation population
            population[:] = toolbox.select(offspring, len(offspring)//2)
            
            # Update the statistics with the new population
            record = stats.compile(population) if stats is not None else {}
            logbook.record(gen=gen, nevals=len(invalid_ind), pm = round(pm*100,1), **record)
            if verbose:
                print(logbook.stream)
            
            pbar.update(1)
            pbar.set_description(f"pm:{pm*100:.1f}")
        
    return population, logbook    
        