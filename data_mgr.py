from lib.nuscenes.nuscenes import NuScenes
from PySide6.QtWidgets import QFileDialog, QWidget 
from PySide6.QtCore import QObject

from enum import Enum

import os

# dataroot = "/Users/sungjaejung1031/dev/proj/VEST/resource/data/v1.0-mini"
# print(dataroot)

# nusc = NuScenes(version='v1.0-mini', dataroot=dataroot, verbose=True)

# print(len(nusc.sample))


import pandas as pd 

class DataType(Enum):
    NUSCENES = 1
    UNKNOWN = 2

class DataManager(QWidget):
    def __init__(self, ui_file_name, parent=None):
        super(DataManager, self).__init__(parent)

        ### set ui
        self.ui_file_name = ui_file_name
        # self.ui_file = QFile(ui_file_name)
        # ui_file.open(QFile.ReadOnly)
        # loader = QUiLoader()
        # self.window = loader.load(ui_file)
        # ui_file.close()

        self.dataroot = ""
        self.nusc = None

    def loadNuscenes(self):
        dataroot = QFileDialog.getExistingDirectory(
            self,
            "Select Data Directory",
        )

        self.dataroot = dataroot

        self.nusc = NuScenes(version="v1.0-mini", dataroot=self.dataroot, verbose=True)