#  Copyright (c) 2020. Lars Hackstein, Holger Schneider
import numpy as np


def savings(giant_route, vehicle):
        """
        Savings Algorithm (Clarke & Wright's Saving Algorithm) extended by multi-tour aspect
        """
        while True:
            savings = [vehicle.metric(r1[-2], r1[-1]) + vehicle.metric(r2[0], r2[1]) - vehicle.metric(r1[-2], r2[1])
                       for i, r1 in enumerate(giant_route)
                       for j, r2 in enumerate(giant_route)]
            savings = np.array(savings)

            giant_route_new = []

            modified = dict()
            for idx in np.argsort(-savings):
                r1, r2 = int(idx / len(giant_route)), int(idx % len(giant_route))
                if r1 == r2 or r1 in modified or r2 in modified:
                    continue
                merge = np.concatenate([giant_route[r1][:-1], giant_route[r2][1:]])
                if vehicle.check(merge):
                    modified[r1] = None
                    modified[r2] = None
                    giant_route_new.append(merge)

            if len(modified) == 0:
                break

            for i, r0 in enumerate(giant_route):
                if i not in modified:
                    giant_route_new.append(r0)

            giant_route = giant_route_new


            print(len(giant_route))

        return giant_route



