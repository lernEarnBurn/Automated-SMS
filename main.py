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
        storedValues = database.readDatabase()
        database.writeToDatabase(self.message.toPlainText(), str(self.firstRow.value()), str(self.lastRow.value()))

        data = gs.fetchData(str(self.firstRow.value()), str(self.lastRow.value()))
      
        message1 = storedValues[3]
        message2 = self.message.toPlainText()

       
        for i in range(len(data)):
            #if colorcheck():
            newMessage1 = message1.format(firstName=gs.formatFirstName(data[i][2]))
            newMessage2 = message2.format(businessName=gs.formatBusinessName(data[i][1]), approvalAmount=gs.roundApproval(data[i][12]))
            
            bot.sendMessage(eval(newMessage1), gs.formatNumber(data[i][gs.whichColumn(data[i][6])]))
            bot.sendMessage(eval(newMessage2), gs.formatNumber(data[i][gs.whichColumn(data[i][6])]))
            self.console.append(f'sent message to {data[i][gs.whichColumn(data[i][6])]}')

        
        self.console.append('Done.')


if __name__ == '__main__':
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

