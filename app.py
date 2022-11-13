from automation import automation
from PyQt6 import QtGui
from PyQt6.QtWidgets import *
import sys

#Class to create window (cant take function so I create 1 more class to take the automation func as param)
class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Automation Tool for Sorting Bottle Dataset")
        self.setFixedSize(400, 100)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.createDisplay()
        self.create_epsillon()


    def createDisplay(self):
        self.display = QVBoxLayout()
        self.button_folder = QPushButton("Your folder")
        self.display.addWidget(self.button_folder)
        self.generalLayout.addLayout(self.display)
        self.button_run = QPushButton("Run")
        self.display.addWidget(self.button_run)
        self.generalLayout.addLayout(self.display)

    def create_epsillon(self):
        self.type = QFormLayout()
        self.epsillon = QLineEdit(self)
        self.type.addRow("Epsillon >= 0 (default = 0)",self.epsillon)
        self.generalLayout.addLayout(self.type)
    
    ### :))) Basically this func belongs to second class, but this class uses attribute from Qtpy -> it can implement the choosing folder func easier
    def onclick_folder(self):
        self.path =  str(QFileDialog.getExistingDirectory(self, "Select Directory"))


#This class implement automation
class App_run:
    def __init__(self, view, automation):
        self._view = view
        self.automation = automation
        self.run()

    def onclick_run(self):
        try:
            if self._view.epsillon.text() == "":
                self.automation(self._view.path, 0)
            elif int(self._view.epsillon.text()) < 0:
                self.automation(self._view.path, 0)
            else:
                self.automation(self._view.path, int(self._view.epsillon.text()))
            print("OK")
        except:
            pass

    def run(self):
        try:
            self._view.button_folder.clicked.connect(self._view.onclick_folder)
        except:
            pass

        try:
            self._view.button_run.clicked.connect(self.onclick_run)
        except:
            pass

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QtGui.QIcon('icon.ico'))
    window = Window()
    app_run = App_run(window,automation)
    window.show()
    sys.exit(app.exec())