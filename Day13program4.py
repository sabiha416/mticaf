def printSun():
    print("Sunday")
    return
def printMon():
    print("Monday")
def printTue():
    print("Tuesday")
def printWed():
    print("Wednesday")
def printThu():
    print("Thursday")
def printFri():
    print("Friday")
def printSat():
    print("Saturday")
def choice():
    print("Enter day number between 1-7")
dayDict={1:printSun, 2:printMon, 3:printTue, 4:printWed, 5:printThu, 6:printFri, 7:printSat}
choice()
dayNo=int(input())
if dayNo>=1 and dayNo<=7:
    dayDict[dayNo]()
else:
    print("INVALID")

   
