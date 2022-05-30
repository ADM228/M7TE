from PyQt5 import QtWidgets, uic, QtGui
import sys, os, json, configparser, Resources
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.version="1.3.0α"
        self.ui = uic.loadUi("Ui/Main.ui")
        self.ui.setWindowTitle("M7TE v"+self.version)
        self.parseSettings()
        self.localize()
        self.ui.centralwidget.resizeEvent = self.resizeEvent
        self.ui.show()
    def localize(self):
        self.locale = configparser.ConfigParser()
        self.locale.optionxform = str #making it case-insensitive
        if os.path.isfile("m7te.lang"):
            self.locale.read("m7te.lang",encoding="utf-8")
        self.localizedData = self.locale[self.config['M7TE']['language']]
        for key in self.localizedData:
            attr = getattr(self.ui, key)
            if str(type (attr)) == "<class 'PyQt5.QtWidgets.QMenu'>":
                attr.setTitle(self.localizedData[key])
            elif str(type (attr)) == "<class 'PyQt5.QtWidgets.QAction'>":
                attr.setText(self.localizedData[key])
        setattr (self.ui, key, attr)
        self.ui.menuHelpAbout.triggered.connect(self.buttonClickAbout)
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
    def resizeEvent(self,event):
        self.resizeGraphics()
        return super(MainWindow, self).resizeEvent(event)
    def resizeGraphics(self):
        if self.ui.frame.width() < self.ui.frame.height():
            diff = int((self.ui.frame.height() - self.ui.frame.width())/2)
            self.ui.frame.setContentsMargins(0,diff,0,diff)
        elif self.ui.frame.width() > self.ui.frame.height(): 
            diff = int((self.ui.frame.width() - self.ui.frame.height())/2)
            self.ui.frame.setContentsMargins(diff,0,diff,0)
        else:
            self.ui.frame.setContentsMargins(0,0,0,0)

        if self.ui.frame_2.width() < self.ui.frame_2.height():
            diff = int((self.ui.frame_2.height() - self.ui.frame_2.width()))
            self.ui.frame_2.setContentsMargins(0,0,0,diff)
        elif self.ui.frame_2.width() > self.ui.frame_2.height(): 
            diff = int((self.ui.frame_2.width() - self.ui.frame_2.height())/2)
            self.ui.frame_2.setContentsMargins(diff,0,diff,0)
        else:
            self.ui.frame_2.setContentsMargins(0,0,0,0)
    #Actions for buttons
    def buttonClickAbout(self):
        windows.append(AboutWindow(self, len(windows)))
        print(windows)
    
class AboutWindow(QtWidgets.QDialog):
    def __init__(self, main, index):
        super().__init__()
        self.version = main.version
        self.ui = uic.loadUi("Ui/About.ui")
        self.ui.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui.setWindowTitle("M7TE v"+self.version)
        self.ui.dialogAboutVersion.setText("M7TE v"+self.version)
        self.ui.closeEvent = self.closeEvent
        self.ui.show()
        self.index = index
        print(self.index)

    def closeEvent(self, event):
        del windows[self.index]
        event.accept()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    windows = [MainWindow()]
    sys.exit(app.exec_())