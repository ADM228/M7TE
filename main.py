from PyQt5 import QtWidgets, uic, QtGui
import sys, os, json, configparser
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.version="1.0.0"
        self.ui = uic.loadUi("Ui/Main.ui")
        self.ui.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.setWindowTitle("M7TE v"+self.version+"α")
        self.parseSettings()
        self.localize("Alex")
        self.ui.show()
    def localize(self,lang):
        pass
    def parseSettings(self):
        pass

Lang = """
[en_us]:
menu.file = File

"""

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())