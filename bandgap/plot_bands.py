import numpy as np
import matplotlib.pyplot as plt

def plot_bands(data, n):
    fig, ax = plt.subplots()
    band1= data.T
    
    ax.plot(band1)
    plt.show()