import modules.googleSheets as gs

import modules.database as database

import modules.bot as bot
import modules.responseCheck as rc

import tkinter
import customtkinter


'''

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

        rowCounter = self.firstRow.value()
      
        message = self.message.toPlainText()

        bot.openBrowser()

       
        for i in range(len(data)):

            self.console.append(f'sending message to {data[i][gs.whichColumn(data[i][6])]}...')

            newMessage = message.format(firstName=gs.formatFirstName(data[i][2]), businessName=gs.formatBusinessName(data[i][1]), approvalAmount=gs.roundApproval(data[i][12]))
            
            bot.sendMessage(eval(newMessage), gs.formatNumber(data[i][gs.whichColumn(data[i][6])]))

            gs.markSent(str(rowCounter))
            rowCounter += 1
           
        
        self.console.append('')
        self.console.append('Checking for responses...')

        rc.markResponses(self.console)
        
        self.console.append('Done.')
'''

if __name__ == '__main__':
    customtkinter.set_appearance_mode("dark")  
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    APP_HEIGHT = 500
    APP_WIDTH = 700

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
    app.grid_columnconfigure(0, weight=1)

    def button_function():
        print("button pressed")

    # Use CTkButton instead of tkinter Button
    button = customtkinter.CTkButton(master=app, text="Run", command=button_function)
    button.grid(row=0, column=1, padx=10, pady=10, sticky="se")
    scrollable_frame = customtkinter.CTkScrollableFrame(app, width=200, height=200)

    entry = customtkinter.CTkEntry(app, placeholder_text="CTkEntry")
    #entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

    frame = customtkinter.CTkFrame(master=app, width=((APP_WIDTH - 10) / 2 ), height=(APP_HEIGHT - 10))
    frame.grid(row=0, column=0, pady=5, padx=5, sticky="w")



    textbox = customtkinter.CTkTextbox(app, width=(APP_WIDTH - 10) / 2, height=())
    textbox.grid(row=0, column=1, pady=5, padx=5, sticky="ne")

    textbox.insert("0.0", "new text to insert")  # insert at line 0 character 0
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
    


    app.mainloop()




    
