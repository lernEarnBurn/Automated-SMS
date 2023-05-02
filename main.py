import modules.googleSheets as gs

import modules.database as database

import modules.bot as bot
import modules.responseCheck as rc

import customtkinter

import asyncio


def blitUI():
    customtkinter.set_appearance_mode("dark")  
    customtkinter.set_default_color_theme("blue") 

    APP_HEIGHT = 500
    APP_WIDTH = 700

    storedValues = database.readDatabase()

    app = customtkinter.CTk() 
    app.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
    app.title("Mass SMS")


    console = customtkinter.CTkTextbox(app, width=((APP_WIDTH - 10) / 2), height=((APP_HEIGHT - 10)), font=('system-ui', 16))
    console.grid(row=0, column=0, pady=5, padx=5, sticky="w")

    console.insert("1.0", "new text to insert") 
    console.insert("end", "\nthis is the end")
    console.configure(state="disabled")
  


    frame = customtkinter.CTkFrame(master=app)
    frame.grid(row=0, column=1, pady=5, padx=5, sticky="news")

    messageBox = customtkinter.CTkTextbox(frame, height=(((APP_HEIGHT / 2.5) - 10)), font=('system-ui', 14))
    messageBox.grid(row=0, column=0, pady=(5, 65), padx=5, sticky="new")
    messageBox.insert("1.0", storedValues[0]) 

    text = messageBox.get("1.0", "end")  
    print(text)
    

    starting_row = customtkinter.CTkEntry(frame, width=APP_WIDTH / 2.9,  placeholder_text="Starting Row", justify="center", font=('system-ui', 12))
    starting_row.grid(row=1, column=0, padx=50, pady=13)
    starting_row.insert(0, storedValues[1])

    ending_row = customtkinter.CTkEntry(frame, width=APP_WIDTH / 2.9, placeholder_text="Ending Row", justify='center', font=('system-ui', 12))
    ending_row.grid(row=2, column=0, padx=50, pady=13)
    ending_row.insert(0, storedValues[2])
    print(ending_row.get())


    button = customtkinter.CTkButton(master=frame, width=APP_WIDTH / 2.9, text="Run", command=asyncio.run(runBlaster()))
    button.grid(row=3, column=0, padx=10, pady=13, sticky="s")
    

    app.mainloop()

   
    async def runBlaster():
        first_row_value = starting_row.get()

        database.writeToDatabase(messageBox.get("1.0", "end"), first_row_value, ending_row.get())
        data = gs.fetchData(first_row_value, ending_row.get())
        rowCounter = first_row_value

        message = messageBox.get("1.0", "end")
        bot.openBrowser()


        for i in range(len(data)):
            await console.insert("end", f'\nsending message to {data[i][gs.whichColumn(data[i][6])]}...')
            newMessage = message.format(firstName=gs.formatFirstName(data[i][2]), businessName=gs.formatBusinessName(data[i][1]), approvalAmount=gs.roundApproval(data[i][12]))

            await bot.sendMessage(eval(newMessage), gs.formatNumber(data[i][gs.whichColumn(data[i][6])]))
            await gs.markSent(rowCounter)
            rowCounter += 1


       
        console.insert("end", '\n\nChecking for responses...')
        rc.markResponses(console)

        console.insert("end", '\n\nDone')


if __name__ == '__main__':
    blitUI()



    
