
from PySide6 import QtWidgets, QtCore

class AnalysisPage(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AnalysisPage, self).__init__(parent)

        self.label = QtWidgets.QLabel(self)

        self.setupUi()

    def setupUi(self):
        self.setObjectName("analysis_page")

        self.label.setGeometry(QtCore.QRect(290, 150, 131, 16))
        self.label.setObjectName("label_analysis_page")

    def retranslateUi(self, _translate):
        self.label.setText(_translate("MainWindow", "Analysis"))
