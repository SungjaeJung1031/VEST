import sys
from PyQt5.QtWidgets import QApplication

from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exec_status = MainWindow()
    sys.exit(app.exec_())