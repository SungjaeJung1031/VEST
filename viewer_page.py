
from PySide6 import QtWidgets, QtCore

class ViewerPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ViewerPage, self).__init__(parent)

        self.label = QtWidgets.QLabel(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("viewer_page")

        self.label.setGeometry(QtCore.QRect(270, 180, 81, 16))
        self.label.setObjectName("label_viewer_page")

    def retranslateUi(self, _translate):
        self.label.setText(_translate("MainWindow", "Viewer"))
