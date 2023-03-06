from bot import closeBrowser, getResponseNumbers
from database import writeCurrentResponses, readPrevResponses
from googleSheets import getRowData, markResponse

def markResponses(console):
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
        

        sheetData1 = getRowData(4500, 'I')
        sheetData2 = getRowData(4500, 'J')

        findAndMarkResponse(sheetData1, unmarkedResponses, console)
        findAndMarkResponse(sheetData2, unmarkedResponses, console)

        writeCurrentResponses(currentResponses)

    
def findAndMarkResponse(data, numbersToFind, console):
     for i in range(len(data)):
        if data[i]['value'] in numbersToFind and len(data[i]['value']) == 11:
            markResponse(data[i]['row'])
            console.append(f"added response to row {data[i]['row']}")
            


if __name__ == '__main__':
    markResponses()
    