from bandgap.plot_structure import plot_structure
from bandgap.plot_bands import plot_bands
from bandgap.band_gap import band_gap
from dataclasses import dataclass, field
import numpy as np
import copy

@dataclass
class truss_like:
    gens: np.ndarray
    age: int = 0
    ym1: float = 70e9
    ym2: float = 411e9
    d1: float = 2.7e3
    d2: float = 19.3e3
    D1: float = 0.004
    D2 = None
    n: int = 3
    nint: int  = 20
    data_plot = None
    bandgap = None
    data_bandgap = None
    pm = None
    var: float = field(default=0)

    def __post_init__(self):
        self.D2 = self.D1 * 2 if self.D2 is None else self.D2
        self.A1 = np.pi * (self.D1 ** 2) / 4
        self.A2 = np.pi * (self.D2 ** 2) / 4

    def __eq__(self, other):
        return np.array_equal(self.gens, other.gens)

    def evaluate(self):
        
        self.bandgap, self.data_bandgap = band_gap(self)
        
        points = self.bandgap if self.bandgap >0.01 else 0.01
        return points,

    def mutate(self):
        flip_bit = lambda x: 1 - x
        i = np.random.rand(*self.gens.shape)
    
        self.gens = np.where(i <= self.pm, 
                 flip_bit(self.gens),
                 self.gens)
    
        return self,

    def clone(self):
        return copy.deepcopy(self)

    def structure(self):
        plot_structure(*self.data_plot)

    def band_diagram(self):
        plot_bands(self.data_bandgap, self.n)
    
    def plot(self):
        self.structure()
        self.band_diagram()
        