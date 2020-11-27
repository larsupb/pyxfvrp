#  Copyright (c) 2020. Lars Hackstein, Holger Schneider
import numpy as np


def normalize_route(giant_route):
    """
    Reformats route in form of
        <Depot><Stop1>..<StopN><Depot><Depot><Stop1>..<StopN><Depot>
    to target form of
        <Depot><Stop1>..<StopN><Depot><Stop1>..<StopN><Depot>
    :param giant_route: original giant route
    :return reformated giant route in target form:
    """
    if len(giant_route) > 1:
        giant_route = [r[:-1] for r in giant_route[:-1]] + [np.array([r for r in giant_route[-1]])]
    giant_route = np.concatenate(giant_route).ravel().tolist()
    return giant_route


def clean_empty_routes(giant_route):
    """
    Reformats route in form of
        <Depot><Stop1>..<StopN><Depot><Depot><Stop1>..<StopN><Depot>
    to target form of
        <Depot><Stop1>..<StopN><Depot><Stop1>..<StopN><Depot>
    :param giant_route: original giant route
    :return reformated giant route in target form:
    """

    cleaned = []
    for i in range(len(giant_route)-1):
        if not giant_route[i].is_depot and giant_route[i+1].is_depot:
            cleaned.append(giant_route[i])
    return cleaned
