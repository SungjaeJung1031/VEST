import sys

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QSlider, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

import g_data 
class Plotter3dProg(QWidget):
    def __init__(self, o_plot3d, parent=None):
        super().__init__()

        self.qss_main = open('resource/qss/style_main.qss').read()
        self.parent = parent
        self.o_plot3d = o_plot3d
        self.hboxlyt_plot3d_prog = QHBoxLayout()
        self.slider_plot3d_prog = QSlider(Qt.Horizontal, self)
        self.slider_plot3d_prog.setMaximum(0)
        self.slider_plot3d_prog.valueChanged.connect(self.handleSliderValueChanged)
        # self.slider_plot3d_prog.setStyleSheet(self.qss_main)
        # self.slider_plot3d_prog.setTickInterval(g_data.frm_len)
        self.slider_plot3d_prog.setTickPosition(QSlider.TicksBelow)


        self.txtedit_plot3d_prog = QLineEdit(self)
        self.txtedit_plot3d_prog.setFixedWidth(80)
        self.txtedit_plot3d_prog.setText(str(g_data.cur_frm))
        # self.field.returnPressed.connect(self.onClick)        // TODO::

        self.btn_prev = QPushButton('', self)
        self.btn_prev.clicked.connect(self.handlePrevButton)
        self.btn_prev.setIcon(QIcon('resource/img/prev-48.png'))
        self.btn_prev.setObjectName("btn_plotter_3d_prog")
        self.btn_prev.setStyleSheet(self.qss_main)

        self.btn_pause = QPushButton('', self)
        self.btn_pause.clicked.connect(self.handlePauseButton)
        self.btn_pause.setIcon(QIcon('resource/img/pause-48.png'))
        self.btn_pause.setObjectName("btn_plotter_3d_prog")
        self.btn_pause.setStyleSheet(self.qss_main)


        self.btn_play = QPushButton('', self)
        self.btn_play.clicked.connect(self.handlePlayButton)
        self.btn_play.setIcon(QIcon('resource/img/play-48.png'))
        self.btn_play.setObjectName("btn_plotter_3d_prog")
        self.btn_play.setStyleSheet(self.qss_main)


        self.btn_stop = QPushButton('', self)
        self.btn_stop.clicked.connect(self.handleStopButton)
        self.btn_stop.setIcon(QIcon('resource/img/stop-48.png'))
        self.btn_stop.setObjectName("btn_plotter_3d_prog")
        self.btn_stop.setStyleSheet(self.qss_main)


        self.btn_next = QPushButton('', self)
        self.btn_next.clicked.connect(self.handleNextButton)
        self.btn_next.setIcon(QIcon('resource/img/next-48.png'))
        self.btn_next.setObjectName("btn_plotter_3d_prog")
        self.btn_next.setStyleSheet(self.qss_main)

        self.hboxlyt_plot3d_prog.addWidget(self.slider_plot3d_prog)
        self.hboxlyt_plot3d_prog.addWidget(self.txtedit_plot3d_prog)
        self.hboxlyt_plot3d_prog.addWidget(self.btn_prev)
        self.hboxlyt_plot3d_prog.addWidget(self.btn_pause)
        self.hboxlyt_plot3d_prog.addWidget(self.btn_play)
        self.hboxlyt_plot3d_prog.addWidget(self.btn_stop)
        self.hboxlyt_plot3d_prog.addWidget(self.btn_next)

        self.setLayout(self.hboxlyt_plot3d_prog)

    def handlePrevButton(self):
        if (0 < g_data.cur_frm):
            g_data.cur_frm = g_data.cur_frm - 1
            self.slider_plot3d_prog.setValue(g_data.cur_frm)
            self.txtedit_plot3d_prog.setText(str(g_data.cur_frm))
        else:
            pass

    def handlePauseButton(self):
        pass

    def handlePlayButton(self):
        pass

    def handleStopButton(self):
        g_data.cur_frm = 0
        self.slider_plot3d_prog.setValue(0)

    def handleNextButton(self):
        if (g_data.cur_frm < g_data.frm_len - 1):
            g_data.cur_frm = g_data.cur_frm + 1
            self.slider_plot3d_prog.setValue(g_data.cur_frm)
            self.txtedit_plot3d_prog.setText(str(g_data.cur_frm))
        else:
            pass

    def handleSliderValueChanged(self):
        g_data.cur_frm = self.slider_plot3d_prog.value()
        self.txtedit_plot3d_prog.setText(str(g_data.cur_frm))

    def initRender(self):
        g_data.cur_frm = 0
        self.slider_plot3d_prog.setMaximum(g_data.frm_len-1)