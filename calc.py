import os
import sys
import time
from PyQt5 import QtWidgets,QtGui

class Converter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_conv()
    
    def init_conv(self):
        self.pict = QtWidgets.QLabel()
        self.pict.setPixmap(QtGui.QPixmap("picture.jpg"))
        self.iconthing = QtWidgets.QLabel()
        self.text = QtWidgets.QLabel("Welcome, this program is converting your python file to exe")
        self.folderoftheexefile = QtWidgets.QLineEdit("The name of folder that your program will stay in")
        self.thenameoffile = QtWidgets.QLineEdit("Name of your python file")
        self.options = QtWidgets.QLabel("<Options>\n")
        self.optionone = QtWidgets.QCheckBox("Don't show console in the program")
        self.optiontwo = QtWidgets.QCheckBox("Only show one file")
        self.button = QtWidgets.QPushButton("Convert to exe")
        self.situation = QtWidgets.QLabel("")

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.pict)
        v_box.addWidget(self.text)
        v_box.addWidget(self.thenameoffile)
        v_box.addWidget(self.folderoftheexefile)
        v_box.addWidget(self.options)
        v_box.addWidget(self.optionone)
        v_box.addWidget(self.optiontwo)
        v_box.addWidget(self.button)
        v_box.addWidget(self.situation)

        self.setLayout(v_box)

        self.setWindowTitle("Convert .py to .exe[Barış ERTAN]")
        self.setWindowIcon(QtGui.QIcon("picture.jpg"))
        self.setGeometry(500,100,500,500)

        self.show()

        self.button.clicked.connect(self.controller)
    
    def controller(self):
        self.thenameoffile = self.thenameoffile.text()
        self.folderoftheexefile = self.folderoftheexefile.text()
        try:
            if self.optionone.isChecked() and self.optiontwo.isChecked():
                self.situation.setText("Converting...")
                os.mkdir(self.folderoftheexefile)
                self.copyofthething = ""
                with open(self.thenameoffile,"r+",encoding="UTF-8") as copythat:
                    self.copyofthething = copythat.read()

                os.chdir(self.folderoftheexefile)
                with open(self.thenameoffile,"w",encoding="UTF-8") as abcdl:
                    abcdl.write(self.copyofthething)

                os.system("pyinstaller {} --onefile --noconsole".format(self.thenameoffile))
                self.situation.setText("Converted {} to exe!".format(self.thenameoffile))
            if self.optionone.isChecked():
                self.situation.setText("Converting...")
                os.mkdir(self.folderoftheexefile)
                self.copyofthething = ""
                with open(self.thenameoffile,"r+",encoding="UTF-8") as copythat:
                    self.copyofthething = copythat.read()
                    
                os.chdir(self.folderoftheexefile)
                with open(self.thenameoffile,"w",encoding="UTF-8") as abcdl:
                    abcdl.write(self.copyofthething)

                os.system("pyinstaller {} --noconsole".format(self.thenameoffile))
                self.situation.setText("Converted {} to exe!".format(self.thenameoffile))
            if self.optiontwo.isChecked():
                self.situation.setText("Converting...")
                os.mkdir(self.folderoftheexefile)
                self.copyofthething = ""
                with open(self.thenameoffile,"r+",encoding="UTF-8") as copythat:
                    self.copyofthething = copythat.read()
                    
                os.chdir(self.folderoftheexefile)
                with open(self.thenameoffile,"w",encoding="UTF-8") as abcdl:
                    abcdl.write(self.copyofthething)
                    
                os.system("pyinstaller {} --onefile".format(self.thenameoffile))
                self.situation.setText("Converted {} to exe!".format(self.thenameoffile))
            else:
                self.situation.setText("Failed, please make sure about\n that there is a file named as {} and you have pyinstaller\n Write 'pip/pip3 install pyinstaller' to download it".format(self.thenameoffile))
        except:
            self.situation.setText("Failed, please make sure about\n that there is a file named as '{}' and you have pyinstaller\n Write 'pip/pip3 install pyinstaller to download it".format(self.thenameoffile))



app = QtWidgets.QApplication(sys.argv)

window = Converter()

sys.exit(app.exec())

"""
os.mkdir("{}".format(self.folderoftheexefile))
os.chdir(self.folderoftheexefile)
"""

