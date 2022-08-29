from PySide6 import QtWidgets, QtGui, QtCore


class Header(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Header, self).__init__(parent)
        # self.dark_theme = open('dark_theme_header.qss').read()
        # self.setStyleSheet(self.dark_theme)
        self.setupUi()

    def setupUi(self):
        # self.header = QtWidgets.QWidget(self.centralwidget)
        self.setObjectName("header")
       
        self.hlytHeader = QtWidgets.QHBoxLayout(self)
        self.hlytHeader.setContentsMargins(5, 5, 5, 5)
        self.hlytHeader.setSpacing(5)
        self.hlytHeader.setObjectName("hlytHeader")
        self.headerLeft = QtWidgets.QFrame(self)
        self.headerLeft.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.headerLeft.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.headerLeft.setObjectName("headerLeft")
        self.hlytHeaderLeft = QtWidgets.QHBoxLayout(self.headerLeft)
        self.hlytHeaderLeft.setContentsMargins(0, -1, 9, -1)
        self.hlytHeaderLeft.setObjectName("hlytHeaderLeft")
        self.menuBtn = QtWidgets.QPushButton(self.headerLeft)
        self.menuBtn.setMinimumSize(QtCore.QSize(25, 0))
        self.menuBtn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.menuBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/icons/menu-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setObjectName("menuBtn")
        self.hlytHeaderLeft.addWidget(self.menuBtn, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.appName = QtWidgets.QLabel(self.headerLeft)
        self.appName.setObjectName("appName")
        self.hlytHeaderLeft.addWidget(self.appName)
        self.appNameFull = QtWidgets.QLabel(self.headerLeft)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.appNameFull.setFont(font)
        self.appNameFull.setLineWidth(1)
        self.appNameFull.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.appNameFull.setObjectName("appNameFull")
        self.hlytHeaderLeft.addWidget(self.appNameFull)
        self.hlytHeader.addWidget(self.headerLeft, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.headerRight = QtWidgets.QFrame(self)
        self.headerRight.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.headerRight.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.headerRight.setObjectName("headerRight")
        self.hlytHeaderRight = QtWidgets.QHBoxLayout(self.headerRight)
        self.hlytHeaderRight.setObjectName("hlytHeaderRight")
        self.changeThemeBtn = QtWidgets.QPushButton(self.headerRight)
        self.changeThemeBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.changeThemeBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resource/icons/change-theme-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.changeThemeBtn.setIcon(icon1)
        self.changeThemeBtn.setIconSize(QtCore.QSize(16, 16))
        self.changeThemeBtn.setObjectName("changeThemeBtn")
        self.hlytHeaderRight.addWidget(self.changeThemeBtn)
        self.configSavedBtn = QtWidgets.QPushButton(self.headerRight)
        self.configSavedBtn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.configSavedBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resource/icons/settings-saved-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.configSavedBtn.setIcon(icon2)
        self.configSavedBtn.setIconSize(QtCore.QSize(16, 16))
        self.configSavedBtn.setObjectName("configSavedBtn")
        self.hlytHeaderRight.addWidget(self.configSavedBtn)
        self.hlytHeader.addWidget(self.headerRight, 0, QtCore.Qt.AlignmentFlag.AlignRight)

    def retranslateUi(self, _translate):
        self.appName.setText(_translate("MainWindow", "VEST"))
        self.appNameFull.setText(_translate("MainWindow", "VEhicle Simulation Tool"))