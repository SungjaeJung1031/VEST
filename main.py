# This Python file uses the following encoding: utf-8
import os
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
from PySide6.QtUiTools import QUiLoader


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()
        self.window.setWindowTitle("VEST")

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)

        # SLIDABLE LEFT MENU /////////////////////
        self.window.menuBtn.clicked.connect(lambda: self.slideLeftMenu())


        # STACKED PAGE (DEFAULT / CURRENT PAGE) ///////////////
        # Set the page that will be visiable by default when the app is opened
        self.window.stackedWidget.setCurrentWidget(self.window.viewerPage)

        # STACKED PAGE NAVIGATION ///////////////////////
        # Using side menu buttons

        # navigating to viewer page
        self.window.viewerBtn.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.viewerPage))
        # navigating to annotation page
        self.window.annotationBtn.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.annotationPage))
        # navigating to analysis page
        self.window.analysisBtn.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.analysisPage))
        # navigating to setting page
        self.window.settingBtn.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.settingPage))
        # navigating to help page
        self.window.helpBtn.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.helpPage))
        # navigating to about page
        self.window.aboutBtn.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.aboutPage))

        ui_file.close()

    def show(self):
        self.window.show()

    ###################################################
    # Slide left menu
    ##################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.window.leftMenuFrameTop.width()
        new_width = 0
        # If minimized
        if width >= 100:
            # Expand menu
            new_width = 30
            # print(1)
        # If maximized
        else:
            # Resotre menu
            new_width = 100
            # print(2)

        # Animate the transition
        self.animation_leftmenutop = QPropertyAnimation(self.window.leftMenuFrameTop, b"minimumWidth")  # Animate minimimWidth
        self.animation_leftmenutop.setDuration(250)
        # print("width:{}, new_width:{}".format(width, new_width))
        self.animation_leftmenutop.setStartValue(width)     # start value is the current menu width
        self.animation_leftmenutop.setEndValue(new_width)   # end value is the new menu width
        self.animation_leftmenutop.setEasingCurve(QEasingCurve.InOutQuart)
        #self.animation.start()

        self.animation_leftmenubottom = QPropertyAnimation(self.window.leftMenuFrameBottom, b"minimumWidth")  # Animate minimimWidth
        self.animation_leftmenubottom.setDuration(250)
        # print("width:{}, new_width:{}".format(width, new_width))
        self.animation_leftmenubottom.setStartValue(width)     # start value is the current menu width
        self.animation_leftmenubottom.setEndValue(new_width)   # end value is the new menu width
        self.animation_leftmenubottom.setEasingCurve(QEasingCurve.InOutQuart)

        self.animation_group_leftmenu = QParallelAnimationGroup()
        self.animation_group_leftmenu.addAnimation(self.animation_leftmenutop)
        self.animation_group_leftmenu.addAnimation(self.animation_leftmenubottom)

        self.animation_group_leftmenu.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
