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
    
    #read operator until allowed one
    allowedoperators = '+-*/%'
    operator="aa"
    while len(operator) != 1 or operator not in allowedoperators:
        operator=input("operator: ")

    while 1:
        number2 = input("second number: ")
        try:
            number2=float(number2.replace(",","."))
            break
        except:
            print("enter a number, not a text")

    if operator == "+":
        result=number1+number2
    if operator == "-":
        result=number1-number2
    if operator == "*":
        result=number1*number2
    if operator == "/":
        result=number1/number2

    string=str(number1)+operator+str(number2)+"= "+str(result)
    print(string)