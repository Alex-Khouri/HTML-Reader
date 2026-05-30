from PyQt6.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot

class WorkerSignals(QObject):
    finished = pyqtSignal()
    result = pyqtSignal(object)

class Worker(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        res = self.function(*self.args, **self.kwargs)
        self.signals.result.emit(res)
        self.signals.finished.emit()