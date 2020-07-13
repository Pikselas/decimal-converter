#decimal to binary,hexa,octal converter
#All functions for Binary conversion
import tkinter as ui
def BinaryConverter(num):
    print("**Steps For Binary Conversion**")
    BinaryList = []
    BinaryResult = ""
    result = num
    quationt = ""
    print("Taken number: "+str(num))
    while result >= 2:
        quationt = result % 2
        print("Division by 2 of Number:"+str(result))
        result = int(result/2)
        print("Result:"+str(result))
        print("quationt:"+str(quationt))
        BinaryList.append(quationt)
    print("Now we get 1 as Result So stop dividing")
    print("\n\n*PRINT LAST RESULTED 1 AS FIRST AND ALL QUATIONTS IN REVERSE*\n\n")
    BinaryList.append(1)
    print("As follows:\n")
    count = (len(BinaryList)-1)
    while count >= 0:
        print("Write "+str(BinaryList[count]))
        BinaryResult += str(BinaryList[count])
        count -= 1
    print("Final Result:"+BinaryResult)
    return BinaryResult
#All Functions For Hex Conversion
def HexAfterNine(num):
    if num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    else:
        return num
def HexConverter(num):
    HexList = []
    HexResult = ""
    result = num
    quationt = 0
    print("**Steps For Hexadecimal Conversion**")
    print("**NOTE:VALUES AFTER 9 TO 15 ARE CONSIDERED AS A-F**")
    print("Taken number: "+str(num))
    while result >= 16:
        print("Division by 16 of Number:"+str(result))
        quationt = HexAfterNine(result % 16)
        result = int(result/16)
        print("Result:"+str(result))
        print("quationt:"+str(quationt))
        HexList.append(quationt)
    print("Now we get "+str(result)+" which is less then 16 so stop dividing")
    print("\n\n*PRINT LAST RESULT AS FIRST AND ALL QUATIONTS IN REVERSE*\n\n")
    HexList.append(HexAfterNine(result))
    count = (len(HexList)-1)
    print("As follows:\n")
    while count >= 0:
        HexResult += str(HexList[count])
        print("Write "+str(HexList[count]))
        count -= 1
    print("Final Result:"+HexResult)
    return HexResult
def Convert():
    num = int(EntryForDecimal.get())
    BinaryVar.set(BinaryConverter(num))
    HexVar.set(HexConverter(num))
Body = ui.Tk()
Body.geometry("500x250")
Body.title("Decimal Converter")
BinaryVar = ui.StringVar()
HexVar = ui.StringVar()
LabelForDecimal = ui.Label(Body,text = "Enter Decimal Number:")
LabelForBinary = ui.Label(Body,text = "Get Binary Result:")
LabelForHex = ui.Label(Body,text = "Get Hexadecimal Result:")
EntryForDecimal = ui.Entry(Body)
EntryForBinary = ui.Entry(Body,textvariable = BinaryVar)
EntryForHex = ui.Entry(Body,textvariable = HexVar)
LabelForDecimal.grid(row = 0,column = 0)
EntryForDecimal.grid(row = 0,column = 1,ipadx = 15,ipady = 5)
LabelForBinary.grid(row = 2,column = 0)
EntryForBinary.grid(row = 2,column = 1,ipadx= 15,ipady = 5)
LabelForHex.grid(row = 4,column = 0)
EntryForHex.grid(row = 4,column = 1,ipadx = 15,ipady = 5)
ConvertButton = ui.Button(Body,text = "Convert",height = 2,width = 10,command = Convert)
ConvertButton.grid(row = 5,column = 1)
Body.mainloop()