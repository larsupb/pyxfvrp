#  Copyright (c) 2020. Lars Hackstein, Holger Schneider
import numpy as np
import pandas as pd

from src.vrp import VRP
from src.base import Node, Vehicle

from shapely.geometry import Point

if __name__ == '__main__':
    data = pd.read_excel('../datasets/Test.100.xls', sheet_name='Eingabedaten')

    depot = data.iloc[0, :]
    depot = Node(ident=depot['ORT_ID'], geo_id=Point(depot[['YLAT', 'XLONG']]), demand=0, is_depot=True)

    demands = [Node(ident=d['ORT_ID'], geo_id=Point(d[['YLAT', 'XLONG']]), demand=d['MENGE'])
               for i, d in data.iterrows() if i > 0]

    def euclidean(src: Node, dst: Node):
        return src.geo_id.distance(dst.geo_id)

    vehicle = Vehicle('Truck', restrictions={'capacity': 200}, metric=euclidean)
    vrp = VRP(demands, depot, vehicle)
    vrp.run()

