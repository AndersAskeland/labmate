# -----------------------------------------------------------------------------
# Module: User interface
#
# What: User interface logic and definitions.
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
# External modules 
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QFile, QSize
from PySide2.QtGui import QIcon
from PySide2.QtSvg import QSvgRenderer, QSvgWidget

# Local functions 

# Local classes 
from resources.user_interface.mainwindow import Ui_MainWindow
# Local resources 


# ------------------------------------------------------------------------------
# 2 - Classes
# ------------------------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):
    '''Main user interface window.
    
    Class that contains all functions and interactions related to
    the main user interace, including initialization of ui, loading
    custom widgets and settings and establishing ui connections.

    Inherits UI file from resources/user_interface/mainwindow.ui.

    Args:
        None
    
    Attributes:
        None
    '''

    # ---- Constructor ---- #
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        # General variables

        # Define user interface
        self.setupUi(self)
        self.setWindowTitle("labmate")

        window_size = QSize(1350/1.4, 800/2)
        self.resize(window_size)
        self.setFixedSize(window_size)

        
        # Signals

    # ---- Slots ---- #

    # ---- Functions ---- #

    # ---- Dialogs ---- #
