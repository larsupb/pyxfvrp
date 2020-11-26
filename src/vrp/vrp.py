#  Copyright (c) 2020. Lars Hackstein, Holger Schneider
import numpy as np

from src.base import Vehicle, Node
from .savings import savings


class VRP:
    """
    The Vehicle Routing Problem (VPR) (from Wikipedia)

    VRP is a combinatorial optimization and integer programming problem which asks "What is the optimal set of routes
    for a fleet of vehicles to traverse in order to deliver to a given set of customers?". It generalises the well-known
    travelling salesman problem (TSP).

    It first appeared in a paper by George Dantzig and John Ramser in 1959,[1] in which the first algorithmic approach
    was written and was applied to petrol deliveries. Often, the context is that of delivering goods located at a
    central depot to customers who have placed orders for such goods. The objective of the VRP is to minimize the total
    route cost. In 1964, Clarke and Wright improved on Dantzig and Ramser's approach using an effective greedy approach
    called the savings algorithm.

    Determining the optimal solution to VRP is NP-hard,[2] so the size of problems that can be solved, optimally,
    using mathematical programming or combinatorial optimization may be limited. Therefore, commercial solvers tend to
    use heuristics due to the size and frequency of real world VRPs they need to solve.
    """

    def __init__(self, demands, depot: Node, vehicle: Vehicle):
        self.demands = demands
        self.depot = depot
        self.vehicle = vehicle

    def run(self):
        route = self.build_giant_route()
        route = savings(route, self.vehicle)


    def build_giant_route(self):
        return [(self.depot, n, self.depot) for n in self.demands]




