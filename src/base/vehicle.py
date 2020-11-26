#  Copyright (c) 2020. Lars Hackstein, Holger Schneider
import numpy as np

class Vehicle:
    """
    A Container encapsulates all necessary parameters like loading capacity, cost parameters or maximal route duration.
    """
    def __init__(self, name, restrictions, metric):
        self.name = name
        self.restrictions = restrictions
        self.metric = metric

    def __str__(self):
        return f"Vehicle({self.name!r})"

    def __repr__(self):
        return f"Vehicle({self.name!r}, {self.restrictions!r})"

    def check(self, tour):
        return np.sum(n.demand for n in tour) <= self.restrictions['capacity']
