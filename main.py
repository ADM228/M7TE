from PyQt5 import QtWidgets, uic, QtGui
app = QtWidgets.QApplication([])

ui = uic.loadUi("Ui/Main.ui")
ui.setWindowIcon(QtGui.QIcon('icon.ico'))

ui.show()
app.exec()