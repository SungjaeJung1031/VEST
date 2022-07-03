import sys

from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, \
                            QPushButton, QCheckBox, QGroupBox

import g_data
class Plotter3dOption(QWidget):
    def __init__(self, o_plot3d, parent=None):
        super().__init__()
        self.o_plot3d = o_plot3d
        self.parent = parent
        self.tab_plot_3d_opt = QTabWidget()
        self.vboxlyt_plot_3d_opt = QVBoxLayout()

        self.hboxlyt_tab_plot = QHBoxLayout()
        self.wdg_tab_plot = QWidget()

        self.btn_plot_opt_a = QPushButton('button A', self)
        self.chkbox_plot_opt_a = QCheckBox('check box A', self)
        self.chkbox_plot_opt_b = QCheckBox('check box B', self)
        self.chkbox_plot_opt_c = QCheckBox('check box C', self)

        self.hboxlyt_tab_plot.addWidget(self.btn_plot_opt_a)
        self.hboxlyt_tab_plot.addWidget(self.chkbox_plot_opt_a)
        self.hboxlyt_tab_plot.addWidget(self.chkbox_plot_opt_b)
        self.hboxlyt_tab_plot.addWidget(self.chkbox_plot_opt_c)

        self.wdg_tab_plot.setLayout(self.hboxlyt_tab_plot)

        #
        self.hboxlyt_tab_data = QHBoxLayout()
        self.wdg_tab_data = QWidget()

        self.gbox_sensor_a = QGroupBox('Sensor A')
        self.gbox_sensor_b = QGroupBox('Sensor B')
        self.gbox_sensor_c = QGroupBox('Sensor C')
        self.gbox_sensor_d = QGroupBox('Sensor D')
        self.gbox_sensor_e = QGroupBox('Sensor E')
        self.gbox_sensor_f = QGroupBox('Sensor F')
        self.gbox_sensor_g = QGroupBox('Sensor G')
        self.gbox_sensor_h = QGroupBox('Sensor H')
        self.gbox_sensor_i = QGroupBox('Sensor I')

        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_a)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_b)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_c)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_d)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_e)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_f)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_g)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_h)
        self.hboxlyt_tab_data.addWidget(self.gbox_sensor_i)

        self.wdg_tab_data.setLayout(self.hboxlyt_tab_data)


        self.initUI()
        
        self.vboxlyt_plot_3d_opt.addWidget(self.tab_plot_3d_opt)

        self.setLayout(self.vboxlyt_plot_3d_opt)

    def initUI(self):
        self.tab_plot_3d_opt.addTab(self.wdg_tab_plot, "Plot")
        self.tab_plot_3d_opt.addTab(self.wdg_tab_data, "Data")

    def initRender(self):
        pass