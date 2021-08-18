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

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 514)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar = QFrame(self.centralwidget)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setMaximumSize(QSize(16777215, 60))
        self.menu_bar.setFrameShape(QFrame.StyledPanel)
        self.menu_bar.setFrameShadow(QFrame.Raised)
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
        self.btn_menu.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/Icons/ico_menu-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(34, 34))
        self.btn_menu.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_menu)

        self.txt_title = QLabel(self.menu_bar)
        self.txt_title.setObjectName(u"txt_title")

        self.horizontalLayout.addWidget(self.txt_title)

        self.txt_module = QLabel(self.menu_bar)
        self.txt_module.setObjectName(u"txt_module")

        self.horizontalLayout.addWidget(self.txt_module)

        self.module_search = QWidget(self.menu_bar)
        self.module_search.setObjectName(u"module_search")

        self.horizontalLayout.addWidget(self.module_search)

        self.btn_view_all = QWidget(self.menu_bar)
        self.btn_view_all.setObjectName(u"btn_view_all")

        self.horizontalLayout.addWidget(self.btn_view_all)

        self.module_users = QWidget(self.menu_bar)
        self.module_users.setObjectName(u"module_users")

        self.horizontalLayout.addWidget(self.module_users)


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
        self.menu_side.setMaximumSize(QSize(150, 16777215))
        self.menu_side.setFrameShape(QFrame.StyledPanel)
        self.menu_side.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.menu_side)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_module_antibodies = QMenuButton(self.menu_side)
        self.btn_module_antibodies.setObjectName(u"btn_module_antibodies")
        self.btn_module_antibodies.setMinimumSize(QSize(0, 60))
        self.btn_module_antibodies.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_3 = QHBoxLayout(self.btn_module_antibodies)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.btn_module_antibodies)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(60, 60))
        self.label.setPixmap(QPixmap(u":/Icons/ico_home-white.svg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.label_2 = QLabel(self.btn_module_antibodies)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addWidget(self.btn_module_antibodies)

        self.widget_2 = QWidget(self.menu_side)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 60))
        self.widget_2.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.menu_side)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 60))
        self.widget_3.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_2.addWidget(self.widget_3)

        self.pushButton = QPushButton(self.menu_side)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 60))
        self.pushButton.setMaximumSize(QSize(16777215, 60))
        self.pushButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.verticalSpacer = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.menu_side)

        self.content_2 = QFrame(self.content)
        self.content_2.setObjectName(u"content_2")
        self.content_2.setFrameShape(QFrame.NoFrame)
        self.content_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.content_2)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.txt_title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-family:'Montserrat'; font-size:24pt;\">labmate</span></p></body></html>", None))
        self.txt_module.setText(QCoreApplication.translate("MainWindow", u"Antibody", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Antibodies", None))
        self.pushButton.setText("")
    # retranslateUi

