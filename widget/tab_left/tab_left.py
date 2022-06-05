import sys

from PyQt5.QtWidgets import QWidget, QTabWidget, QVideoWidget


class TabLeft(QWidget):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.tab_plot_3d_opt = QTabWidget()


        self.setWidget(self.tab_plot_3d_opt)