import numpy as np
import matplotlib.pyplot as plt

def plot_structure(ne, connect, coord, xbeam_area, xbeam_mat):
    coord = coord * 100
    fig, ax = plt.subplots()
    
    for ele in range(ne):
        # recover the nodes
        node = connect[ele, :]

        # recover the coordinates
        vect1 = coord[node[0], :]
        vect2 = coord[node[1], :]

        # Adds a line to the plot
        if xbeam_mat[ele] == 0.0:
            ax.plot([vect1[0], vect2[0]], [vect1[1], vect2[1]], color="b", linewidth=1 + 3 * xbeam_area[ele])
        elif xbeam_mat[ele] == 1.0:
            ax.plot([vect1[0], vect2[0]], [vect1[1], vect2[1]], color="r", linewidth=1 + 3 * xbeam_area[ele])
    
    ax.plot(np.nan, np.nan, 'b')
    ax.plot(np.nan, np.nan, 'r')
    ax.plot(np.nan, np.nan, 'b', linewidth=4)
    ax.plot(np.nan, np.nan, 'r', linewidth=4)
    
    ax.set_ylabel('Length [cm]', fontsize=12)
    ax.set_xlabel('Width [cm]', fontsize=12)
    ax.set_title('(b)', fontsize=12)
    
    ax.set_xlim([0, coord[-1, -1]])
    ax.set_ylim([0, coord[-1, -1]])
    plt.show()

