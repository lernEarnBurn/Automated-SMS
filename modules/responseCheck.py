from modules.bot import closeBrowser, getResponseNumbers, checkIfResponses
from modules.database import writeCurrentResponses, readPrevResponses
from modules.googleSheets import getRowData, markResponse

def markResponses(console, endRowVal):
        # need to figure out this non async shitstorm  
        if checkIfResponses():
            currentResponses = getResponseNumbers()
            
            closeBrowser()

            prevResponses = readPrevResponses()[0].split()
            if len(currentResponses) > len(prevResponses): 
                unmarkedResponses = []
                for i in range(len(currentResponses)):
                    if currentResponses[i] in prevResponses:
                        pass
                    else:
                        unmarkedResponses.append(currentResponses[i])

                print(len(unmarkedResponses))
                print(unmarkedResponses)


                sheetData1 = getRowData(endRowVal, 'I')
                sheetData2 = getRowData(endRowVal, 'J')

                numberFound = []

            findAndMarkResponse(sheetData1, unmarkedResponses, console, numberFound)
            findAndMarkResponse(sheetData2, unmarkedResponses, console, numberFound)

            writeCurrentResponses(numberFound)
        else:
            closeBrowser()


    
def findAndMarkResponse(data, numbersToFind, console, arr):
     for i in range(len(data)):
        if data[i]['value'] in numbersToFind and len(data[i]['value']) == 11:
            markResponse(data[i]['row'])
            console.insert("end", f"\nresponse at row {data[i]['row']}")
            arr.append(data[i]['value'])
            


if __name__ == '__main__':
    print(getResponseNumbers())
    