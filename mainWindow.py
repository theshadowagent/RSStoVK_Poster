import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import autoUpdate
import pyqt


class MainWindow(QtGui.QMainWindow, pyqt.UIDialog):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setup_UI(self)
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.start_rss)

    def start_rss(self):
        time_interval = QtGui.QLineEdit('', self.LineEdit_2)
        autoUpdate.main(time_interval)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())

