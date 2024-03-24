from pathlib import Path
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog
from qgis.core import QgsCoordinateReferenceSystem
from qgis.utils import iface


FORM_CLASS, _ = uic.loadUiType(
    Path(__file__).parent / f"{Path(__file__).stem}.ui")


class ExtentDialog(QDialog, FORM_CLASS):
    """Dialog to choose an Extent for the overpass download."""
    def __init__(self, parent=None):
        super(ExtentDialog, self).__init__(parent)
        self.setupUi(self)

        self.extent_groupbox.setMapCanvas(iface.mapCanvas())
        self.extent_groupbox.setOutputCrs(
            QgsCoordinateReferenceSystem("EPSG:4326"))
        
    

    






