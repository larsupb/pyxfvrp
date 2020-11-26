#  Copyright (c) 2020. Lars Hackstein, Holger Schneider


class Node:
    """
     Nodes are the basic structure of this optimization model. The route representation
     relies on nodes. Depots and customers are both Node objects, whereas the site type differs
     between the two types.
     """
    def __init__(self, ident, geo_id, demand, requirements=None):
        self.ident = ident
        self.geo_id = geo_id
        self.demand = demand
        self.requirements = requirements

    def __str__(self):
        return f"Node({self.ident!r}, {self.geo_id.coords[0]!r})"

    def __repr__(self):
        return f"Node({self.geo_id.coords[0]!r})"
