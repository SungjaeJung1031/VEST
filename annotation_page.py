from PySide6 import QtWidgets, QtGui, QtCore, QtOpenGLWidgets
import time


from top_view_annotation_page import TopViewAnnotationPage


from wgpu.gui.qt import WgpuWidget
import wgpu.backends.rs  # noqa: F401, Select Rust backend
from triangle import main
from triangle_qt_embed_test import ExampleWidget
from wgpu_top_view import WgpuTopView
from wgpu_bottom_left_view import WgpuBottomLeftView
from wgpu_bottom_center_view import WgpuBottomCenterView
from wgpu_bottom_right_view import WgpuBottomRightView

class AnnotationPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AnnotationPage, self).__init__(parent)

        self.setObjectName("annotation_page")

        self.cur_frm = 0
        self.len_frm = 0
        self.cur_time_sec = 0

        self.vlyt = QtWidgets.QVBoxLayout(self)

        self.vlyt_annotation_page = QtWidgets.QVBoxLayout()
        self.tab_annotation_page = QtWidgets.QTabWidget(self)


        #### control tab
        self.tab_control_main_annotation_page = QtWidgets.QWidget()
        
        self.hlyt_tab_control_main_annotation_page = QtWidgets.QHBoxLayout(self.tab_control_main_annotation_page)
        self.hlyt_play_control_annotation_page = QtWidgets.QHBoxLayout()
        self.hor_slider = QtWidgets.QSlider(self.tab_control_main_annotation_page)
        self.frm_play_control = QtWidgets.QFrame(self.tab_control_main_annotation_page)
        self.line_edit_frm = QtWidgets.QLineEdit(self.tab_control_main_annotation_page)
        # self.hlinePlayControl2 = QtWidgets.QFrame(self.tab_control_main_annotation_page)
        self.btn_start = QtWidgets.QPushButton(self.tab_control_main_annotation_page)
        self.btn_step_bwd = QtWidgets.QPushButton(self.tab_control_main_annotation_page)
        self.btn_play = QtWidgets.QPushButton(self.tab_control_main_annotation_page)
        self.btn_pause = QtWidgets.QPushButton(self.tab_control_main_annotation_page)
        self.btn_step_fwd = QtWidgets.QPushButton(self.tab_control_main_annotation_page)
        self.btn_end = QtWidgets.QPushButton(self.tab_control_main_annotation_page)

        #### radar configuration tab
        self.tab_radar_config_main_annotation_page = QtWidgets.QWidget()
        self.hlyt_tab_radar_config_main_annotation_page = QtWidgets.QHBoxLayout(self.tab_radar_config_main_annotation_page)
        self.hlyt_radar_config_annotation_page = QtWidgets.QHBoxLayout()

        self.combo_box_radar_config = QtWidgets.QComboBox(self.tab_radar_config_main_annotation_page)
        self.combo_box_radar_det_config = QtWidgets.QComboBox(self.tab_radar_config_main_annotation_page)
        self.combo_box_radar_obj_config = QtWidgets.QComboBox(self.tab_radar_config_main_annotation_page)
        self.combo_box_radar_view_config = QtWidgets.QComboBox(self.tab_radar_config_main_annotation_page)

        self.btn_save_config = QtWidgets.QPushButton(self.tab_radar_config_main_annotation_page)
        self.btn_load_config = QtWidgets.QPushButton(self.tab_radar_config_main_annotation_page)
        self.btn_palette = QtWidgets.QPushButton(self.tab_radar_config_main_annotation_page)

        #### viewer
        self.hsplt_main_annotation_page = QtWidgets.QSplitter(self)
        self.vsplt_view_annotation_page = QtWidgets.QSplitter(self.hsplt_main_annotation_page)

        #self.opengl_top_view = QtOpenGLWidgets.QOpenGLWidget(self.vsplt_view_annotation_page)

        # self.opengl_top_view = TopViewAnnotationPage(self.vsplt_view_annotation_page)
        # self.opengl_top_view.show()
        # self.opengl_top_view = ExampleWidget(self.vsplt_view_annotation_page)
        # self.wgpu_top_view = WgpuWidget(self.vsplt_view_annotation_page)
        # main(self.wgpu_top_view)

        self.wgpu_top_view = WgpuTopView(self.vsplt_view_annotation_page)

        # self.opengl_top_view.initRender()

        self.hsplt_view_annotation_page = QtWidgets.QSplitter(self.vsplt_view_annotation_page)


        self.wgpu_bottom_left_view = WgpuBottomLeftView(self.hsplt_view_annotation_page)
        self.wgpu_bottom_center_view = WgpuBottomCenterView(self.hsplt_view_annotation_page)
        self.wgpu_bottom_right_view = WgpuBottomRightView(self.hsplt_view_annotation_page)

        #### annotation info
        self.annotation_page_info = QtWidgets.QTabWidget(self.hsplt_main_annotation_page)
        self.tab_1_annotation_page_info = QtWidgets.QWidget()
        self.tab_2_annotation_page_info = QtWidgets.QWidget()

        self.setupUi()

    def setupUi(self):
        self.vlyt.setContentsMargins(5, 5, 5, 5)
        self.vlyt.setSpacing(5)
        self.vlyt.setObjectName("vlt")

        self.vlyt_annotation_page.setSpacing(5)
        self.vlyt_annotation_page.setObjectName("vlyt_annotation_page")
        
        self.tab_annotation_page.setObjectName("tab_annotation_page")
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_control_main_annotation_page.sizePolicy().hasHeightForWidth())

        #### control tab
        self.tab_control_main_annotation_page.setSizePolicy(sizePolicy)
        self.tab_control_main_annotation_page.setObjectName("tab_control_main_annotation_page")
        
        self.hlyt_tab_control_main_annotation_page.setObjectName("hlyt_tab_control_main_annotation_page")
        
        self.hlyt_play_control_annotation_page.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.hlyt_play_control_annotation_page.setSpacing(5)
        self.hlyt_play_control_annotation_page.setObjectName("hlyt_play_control_annotation_page")

        
        self.hor_slider.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.SizeHorCursor))
        self.hor_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.hor_slider.setObjectName("hor_slider")
        self.hor_slider.setMaximum(0)
        self.hor_slider.valueChanged.connect(self.handleSliderValueChanged)

        self.hlyt_play_control_annotation_page.addWidget(self.hor_slider)
        
        self.frm_play_control.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.frm_play_control.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.frm_play_control.setObjectName("frm_play_control")
        self.hlyt_play_control_annotation_page.addWidget(self.frm_play_control)

        self.line_edit_frm.setObjectName("line_edit_frm")
        self.line_edit_frm.setText(str(self.hor_slider.value()))

        self.hlyt_play_control_annotation_page.addWidget(self.line_edit_frm)
        
        # self.hlinePlayControl2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        # self.hlinePlayControl2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        # self.hlinePlayControl2.setObjectName("hlinePlayControl2")
        # self.hlyt_play_control_annotation_page.addWidget(self.hlinePlayControl2)
        
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_start.setText("")
        icon_btn_start = QtGui.QIcon()
        icon_btn_start.addPixmap(QtGui.QPixmap("resource/icons/player-control-skip-to-start-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_start.setIcon(icon_btn_start)
        self.btn_start.setObjectName("btn_start")
        self.btn_start.clicked.connect(self.handleBtnStart)
        self.hlyt_play_control_annotation_page.addWidget(self.btn_start)

        self.btn_step_bwd.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_step_bwd.setText("")
        icon_btn_step_bwd = QtGui.QIcon()
        icon_btn_step_bwd.addPixmap(QtGui.QPixmap("resource/icons/player-control-rewind-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_step_bwd.setIcon(icon_btn_step_bwd)
        self.btn_step_bwd.setIconSize(QtCore.QSize(16, 16))
        self.btn_step_bwd.setObjectName("btn_step_bwd")
        self.btn_step_bwd.clicked.connect(self.handleBtnStepBwd)
        self.hlyt_play_control_annotation_page.addWidget(self.btn_step_bwd)

        self.btn_pause.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_pause.setText("")
        icon_btn_pause = QtGui.QIcon()
        icon_btn_pause.addPixmap(QtGui.QPixmap("resource/icons/player-control-pause-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_pause.setIcon(icon_btn_pause)
        self.btn_pause.setObjectName("btn_pause")
        self.btn_pause.clicked.connect(self.handleBtnPause)
        self.hlyt_play_control_annotation_page.addWidget(self.btn_pause)

        
        self.btn_play.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_play.setText("")
        icon_btn_play = QtGui.QIcon()
        icon_btn_play.addPixmap(QtGui.QPixmap("resource/icons/player-control-play-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_play.setIcon(icon_btn_play)
        self.btn_play.setObjectName("btn_play")
        self.btn_play.clicked.connect(self.handleBtnPlay)
        self.hlyt_play_control_annotation_page.addWidget(self.btn_play)

        self.btn_step_fwd.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_step_fwd.setText("")
        icon_btn_step_fwd = QtGui.QIcon()
        icon_btn_step_fwd.addPixmap(QtGui.QPixmap("resource/icons/player-control-fast-forward-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_step_fwd.setIcon(icon_btn_step_fwd)
        self.btn_step_fwd.setObjectName("btn_step_fwd")
        self.btn_step_fwd.clicked.connect(self.handleBtnStepFwd)
        self.hlyt_play_control_annotation_page.addWidget(self.btn_step_fwd)

        self.btn_end.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_end.setText("")
        icon_btn_end = QtGui.QIcon()
        icon_btn_end.addPixmap(QtGui.QPixmap("resource/icons/player-control-end-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_end.setIcon(icon_btn_end)
        self.btn_end.setObjectName("btn_end")
        self.btn_end.clicked.connect(self.handleBtnEnd)
        self.hlyt_play_control_annotation_page.addWidget(self.btn_end)

        self.hlyt_play_control_annotation_page.setStretch(0, 9)
        self.hlyt_tab_control_main_annotation_page.addLayout(self.hlyt_play_control_annotation_page)
        self.tab_annotation_page.addTab(self.tab_control_main_annotation_page, "")

        #### configuration tab
        self.tab_radar_config_main_annotation_page.setObjectName("tab_radar_config_main_annotation_page")
        
        self.hlyt_tab_radar_config_main_annotation_page.setObjectName("hlyt_tab_radar_config_main_annotation_page")
        
        self.hlyt_radar_config_annotation_page.setObjectName("hlyt_radar_config_annotation_page")

        self.combo_box_radar_config.setObjectName("combo_box_radar_config")
        self.hlyt_radar_config_annotation_page.addWidget(self.combo_box_radar_config)

        self.combo_box_radar_det_config.setObjectName("combo_box_radar_det_config")
        self.hlyt_radar_config_annotation_page.addWidget(self.combo_box_radar_det_config)

        self.combo_box_radar_obj_config.setObjectName("combo_box_radar_obj_config")
        self.hlyt_radar_config_annotation_page.addWidget(self.combo_box_radar_obj_config)

        self.combo_box_radar_view_config.setObjectName("combo_box_radar_view_config")
        self.hlyt_radar_config_annotation_page.addWidget(self.combo_box_radar_view_config)

        
        self.btn_palette.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_palette.setText("")
        icon_btn_palette = QtGui.QIcon()
        icon_btn_palette.addPixmap(QtGui.QPixmap("resource/icons/palette-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_palette.setIcon(icon_btn_palette)
        self.btn_palette.setObjectName("btn_palette")
        self.hlyt_radar_config_annotation_page.addWidget(self.btn_palette)

        self.btn_save_config.setText("")
        icon_btn_save_config = QtGui.QIcon()
        icon_btn_save_config.addPixmap(QtGui.QPixmap("resource/icons/save-document-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_save_config.setIcon(icon_btn_save_config)
        self.btn_save_config.setObjectName("btn_save_config")
        self.hlyt_radar_config_annotation_page.addWidget(self.btn_save_config)

        self.btn_load_config.setText("")
        icon_btn_load_config = QtGui.QIcon()
        icon_btn_load_config.addPixmap(QtGui.QPixmap("resource/icons/open-document-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_load_config.setIcon(icon_btn_load_config)
        self.btn_load_config.setObjectName("btn_load_config")
        self.hlyt_radar_config_annotation_page.addWidget(self.btn_load_config)

        self.hlyt_radar_config_annotation_page.setStretch(0, 1)
        self.hlyt_radar_config_annotation_page.setStretch(1, 1)
        self.hlyt_radar_config_annotation_page.setStretch(2, 1)
        self.hlyt_radar_config_annotation_page.setStretch(3, 1)

        self.hlyt_tab_radar_config_main_annotation_page.addLayout(self.hlyt_radar_config_annotation_page)
        self.tab_annotation_page.addTab(self.tab_radar_config_main_annotation_page, "")
        self.vlyt_annotation_page.addWidget(self.tab_annotation_page)

        #### viewer
        self.hsplt_main_annotation_page.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.hsplt_main_annotation_page.setChildrenCollapsible(False)
        self.hsplt_main_annotation_page.setObjectName("hsplt_main_annotation_page")

        
        self.vsplt_view_annotation_page.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.vsplt_view_annotation_page.setChildrenCollapsible(False)
        self.vsplt_view_annotation_page.setObjectName("vsplt_view_annotation_page")

        self.wgpu_top_view.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.wgpu_top_view.setMouseTracking(False)
        self.wgpu_top_view.setObjectName("wgpu_top_view")

        self.hsplt_view_annotation_page.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.hsplt_view_annotation_page.setChildrenCollapsible(False)
        self.hsplt_view_annotation_page.setObjectName("hsplt_view_annotation_page")

        
        self.wgpu_bottom_left_view.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.wgpu_bottom_left_view.setObjectName("wgpu_bottom_left_view")

        self.wgpu_bottom_center_view.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.wgpu_bottom_center_view.setObjectName("wgpu_bottom_center_view")

        self.wgpu_bottom_right_view.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.wgpu_bottom_right_view.setObjectName("wgpu_bottom_right_view")

        #### annotation info
        self.annotation_page_info.setObjectName("annotation_page_info")

        self.tab_1_annotation_page_info.setObjectName("tab_1_annotation_page_info")
        self.annotation_page_info.addTab(self.tab_1_annotation_page_info, "")
        
        self.tab_2_annotation_page_info.setObjectName("tab_2_annotation_page_info")
        self.annotation_page_info.addTab(self.tab_2_annotation_page_info, "")

        self.vlyt_annotation_page.addWidget(self.hsplt_main_annotation_page)
        self.vlyt_annotation_page.setStretch(1, 9)

        self.vlyt.addLayout(self.vlyt_annotation_page)

        self.tab_annotation_page.setCurrentIndex(0)
        self.annotation_page_info.setCurrentIndex(0)
        
    def retranslateUi(self, _translate):
        self.tab_annotation_page.setTabText(self.tab_annotation_page.indexOf(self.tab_control_main_annotation_page), _translate("MainWindow", "Play Controls"))
        self.tab_annotation_page.setTabText(self.tab_annotation_page.indexOf(self.tab_radar_config_main_annotation_page), _translate("MainWindow", "View Configuration"))
        self.annotation_page_info.setTabText(self.annotation_page_info.indexOf(self.tab_1_annotation_page_info), _translate("MainWindow", "Tab 1"))
        self.annotation_page_info.setTabText(self.annotation_page_info.indexOf(self.tab_2_annotation_page_info), _translate("MainWindow", "Tab 2"))

        self.hsplt_main_annotation_page.setSizes([self.hsplt_main_annotation_page.size().height() * 0.7,
                                                self.hsplt_main_annotation_page.size().height() * 0.3])

        self.vsplt_view_annotation_page.setSizes([self.vsplt_view_annotation_page.size().height()*0.7,
                                                        self.vsplt_view_annotation_page.size().height()*0.3])

        self.hsplt_view_annotation_page.setSizes([self.hsplt_view_annotation_page.size().width()*0.33,
                                                        self.hsplt_view_annotation_page.size().width()*0.33,
                                                        self.hsplt_view_annotation_page.size().width()*0.33])

    def handleSliderValueChanged(self):
        self.cur_frm = self.hor_slider.value()
        self.line_edit_frm.setText(str(self.cur_frm))


    def handleBtnStart(self):
        self.cur_frm = 0
        self.hor_slider.setValue(self.cur_frm)
        self.handleSliderValueChanged()

    def handleBtnStepBwd(self):
        if (0 < self.cur_frm):
            self.cur_frm = self.cur_frm - 1
            self.hor_slider.setValue(self.cur_frm)
            self.handleSliderValueChanged()

    def handleBtnPlay(self):
        while(self.cur_frm < self.len_frm):
            curTimeSec = lambda: int(round(time.time()))

            if (0 == self.cur_time_sec):
                self.cur_time_sec = curTimeSec()
            else:
                if ((0 < self.cur_time_sec) and (1 < abs(self.cur_time_sec - curTimeSec()))):
                    self.cur_frm = self.cur_frm + 1
                    self.hor_slider.setValue(self.cur_frm)
                    self.handleSliderValueChanged()
                    print(self.cur_time_sec)
                else:
                    self.cur_time_sec = curTimeSec()
            
    def handleBtnPause(self):
        self.f_play = False

    def handleBtnStepFwd(self):
        if (self.cur_frm < self.len_frm):
            self.cur_frm = self.cur_frm + 1
            self.hor_slider.setValue(self.cur_frm)
            self.handleSliderValueChanged()

    def handleBtnEnd(self):
        self.cur_frm = self.len_frm
        self.hor_slider.setValue(self.cur_frm)
        self.handleSliderValueChanged()

    def setSliderRange(self, max_range:int, sz_single_step:int=1):
        self.hor_slider.setMinimum(0)
        self.len_frm = max_range
        self.hor_slider.setMaximum(self.len_frm)
        self.hor_slider.setSingleStep(sz_single_step)
