from PySide2.QtWidgets import QWidget, QPushButton
class QMenuButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setFlat(True)