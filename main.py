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
        self.locale.optionxform = str #making it case-insensitive
        if os.path.isfile("m7te.lang"):
            self.locale.read("m7te.lang",encoding="utf-8")
        self.localizedData = self.locale[self.config['M7TE']['language']]
        for key in self.localizedData:
            #print(key, self.localizedData[key])
            attr = getattr(self.ui, key)
            if str(type (attr)) == "<class 'PyQt5.QtWidgets.QMenu'>":
                attr.setTitle(self.localizedData[key])
            elif str(type (attr)) == "<class 'PyQt5.QtWidgets.QAction'>":
                attr.setText(self.localizedData[key])
            #attr.setText(self.localizedData[key])
            
            #attr.value = self.localizedData[key]
            setattr (self.ui, key, attr)
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