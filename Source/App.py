from PyQt6.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

from Globals import *
from Window import Window
from Worker import Worker

# application = QApplication(sys.argv)

class Application(QApplication):
	def __init__(self):
		super().__init__(sys.argv)
		self.window = Window()
		self.threadpool = QThreadPool()

	def processText(self, text):
		# TODO: Complete this
		pass

	def updateOutputDisplay(self, text):
		# TODO: Complete this
		pass

	def triggerTextProcessing(self):
		inputText = ""	# TODO: Retrieve text from input widget element
		worker = Worker(self.processText, inputText)
		# TODO: Retrieve output from worker
		worker.signals.result.connect(self.updateOutputDisplay)	# TODO: Pass output to display update
		self.threadpool.start(worker)
		# TODO: Retrieve output from worker, then display on ouput widget element

	def run(self):
		print("Starting app...")
		self.window.show()
		sys.exit(super().exec())
		print("Stopping app...")

app = Application()
app.run()