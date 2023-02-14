import modules.googleSheets as gs

import modules.database as database

import modules.bot as bot

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
      
        
        message = self.message.toPlainText()
        #print(message)

       
        for i in range(len(data)):
            #if colorcheck():

            newMessage = message.format(firstName=gs.formatFirstName(data[i][3]), businessName=gs.formatBusinessName(data[i][2]), approvalAmount=gs.roundApproval(data[i][13]))
            print(f'{eval(newMessage)} to {gs.formatNumber(data[i][gs.whichColumn(data[i][6])])}\n\n')
            bot.sendMessage(eval(newMessage), gs.formatNumber(data[i][gs.whichColumn(data[i][6])]))
        


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

