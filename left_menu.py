from PySide6 import QtCore, QtGui, QtWidgets

class LeftMenu(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(LeftMenu, self).__init__(parent)
        self.setEnabled(True)
        self.setMinimumSize(QtCore.QSize(25, 0))
        self.setMaximumSize(QtCore.QSize(250, 16777215))
        self.setBaseSize(QtCore.QSize(0, 0))
        self.setObjectName("left_menu")

        self.vlyt = QtWidgets.QVBoxLayout(self)
        self.frame_wrap = QtWidgets.QWidget(self)
        self.vlyt_frame_wrap = QtWidgets.QVBoxLayout(self.frame_wrap)
        self.frame_top = QtWidgets.QFrame(self.frame_wrap)
        self.frame_bottom = QtWidgets.QFrame(self.frame_wrap)

        self.vlyt_frame_top = QtWidgets.QVBoxLayout(self.frame_top)
        self.vlyt_frame_bottom = QtWidgets.QVBoxLayout(self.frame_bottom)

        self.btn_viewer_tab = QtWidgets.QPushButton(self.frame_top)
        self.btn_annotation_tab = QtWidgets.QPushButton(self.frame_top)
        self.btn_analysis_tab = QtWidgets.QPushButton(self.frame_top)

        self.btn_setting = QtWidgets.QPushButton(self.frame_bottom)
        self.btn_help = QtWidgets.QPushButton(self.frame_bottom)
        self.btn_about = QtWidgets.QPushButton(self.frame_bottom)

        self.btn_group = QtWidgets.QButtonGroup(self)


        self.setupUi()

    def setupUi(self):
        self.vlyt.setContentsMargins(0, 0, 0, 0)
        self.vlyt.setSpacing(0)
        self.vlyt.setObjectName("vlyt_left_menu")

        #### set frame
        self.frame_wrap.setBaseSize(QtCore.QSize(0, 0))
        self.frame_wrap.setObjectName("frame_wrap_left_menu")

        self.vlyt_frame_wrap.setContentsMargins(0, 0, 0, 5)
        self.vlyt_frame_wrap.setSpacing(0)
        self.vlyt_frame_wrap.setObjectName("vlyt_frame_wrap_left_menu")

        self.frame_top.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_top.setBaseSize(QtCore.QSize(0, 0))
        self.frame_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_top.setObjectName("frame_top_left_menu")

        self.frame_bottom.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_bottom.setBaseSize(QtCore.QSize(0, 0))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_bottom.setObjectName("frame_bottom_left_menu")

        self.vlyt_frame_top.setContentsMargins(0, 0, 0, 0)
        self.vlyt_frame_top.setSpacing(0)
        self.vlyt_frame_top.setObjectName("vlyt_frame_top_left_menu")

        self.vlyt_frame_bottom.setContentsMargins(0, 0, 0, 0)
        self.vlyt_frame_bottom.setSpacing(0)
        self.vlyt_frame_bottom.setObjectName("vlyt_frame_bottom_left_menu")

        self.btn_group.setObjectName("btn_group_left_menu")

        #### set buttons
        ## frame top
        self.btn_viewer_tab.setMinimumSize(QtCore.QSize(25, 0))
        self.btn_viewer_tab.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btn_viewer_tab.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_viewer_tab.setStyleSheet(":open{\n"
    "    background-color:#242424;\n"
    "    border-left: 2px solid #f84119;\n"
    "}")
        self.btn_viewer_tab.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resource/icons/viewer-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_viewer_tab.setIcon(icon3)
        self.btn_viewer_tab.setCheckable(True)
        self.btn_viewer_tab.setChecked(True)
        self.btn_viewer_tab.setAutoRepeat(False)
        self.btn_viewer_tab.setDefault(False)
        self.btn_viewer_tab.setObjectName("btn_viewer_tab")
        self.btn_group.addButton(self.btn_viewer_tab)
        self.vlyt_frame_top.addWidget(self.btn_viewer_tab)


        self.btn_annotation_tab.setMinimumSize(QtCore.QSize(25, 0))
        self.btn_annotation_tab.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btn_annotation_tab.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_annotation_tab.setStyleSheet(":open{\n"
    "    background-color:#242424;\n"
    "    border-left: 2px solid #f84119;\n"
    "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resource/icons/tag-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_annotation_tab.setIcon(icon4)
        self.btn_annotation_tab.setCheckable(True)
        self.btn_annotation_tab.setAutoDefault(False)
        self.btn_annotation_tab.setDefault(False)
        self.btn_annotation_tab.setObjectName("btn_annotation_tab")
        self.btn_group.addButton(self.btn_annotation_tab)
        self.vlyt_frame_top.addWidget(self.btn_annotation_tab)

        self.btn_analysis_tab.setMinimumSize(QtCore.QSize(25, 0))
        self.btn_analysis_tab.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btn_analysis_tab.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_analysis_tab.setStyleSheet(":open{\n"
    "    background-color:#242424;\n"
    "    border-left: 2px solid #f84119;\n"
    "}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resource/icons/scatter-plot-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_analysis_tab.setIcon(icon5)
        self.btn_analysis_tab.setCheckable(True)
        self.btn_analysis_tab.setObjectName("btn_analysis_tab")
        self.btn_group.addButton(self.btn_analysis_tab)
        self.vlyt_frame_top.addWidget(self.btn_analysis_tab)

        self.vlyt_frame_wrap.addWidget(self.frame_top)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vlyt_frame_wrap.addItem(spacer_item)

        ## frame bottom
        self.btn_setting.setMinimumSize(QtCore.QSize(25, 0))
        self.btn_setting.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btn_setting.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_setting.setStyleSheet(":open{\n"
    "    background-color:#242424;\n"
    "    border-left: 2px solid #f84119;\n"
    "}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resource/icons/settings-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_setting.setIcon(icon6)
        self.btn_setting.setCheckable(True)
        self.btn_setting.setObjectName("btn_setting")
        self.btn_group.addButton(self.btn_setting)
        self.vlyt_frame_bottom.addWidget(self.btn_setting)


        self.btn_help.setMinimumSize(QtCore.QSize(25, 0))
        self.btn_help.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btn_help.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_help.setStyleSheet(":open{\n"
    "    background-color:#242424;\n"
    "    border-left: 2px solid #f84119;\n"
    "}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resource/icons/help-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_help.setIcon(icon7)
        self.btn_help.setCheckable(True)
        self.btn_help.setObjectName("helpBtn")
        self.btn_group.addButton(self.btn_help)
        self.vlyt_frame_bottom.addWidget(self.btn_help)

        self.btn_about.setMinimumSize(QtCore.QSize(25, 0))
        self.btn_about.setMaximumSize(QtCore.QSize(250, 16777215))
        self.btn_about.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_about.setStyleSheet(":open{\n"
    "    background-color:#242424;\n"
    "    border-left: 2px solid #f84119;\n"
    "}")
        self.btn_about.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.UnitedStates))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resource/icons/info-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_about.setIcon(icon8)
        self.btn_about.setCheckable(True)
        self.btn_about.setChecked(False)
        self.btn_about.setAutoDefault(False)
        self.btn_about.setDefault(False)
        self.btn_about.setObjectName("aboutBtn")
        self.btn_group.addButton(self.btn_about)
        self.vlyt_frame_bottom.addWidget(self.btn_about)

        self.vlyt_frame_wrap.addWidget(self.frame_bottom)

        self.vlyt.addWidget(self.frame_wrap)



    def retranslateUi(self, _translate):
        self.btn_viewer_tab.setText(_translate("MainWindow", "Viewer"))
        self.btn_annotation_tab.setText(_translate("MainWindow", "Annotation"))
        self.btn_analysis_tab.setText(_translate("MainWindow", "Analysis"))
        self.btn_setting.setText(_translate("MainWindow", "Setting"))
        self.btn_help.setText(_translate("MainWindow", "Help"))
        self.btn_about.setText(_translate("MainWindow", "About"))

        
        # navigating to viewer page
        # self.btn_viewer_tab.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.viewerPage))



