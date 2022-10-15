
from PySide6 import QtWidgets, QtCore

class SettingPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SettingPage, self).__init__(parent)

        self.label = QtWidgets.QLabel(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("setting_page")

        self.label.setGeometry(QtCore.QRect(400, 190, 121, 16))
        self.label.setObjectName("label_setting_page")

    def retranslateUi(self, _translate):
        self.label.setText(_translate("MainWindow", "Setting"))
