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
        self.frame_left_menu_top = QtWidgets.QFrame(self.frame_wrap)
        self.vlyt_frame_left_menu_top = QtWidgets.QVBoxLayout(self.frame_left_menu_top)

        self.setupUi()

    def setupUi(self):
        self.vlyt.setContentsMargins(0, 0, 0, 0)
        self.vlyt.setSpacing(0)
        self.vlyt.setObjectName("vlyt_left_menu")

        ### frame_wrap
        self.frame_wrap.setBaseSize(QtCore.QSize(0, 0))
        self.frame_wrap.setObjectName("frame_wrap_left_menu")

        self.vlyt_frame_wrap.setContentsMargins(0, 0, 0, 5)
        self.vlyt_frame_wrap.setSpacing(0)
        self.vlyt_frame_wrap.setObjectName("vlyt_frame_wrap_left_menu")

        self.frame_left_menu_top.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_left_menu_top.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_left_menu_top.setBaseSize(QtCore.QSize(0, 0))
        self.frame_left_menu_top.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_left_menu_top.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left_menu_top.setObjectName("left_menu_frame_top")

        self.vlyt_frame_left_menu_top.setContentsMargins(0, 0, 0, 0)
        self.vlyt_frame_left_menu_top.setSpacing(0)
        self.vlyt_frame_left_menu_top.setObjectName("vlyt_left_menu_frame_top")

