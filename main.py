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
      
        
        '''possibility one: [1] = equity check  [2] = company name  [3] = first name   [8] = phone num   [13] = approval amount
                                                                                    if [8] != phone num { [9] = phone num }'''

        for i in range(len(data)):
            #just cause of alternating lines of mock leads
            if i % 2 == 0:
                #if colorcheck():
                    #need to connect these mockSend values to the message stored in self.message
                    self.console.append(
                        vonage.mockSend(
                            gs.firstNameFormat(data[i][3]), gs.getBusinessName(data[i][2]), data[i][gs.whichColumn(data[i][6])], gs.roundValue(data[i][13])
                        ))


#look into if name = main business
app = QtWidgets.QApplication([])
window = MainWindow()

stylesheet = """
QTextEdit {border-radius: 25px;}

QLabel {color:#F9F9F9;}

MainWindow {background-color: #7FC8F8;}
"""


app.setStyleSheet(stylesheet)
window.show()
app.exec()











