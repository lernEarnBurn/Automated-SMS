import modules.googleSheets as gs

import modules.vonageSMS as vonage

from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("./text.ui", self)


        self.message = self.findChild(QtWidgets.QTextEdit, "Message")

        self.firstRow = self.findChild(QtWidgets.QSpinBox, "firstRow")
        

        self.lastRow = self.findChild(QtWidgets.QSpinBox, "lastRow")

        self.button = self.findChild(QtWidgets.QPushButton, "btn")

        self.console = self.findChild(QtWidgets.QTextBrowser, "console")


        self.button.clicked.connect(self.runBlaster)

    
    def runBlaster(self):
        data = gs.readSpreadsheet(str(self.firstRow.value()), str(self.lastRow.value()))
       

        for i in range(len(data)):
            try:
                vonage.mockSend(self.message.toPlainText(), data[i][4])
                self.console.append(f"sent {self.message.toPlainText()} to {data[i][4]}")
            except:
                self.console.append('error')


#look into if name = main business
app = QtWidgets.QApplication([])
window = MainWindow()

stylesheet = """
QTextEdit {border-radius: 40px; border: 2px red;}

QLabel {color:#F9F9F9;}

MainWindow {background-color: #7FC8F8;}
"""

app.setStyleSheet(stylesheet)
window.show()
app.exec()











