
from PySide6 import QtWidgets, QtCore

class HelpPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(HelpPage, self).__init__(parent)

        self.label = QtWidgets.QLabel(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("help_page")

        self.label.setGeometry(QtCore.QRect(260, 230, 81, 16))
        self.label.setObjectName("label_help_page")

    def retranslateUi(self, _translate):
        self.label.setText(_translate("MainWindow", "Help"))
