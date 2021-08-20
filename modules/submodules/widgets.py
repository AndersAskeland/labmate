# -----------------------------------------------------------------------------
# Module: Widgets
#
# What: Custom widgets
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
from PySide2.QtWidgets import QGraphicsDropShadowEffect, QWidget, QFrame, QPushButton,QHBoxLayout, QLabel, QLineEdit, QSizePolicy, QVBoxLayout
from PySide2.QtCore import QLine, QSize, Qt, QRect
from PySide2.QtSvg import QSvgWidget
from PySide2.QtGui import QIcon, QPalette, QPixmap, QColor, QRegion, QPainterPath, QPainter, QResizeEvent

# Local functions 

# Local classes 

# Local resources 


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class QMenuButton(QPushButton):
    ''' No real changes? I will need to recreate these buttons with push animations later. '''
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFlat(True)

        # Try rippleoverlay
        # ripple = setOverlay()

class QTopMenuBar(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.palatte = self.palette()
        self.palatte.setColor(QPalette.Background, QColor(33, 119, 239))
        self.setPalette(self.palatte)
        self.setAutoFillBackground(True)


    # box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2),

        # Shadow - Top

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(4)
        self.shadow.setBlurRadius(5)
        # self.shadow.setOffset(-1)
        self.shadow.setColor(QColor(0,0,0, 14))
        self.setGraphicsEffect(self.shadow)

    # Def theme_change - Make one for each widget

class QUserSelection(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)

        # Color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(75, 140, 242))
        self.setPalette(palette)

        # Image widget
        label_image = QLabel()

        
        # Text widget
        label_name = QLabel()
        label_name.setTextFormat(Qt.RichText)
        label_name.setText("Anders Askeland")

        # SVG widget
        btn = QPushButton()
        btn.setFlat(True)
        icon = QIcon()
        icon.addFile(u":/Icons/ico_expand-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        btn.setIcon(icon)
        # icon = QIcon()
        # icon.addFile(u":/Icons/ico_menu-white.svg", QSize(), QIcon.Normal, QIcon.Off)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(label_image)
        layout.addWidget(label_name)
        layout.addWidget(btn)
        self.setLayout(layout)

class QSearchBarNew(QFrame):
    def __init__(self,parent=None):
        super().__init__(parent)
        
        # General

        # Color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(75, 140, 242))
        self.setPalette(palette)

        # Label widget
        label = QLabel()
        label.setObjectName(u"ico_search")
        label.setPixmap(u":/Icons/ico_search-white.svg")
        label.setAlignment(Qt.AlignCenter)

        # Lineedit widget
        search_bar = QLineEdit()
        search_bar.setObjectName(u"search_bar")
        search_bar.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        search_bar.setAutoFillBackground(True)
        search_bar.setFrame(False)
        search_bar.setPlaceholderText("Search")
        
        # Shadow
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setXOffset(2)
        self.shadow.setYOffset(8)
        self.shadow.setBlurRadius(14)
        self.shadow.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(self.shadow)

        # design
        palette.setColor(QPalette.Base, QColor(75, 140, 242))
        search_bar.setPalette(palette)
        # TODO: Shadow

        # Logic
        # TODO: Search logic

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(label)
        layout.addWidget(search_bar)
        self.setLayout(layout)

    # ----- Setters ----- #
    def geometry_setter(self):
        # Creates rounded edges
        radius = 2
        painter = QPainterPath()
        painter.addRoundedRect(QRect(self.contentsRect()), radius, radius)
        mask = QRegion(painter.toFillPolygon().toPolygon())
        self.setMask(mask)

    # ------ Events ----- #
    def resizeEvent(self, event: QResizeEvent) -> None:
        print("rezise")
        self.update()
        self.geometry_setter()

class QMaterialAppbar(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        # Set shadow
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(11)
        self.shadow.setColor(QColor(0,0,0, 50))
        self.shadow.setOffset(0, 3)

        self.setGraphicsEffect(self.shadow)

        layout = QHBoxLayout()
        self.setLayout(layout)









# Notes

# .md-whiteframe-1dp {
#     box-shadow:  0px 1px 3px 0px rgba(0, 0, 0, 0.2),
#     0px 1px 1px 0px rgba(0, 0, 0, 0.14),
#     0px 2px 1px -1px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-2dp {
#     box-shadow:  0px 1px 5px 0px rgba(0, 0, 0, 0.2),
#     0px 2px 2px 0px rgba(0, 0, 0, 0.14),
#     0px 3px 1px -2px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-3dp {
#     box-shadow:0px 1px 8px 0px rgba(0, 0, 0, 0.2),
#     0px 3px 4px 0px rgba(0, 0, 0, 0.14),
#     0px 3px 3px -2px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-4dp {
#     box-shadow: 0px 2px 4px -1px rgba(0, 0, 0, 0.2),
#     0px 4px 5px 0px rgba(0, 0, 0, 0.14),
#     0px 1px 10px 0px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-5dp {
#     box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2),
#     0px 5px 8px 0px rgba(0, 0, 0, 0.14),
#     0px 1px 14px 0px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-6dp {
#     box-shadow: 0px 3px 5px -1px rgba(0, 0, 0, 0.2),
#     0px 6px 10px 0px rgba(0, 0, 0, 0.14),
#     0px 1px 18px 0px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-7dp {
#     box-shadow: 0px 4px 5px -2px rgba(0, 0, 0, 0.2),
#     0px 7px 10px 1px rgba(0, 0, 0, 0.14),
#     0px 2px 16px 1px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-8dp {
#     box-shadow: 0px 5px 5px -3px rgba(0, 0, 0, 0.2),
#     0px 8px 10px 1px rgba(0, 0, 0, 0.14),
#     0px 3px 14px 2px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-9dp {
#     box-shadow: 0px 5px 6px -3px rgba(0, 0, 0, 0.2),
#     0px 9px 12px 1px rgba(0, 0, 0, 0.14),
#     0px 3px 16px 2px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-10dp {
#     box-shadow: 0px 6px 6px -3px rgba(0, 0, 0, 0.2),
#     0px 10px 14px 1px rgba(0, 0, 0, 0.14),
#     0px 4px 18px 3px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-11dp {
#     box-shadow: 0px 6px 7px -4px rgba(0, 0, 0, 0.2),
#     0px 11px 15px 1px rgba(0, 0, 0, 0.14),
#     0px 4px 20px 3px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-12dp {
#     box-shadow: 0px 7px 8px -4px rgba(0, 0, 0, 0.2),
#     0px 12px 17px 2px rgba(0, 0, 0, 0.14),
#     0px 5px 22px 4px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-13dp {
#     box-shadow: 0px 7px 8px -4px rgba(0, 0, 0, 0.2),
#     0px 13px 19px 2px rgba(0, 0, 0, 0.14),
#     0px 5px 24px 4px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-14dp {
#     box-shadow: 0px 7px 9px -4px rgba(0, 0, 0, 0.2),
#     0px 14px 21px 2px rgba(0, 0, 0, 0.14),
#     0px 5px 26px 4px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-15dp {
#     box-shadow: 0px 8px 9px -5px rgba(0, 0, 0, 0.2),
#     0px 15px 22px 2px rgba(0, 0, 0, 0.14),
#     0px 6px 28px 5px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-16dp {
#     box-shadow: 0px 8px 10px -5px rgba(0, 0, 0, 0.2),
#     0px 16px 24px 2px rgba(0, 0, 0, 0.14),
#     0px 6px 30px 5px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-17dp {
#     box-shadow: 0px 8px 11px -5px rgba(0, 0, 0, 0.2),
#     0px 17px 26px 2px rgba(0, 0, 0, 0.14),
#     0px 6px 32px 5px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-18dp {
#     box-shadow: 0px 9px 11px -5px rgba(0, 0, 0, 0.2),
#     0px 18px 28px 2px rgba(0, 0, 0, 0.14),
#     0px 7px 34px 6px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-19dp {
#     box-shadow: 0px 9px 12px -6px rgba(0, 0, 0, 0.2),
#     0px 19px 29px 2px rgba(0, 0, 0, 0.14),
#     0px 7px 36px 6px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-20dp {
#     box-shadow: 0px 10px 13px -6px rgba(0, 0, 0, 0.2),
#     0px 20px 31px 3px rgba(0, 0, 0, 0.14),
#     0px 8px 38px 7px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-21dp {
#     box-shadow: 0px 10px 13px -6px rgba(0, 0, 0, 0.2),
#     0px 21px 33px 3px rgba(0, 0, 0, 0.14),
#     0px 8px 40px 7px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-22dp {
#     box-shadow: 0px 10px 14px -6px rgba(0, 0, 0, 0.2),
#     0px 22px 35px 3px rgba(0, 0, 0, 0.14),
#     0px 8px 42px 7px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-23dp {
#     box-shadow: 0px 11px 14px -7px rgba(0, 0, 0, 0.2),
#     0px 23px 36px 3px rgba(0, 0, 0, 0.14),
#     0px 9px 44px 8px rgba(0, 0, 0, 0.12); }
# .md-whiteframe-24dp {
#     box-shadow: 0px 11px 15px -7px rgba(0, 0, 0, 0.2),
#     0px 24px 38px 3px rgba(0, 0, 0, 0.14),
#     0px 9px 46px 8px rgba(0, 0, 0, 0.12); }