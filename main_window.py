import sys

from PyQt5.QtWidgets    import QAction, QWidget, QMainWindow, qApp
from PyQt5.QtGui        import QIcon

from layout_main        import LayoutMain

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget(self)
        self.qss_main = open('resource/qss/style_main.qss').read()
        self.setStyleSheet(self.qss_main)

        self.menubar = self.menuBar()
        self.action_load = QAction(QIcon('resource/img/import-24.png'),'Load', self)
        self.action_save = QAction(QIcon('resource/img/export-24.png'),'Save', self)
        self.action_exit = QAction(QIcon('resource/img/exit-24.png'),'Exit', self)

        self.initUI()
    
    def initUI(self):
        self.setCentralWidget(self.main_widget)

        self.initMenubar()
        self.initMainLayout()
        self.initStatusBar()

        self.setWindowTitle("VEST")
        self.setWindowIcon(QIcon('resource/img/vest-64.png'))
        self.setGeometry(200,300,500,500)
        self.showMaximized()

    def initMenubar(self):
        self.action_load.setShortcut('Ctrl+L')
        self.action_load.setStatusTip('Load File')
        # self.action_load.triggered.conenct() # TODO::

        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setStatusTip('Save File')
        # self.action_load.triggered.conenct() # TODO::

        self.action_exit.setShortcut('Ctrl+Q')
        self.action_exit.setStatusTip('Exit Application')
        self.action_exit.triggered.connect(qApp.quit)
        
        self.menubar.setNativeMenuBar(False)
        filemenu = self.menubar.addMenu('&File')

        filemenu.addAction(self.action_load)
        filemenu.addAction(self.action_save)
        filemenu.addAction(self.action_exit)

    def initMainLayout(self):
        self.main_widget.setLayout(LayoutMain(self))

    def initStatusBar(self):
        self.statusBar().showMessage('Ready')