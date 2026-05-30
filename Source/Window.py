from PyQt6.QtWidgets import QApplication, QWidget, QLabel

from Globals import *

class Window(QWidget):
	def __init__(self):
		super().__init__()
		super().setWindowTitle(WINDOW_TITLE)
		super().resize(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
		self.__populateWindowElements()
	
	def __populateWindowElements(self):
		label = QLabel("Test Label", parent=self)