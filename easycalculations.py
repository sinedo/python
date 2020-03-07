count=0
number1=""
operator=""
number2=""
result=""

print("easy calculation\n================")


while 1:
    while 1:
        number1 = input("first number: ")
        try:
            number1=inputnumber(number1)
            break
        except:
            error(1)
        
'''
    number1=inputnumber(number1)
    operator=print("operator: ")
    inputoperator(operator)
    number2=input("second number: ")
    inputnumber(number2)
    calculate(number1, number2, operator)
'''







def error(nr):
    if nr == 1:
        print("enter a number, not a text")
        

def inputnumber(string):
    string=string.replace(",",".")
    return float(string)


#def inputoperator(string):

#def calculate(n1,n2,o):