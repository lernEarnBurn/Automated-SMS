import modules.googleSheets as gs

import modules.vonageSMS as vonage

import modules.database as database

from PyQt6 import QtWidgets, uic


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("./text.ui", self)

        storedValues = database.readDatabase()


        self.message = self.findChild(QtWidgets.QTextEdit, "Message")
        self.message.setText(storedValues[0])

        self.firstRow = self.findChild(QtWidgets.QSpinBox, "firstRow")
        self.firstRow.setRange(0, 99999)
        self.firstRow.setValue(int(storedValues[1]))

        self.lastRow = self.findChild(QtWidgets.QSpinBox, "lastRow")
        self.lastRow.setRange(0, 99999)
        self.lastRow.setValue(int(storedValues[2]))

        self.button = self.findChild(QtWidgets.QPushButton, "btn")

        self.console = self.findChild(QtWidgets.QTextBrowser, "console")

        self.button.clicked.connect(self.runBlaster)

    
    def runBlaster(self):
        database.writeToDatabase(self.message.toPlainText(), str(self.firstRow.value()), str(self.lastRow.value()))

        data = gs.fetchData(str(self.firstRow.value()), str(self.lastRow.value()))

        for i in range(len(data)):
            #put error handling in the method, might not be neccesary
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











