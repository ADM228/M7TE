from PyQt5 import QtWidgets, uic, QtGui
version = "0.1.0"
app = QtWidgets.QApplication([])

ui = uic.loadUi("Ui/Main.ui")
ui.setWindowIcon(QtGui.QIcon('icon.ico'))
ui.setWindowTitle("M7TE v"+version)

ui.show()
app.exec()