import numpy as np
import matplotlib.pyplot as plt

def plot_bands(data, n):
    fig, ax = plt.subplots()
    band1 = data.T
    
    x_lim = data.shape[1]
    # Usamos el argumento `color` para especificar el color azul
    ax.plot(band1, color='blue')
    
    # Establecemos los límites de los ejes
    ax.set_xlim([1, x_lim])  # Límites del eje x
    ax.set_ylim([0, np.max(np.max(band1))])  # Límites del eje y
    
    # Calcular maximo, minimo, delta y media para la zona rellena
    maximo = np.max(band1[:,n-1])  # Maximo de la columna n (Python usa índices 0-basados)
    minimo = np.min(band1[:,n])    # Minimo de la columna n+1
    delta = minimo - maximo
    media = (maximo + minimo) / 2
    
    # Añadir texto en la gráfica
    txt = r'$\Delta\omega =$ ' + str(round(delta, 2)) + ' [kHz]'
    ax.text(x_lim/2 - 2, media, txt, fontsize=12, ha='center', va='center', 
            color='black', weight='bold', style='italic', 
            usetex=True)
    
    # Rellenar el área entre maximo y minimo
    ax.fill([0, x_lim, x_lim, 0], [minimo, minimo, maximo, maximo], 'k', 
            linestyle='none', alpha=0.25)
    
    # Añadir líneas horizontales en maximo y minimo
    ax.plot([0, x_lim], [maximo, maximo], 'k-', linewidth=0.1)
    ax.plot([0, x_lim], [minimo, minimo], 'k-', linewidth=0.1)
    
    # Añadir la grilla
    ax.grid(True)
    
    # Título de la gráfica con LaTeX habilitado
    ax.set_title(f'n = {n}', fontsize=12, usetex=True)
 
     # Establecemos los límites de los ejes
    ax.set_xlim([1, x_lim])  # Límites del eje x
    ax.set_ylim([0, np.max(np.max(band1))])  # Límites del eje y
    
    # Etiquetas de los ejes con formato LaTeX
    ax.set_xlabel(r'Wave vector', fontsize=12)
    ax.set_ylabel(r'Frequency [kHz]', fontsize=12)
    
    # Establecemos las posiciones de las etiquetas en el eje x
    ax.set_xticks([1, 20, 40, 60])  # Posiciones específicas en el eje x
    
    # Asignamos las etiquetas del eje x
    ax.set_xticklabels([r'$\Gamma$', r'$X_{1}$', r'$M_{1}$', r'$\Gamma$'])
    
    plt.show()