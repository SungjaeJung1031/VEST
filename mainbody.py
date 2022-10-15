from PySide6 import QtWidgets, QtGui, QtCore, QtOpenGLWidgets
from about_page import AboutPage

from left_menu import LeftMenu
from viewer_page import ViewerPage
from analysis_page import AnalysisPage
from annotation_page import AnnotationPage
from setting_page import SettingPage
from help_page import HelpPage

class MainBody(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainBody, self).__init__(parent)
        self.setupUi()

        self.cur_frm = 0

    def setupUi(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setObjectName("mainBody")
        self.hlyt_main_body = QtWidgets.QHBoxLayout(self)
        self.hlyt_main_body.setContentsMargins(5, 5, 0, 0)
        self.hlyt_main_body.setSpacing(0)
        self.hlyt_main_body.setObjectName("hlyt_main_body")

        ### left menu
        self.left_menu = LeftMenu(self)
        self.hlyt_main_body.addWidget(self.left_menu)

        content_mainbody = QtWidgets.QWidget(self)
        content_mainbody.setObjectName("content_mainbody")
        content_mainbody.setStyleSheet("background-color:#242424")

        self.vlyt_main_body_content = QtWidgets.QVBoxLayout(content_mainbody)
        self.vlyt_main_body_content.setObjectName("vlyt_main_body_content")

        self.stacked_widget = QtWidgets.QStackedWidget(content_mainbody)
        self.stacked_widget.setObjectName("stacked_widget")
        
        self.viewer_page = ViewerPage()
        self.stacked_widget.addWidget(self.viewer_page)

        self.annotation_page = AnnotationPage()

        self.stacked_widget.addWidget(self.annotation_page)

        self.analysis_page = AnalysisPage(self)
        self.stacked_widget.addWidget(self.analysis_page)

        self.setting_page = SettingPage(self)
        self.stacked_widget.addWidget(self.setting_page)

        self.help_page = HelpPage(self)
        self.stacked_widget.addWidget(self.help_page)

        self.about_page = AboutPage(self)
        self.stacked_widget.addWidget(self.about_page)

        self.vlyt_main_body_content.addWidget(self.stacked_widget)
        self.hlyt_main_body.addWidget(content_mainbody)

        ### deprecated
        self.rightMenu = QtWidgets.QWidget(self)
        self.rightMenu.setObjectName("rightMenu")
        self.hlyt_main_body.addWidget(self.rightMenu)

        self.stacked_widget.setCurrentIndex(1)


    def retranslateUi(self, _translate):
        self.left_menu.retranslateUi(_translate)
        self.viewer_page.retranslateUi(_translate)
        self.analysis_page.retranslateUi(_translate)
        self.annotation_page.retranslateUi(_translate)
        self.setting_page.retranslateUi(_translate)
        self.help_page.retranslateUi(_translate)
        self.about_page.retranslateUi(_translate)

        # STACKED PAGE (DEFAULT / CURRENT PAGE) ///////////////
        # Set the page that will be visiable by default when the app is opened
        self.stacked_widget.setCurrentWidget(self.viewer_page)

        # STACKED PAGE NAVIGATION ///////////////////////
        # Using side menu buttons

        # navigating to viewer page
        self.left_menu.btn_viewer_tab.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.viewer_page))
        # navigating to annotation page
        self.left_menu.btn_annotation_tab.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.annotation_page))
        # navigating to analysis page
        self.left_menu.btn_analysis_tab.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.analysis_page))
        # navigating to setting page
        self.left_menu.btn_setting.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.setting_page))
        # navigating to help page
        self.left_menu.btn_help.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.help_page))
        # navigating to about page
        self.left_menu.btn_about.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.about_page))