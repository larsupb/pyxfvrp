#  Copyright (c) 2020. Lars Hackstein, Holger Schneider
import numpy as np


class Relocate:
    class Improvement:
        __slots__ = ['i', 'j', 'objective']

        def __init__(self, i, j, objective):
            self.i = i
            self.j = j
            self.objective = objective

    EPSILON = 0.001

    def __init__(self, vehicle):
        self.vehicle = vehicle

    def improve(self, giant_route):
        best_objective = None
        best_route = giant_route.copy()
        while True:
            imp_found = False
            alternatives = self.search(best_route)
            for (i, j) in alternatives:
                obj = self.vehicle.evaluate(self.move(best_route, int(i), int(j)))
                if best_objective is None or obj < best_objective:
                    best_objective = obj
                    best_route = self.move(best_route, i, j)
                    imp_found = True
                    print(best_objective, len(best_route))
                    break
            if not imp_found:
                break
        return best_route

    def search(self, giant_route):
        steps = []
        step_val = []
        for src in range(1, len(giant_route)-1):
            for dst in range(1, len(giant_route)-1):
                if giant_route[dst].is_depot:
                    continue
                if src == dst or dst - src == 1:
                    continue

                val = 0
                if src - dst == 1:
                    # Calculate distances for IS
                    val += self.vehicle.metric(giant_route[src], giant_route[src+1])
                    val += self.vehicle.metric(giant_route[dst], giant_route[src])
                    val += self.vehicle.metric(giant_route[dst-1], giant_route[dst])
                    # Calculate distances for TARGET
                    val -= self.vehicle.metric(giant_route[dst], giant_route[src+1])
                    val -= self.vehicle.metric(giant_route[src], giant_route[dst])
                    val -= self.vehicle.metric(giant_route[dst-1], giant_route[src])
                else:
                    # Calculate distances for IS
                    val += self.vehicle.metric(giant_route[src-1], giant_route[src])
                    val += self.vehicle.metric(giant_route[src], giant_route[src+1])
                    val += self.vehicle.metric(giant_route[dst-1], giant_route[dst])
                    # Calculate distances for TARGET
                    val -= self.vehicle.metric(giant_route[src-1], giant_route[src+1])
                    val -= self.vehicle.metric(giant_route[src], giant_route[dst])
                    val -= self.vehicle.metric(giant_route[dst-1], giant_route[src])

                if val > Relocate.EPSILON:
                    step_val.append(val)
                    steps.append((src, dst))

        print(f'Generated {len(steps)} possible improvements.')
        if len(steps) == 0:
            return []

        indices = np.argsort(-np.array(step_val))
        steps = np.array(steps)
        return steps[indices]  # Sorted by value

    @staticmethod
    def move(giant_route, src, dst):
        if src == dst:
            return giant_route
        s, d = min(src, dst), max(src, dst)
        out = np.concatenate([giant_route[:s], [giant_route[d]], giant_route[s:d], giant_route[d+1:]])
        return out



