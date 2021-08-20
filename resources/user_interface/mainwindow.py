# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from modules.submodules.widgets import QMenuButton
from modules.submodules.widgets import QSearchBarNew
from modules.submodules.widgets import QTopMenuBar
from modules.submodules.widgets import QUserSelection

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2989, 779)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QTopMenuBar(self.centralwidget)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMinimumSize(QSize(0, 60))
        self.menu_bar.setMaximumSize(QSize(16777215, 60))
        self.menu_bar.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.menu_bar)
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.menu_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy)
        self.btn_menu.setMinimumSize(QSize(60, 60))
        self.btn_menu.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/Icons/ico_menu-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(34, 34))
        self.btn_menu.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_menu)

        self.txt_title = QLabel(self.menu_bar)
        self.txt_title.setObjectName(u"txt_title")
        self.txt_title.setMinimumSize(QSize(120, 0))
        self.txt_title.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.txt_title)

        self.horizontalSpacer = QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.txt_module = QLabel(self.menu_bar)
        self.txt_module.setObjectName(u"txt_module")
        self.txt_module.setMinimumSize(QSize(170, 0))
        self.txt_module.setMaximumSize(QSize(170, 16777215))
        font = QFont()
        font.setFamily(u"Helvetica Neue")
        font.setPointSize(16)
        self.txt_module.setFont(font)
        self.txt_module.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_module.setMargin(10)

        self.horizontalLayout.addWidget(self.txt_module)

        self.frame_search_bar = QFrame(self.menu_bar)
        self.frame_search_bar.setObjectName(u"frame_search_bar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_search_bar.sizePolicy().hasHeightForWidth())
        self.frame_search_bar.setSizePolicy(sizePolicy1)
        self.frame_search_bar.setMinimumSize(QSize(300, 0))
        self.frame_search_bar.setMaximumSize(QSize(1000, 16777215))
        self.frame_search_bar.setFrameShape(QFrame.NoFrame)
        self.frame_search_bar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_search_bar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.module_search_bar = QSearchBarNew(self.frame_search_bar)
        self.module_search_bar.setObjectName(u"module_search_bar")
        sizePolicy1.setHeightForWidth(self.module_search_bar.sizePolicy().hasHeightForWidth())
        self.module_search_bar.setSizePolicy(sizePolicy1)
        self.module_search_bar.setMinimumSize(QSize(0, 0))
        self.module_search_bar.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.module_search_bar)


        self.horizontalLayout.addWidget(self.frame_search_bar)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_view_menu = QPushButton(self.menu_bar)
        self.btn_view_menu.setObjectName(u"btn_view_menu")
        self.btn_view_menu.setMinimumSize(QSize(60, 60))
        self.btn_view_menu.setMaximumSize(QSize(60, 60))
        icon1 = QIcon()
        icon1.addFile(u":/Icons/ico_dashboard-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_view_menu.setIcon(icon1)
        self.btn_view_menu.setIconSize(QSize(34, 34))
        self.btn_view_menu.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_view_menu)

        self.frame_users = QFrame(self.menu_bar)
        self.frame_users.setObjectName(u"frame_users")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_users.sizePolicy().hasHeightForWidth())
        self.frame_users.setSizePolicy(sizePolicy2)
        self.frame_users.setMinimumSize(QSize(200, 0))
        self.frame_users.setMaximumSize(QSize(200, 16777215))
        self.frame_users.setFrameShape(QFrame.NoFrame)
        self.frame_users.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_users)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 12, 12, 12)
        self.module_users = QUserSelection(self.frame_users)
        self.module_users.setObjectName(u"module_users")

        self.horizontalLayout_6.addWidget(self.module_users)


        self.horizontalLayout.addWidget(self.frame_users)


        self.verticalLayout.addWidget(self.menu_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_side = QFrame(self.content)
        self.menu_side.setObjectName(u"menu_side")
        self.menu_side.setMinimumSize(QSize(170, 0))
        self.menu_side.setMaximumSize(QSize(170, 16777215))
        self.menu_side.setFrameShape(QFrame.StyledPanel)
        self.menu_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_side)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btn_module_antibodies = QMenuButton(self.menu_side)
        self.btn_module_antibodies.setObjectName(u"btn_module_antibodies")
        self.btn_module_antibodies.setMinimumSize(QSize(0, 40))
        self.btn_module_antibodies.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.btn_module_antibodies)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.ico_antibody = QLabel(self.btn_module_antibodies)
        self.ico_antibody.setObjectName(u"ico_antibody")
        self.ico_antibody.setMinimumSize(QSize(40, 0))
        self.ico_antibody.setMaximumSize(QSize(40, 60))
        self.ico_antibody.setPixmap(QPixmap(u":/Icons/ico_antibody-white.svg"))
        self.ico_antibody.setScaledContents(False)
        self.ico_antibody.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.ico_antibody)

        self.text_antibody = QLabel(self.btn_module_antibodies)
        self.text_antibody.setObjectName(u"text_antibody")
        font1 = QFont()
        font1.setFamily(u"Helvetica Neue")
        font1.setPointSize(15)
        self.text_antibody.setFont(font1)

        self.horizontalLayout_3.addWidget(self.text_antibody)

        self.sel_id_antibody = QFrame(self.btn_module_antibodies)
        self.sel_id_antibody.setObjectName(u"sel_id_antibody")
        self.sel_id_antibody.setMaximumSize(QSize(5, 16777215))
        self.sel_id_antibody.setFrameShape(QFrame.StyledPanel)
        self.sel_id_antibody.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.sel_id_antibody)


        self.verticalLayout_2.addWidget(self.btn_module_antibodies)

        self.btn_module_placeholder = QMenuButton(self.menu_side)
        self.btn_module_placeholder.setObjectName(u"btn_module_placeholder")
        self.btn_module_placeholder.setMinimumSize(QSize(0, 40))
        self.btn_module_placeholder.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.btn_module_placeholder)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.ico_placeholder = QLabel(self.btn_module_placeholder)
        self.ico_placeholder.setObjectName(u"ico_placeholder")
        self.ico_placeholder.setMinimumSize(QSize(40, 0))
        self.ico_placeholder.setMaximumSize(QSize(40, 60))
        self.ico_placeholder.setPixmap(QPixmap(u":/Icons/ico_home-white.svg"))
        self.ico_placeholder.setScaledContents(False)
        self.ico_placeholder.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.ico_placeholder)

        self.text_placeholder = QLabel(self.btn_module_placeholder)
        self.text_placeholder.setObjectName(u"text_placeholder")
        self.text_placeholder.setFont(font1)

        self.horizontalLayout_4.addWidget(self.text_placeholder)

        self.sel_id_placeholder = QFrame(self.btn_module_placeholder)
        self.sel_id_placeholder.setObjectName(u"sel_id_placeholder")
        self.sel_id_placeholder.setMaximumSize(QSize(5, 16777215))
        self.sel_id_placeholder.setFrameShape(QFrame.StyledPanel)
        self.sel_id_placeholder.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.sel_id_placeholder)


        self.verticalLayout_2.addWidget(self.btn_module_placeholder)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.menu_side)

        self.stackedWidget = QStackedWidget(self.content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.page_antibody = QWidget()
        self.page_antibody.setObjectName(u"page_antibody")
        self.stackedWidget.addWidget(self.page_antibody)
        self.page_placeholder = QWidget()
        self.page_placeholder.setObjectName(u"page_placeholder")
        self.stackedWidget.addWidget(self.page_placeholder)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 2989, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.txt_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Montserrat'; font-size:24pt; color:rgba(255, 255, 255, 0.87)\">labmate</span></p></body></html>", None))
        self.txt_module.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:rgba(255,255,255,0.866667);\">Antibody manager</span><span style=\" color:rgba(255,255,255,0.866667);\"/></p></body></html>", None))
        self.btn_view_menu.setText("")
        self.ico_antibody.setText("")
        self.text_antibody.setText(QCoreApplication.translate("MainWindow", u"<p style=\"color:rgba(255, 255, 255, 0.87)\"> Antibodies </p>", None))
        self.ico_placeholder.setText("")
        self.text_placeholder.setText(QCoreApplication.translate("MainWindow", u"<p style=\"color:rgba(255, 255, 255, 0.87)\"> Placeholder </p>", None))
    # retranslateUi

