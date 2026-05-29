from Globals import *

print("Running app!")

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("HTML Reader")
window.setGeometry(100, 100, 800, 600)

label = QLabel("Test Label", parent=window)

window.show()

sys.exit(app.exec())