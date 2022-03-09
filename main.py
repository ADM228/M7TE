from PyQt5 import QtWidgets, uic, QtGui
import sys, os, json, configparser
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.version="1.1.0"
        self.ui = uic.loadUi("Ui/Main.ui")
        self.ui.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.setWindowTitle("M7TE v"+self.version+"α")
        self.parseSettings()
        self.localize()
        self.ui.show()
    def localize(self):
        self.locale = configparser.ConfigParser()
        if os.path.isfile("m7te.lang"):
            self.locale.read("m7te.lang",encoding="utf-8")
        self.localizedData = self.locale[self.config['M7TE']['language']]
        print(self.ui.menuFile.title())
        for menu in self.ui.menu.findChildren(QtWidgets.QWidget):
            try:
                print (menu.title())
            except: pass
            try:
                print (menu.value())
            except: pass
            # menu.setTitle(self.localizedData[menu.title()])
        print("------------")
        for action in self.ui.menu.actions():
            print (action.text())
            for action2 in action.findChildren(QtWidgets.QWidget):
                print (action2.text())
            # action.setText(self.localizedData[action.text()])
    def parseSettings(self):
        self.config = configparser.ConfigParser()
        if os.path.isfile("m7te.cfg"):
            self.config.read("m7te.cfg",encoding="utf-8")
        else:
            self.config['M7TE'] = {
                'language': 'en_us',
                'recent': (json.loads("[]"))
            }
            with open("m7te.cfg", 'w') as file:
                self.config.write(file)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())