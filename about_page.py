
from PySide6 import QtWidgets, QtCore

class AboutPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AboutPage, self).__init__(parent)

        self.label = QtWidgets.QLabel(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("about_page")

        self.label.setGeometry(QtCore.QRect(420, 260, 91, 16))
        self.label.setObjectName("label_about_page")

    def retranslateUi(self, _translate):
        self.label.setText(_translate("MainWindow", "About"))
