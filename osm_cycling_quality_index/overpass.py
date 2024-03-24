import requests
from pathlib import Path

from qgis.core import QgsRectangle


def get_data(bbox: QgsRectangle):
    coord_list = [
        bbox.yMinimum(),
        bbox.xMinimum(),
        bbox.yMaximum(),
        bbox.xMaximum()
    ]
    bbox_str = "%2C".join([str(b) for b in coord_list])
    with open(Path(__file__).parent / "req.txt") as file:
        data = file.read()
        data_new = data.replace("{bbox}", bbox_str)
    print(data_new)
    res = requests.get(
        "https://overpass-api.de/api/interpreter", data=data_new)
    return res.json()
