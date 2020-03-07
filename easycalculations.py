print("easy calculation\n================")

while 1:
    #read first number until float value
    while 1:
        number1 = input("first number: ")
        try:
            number1=float(number1.replace(",","."))
            break
        except:
            print("enter a number, not a text")
    while 1:
        #read operator until allowed one
        allowedoperators = '+-*/'
        
