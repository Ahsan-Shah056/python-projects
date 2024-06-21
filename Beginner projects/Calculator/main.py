from drawing import logo



def add(n1,n2):
    return n1+n2

def multiply(n1,n2):
    return n1*n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2



symbols = {
    "+" :add,
    "-" :subtract,
    "*" :multiply,
    "/" :divide,
           }
def calculator():
    print (logo)
    num1=float(input("Enter the first number: "))


    for letter in symbols:
        print (letter)

    should_continue = True
    
    while should_continue:
        num2=float(input("Enter the next number: "))
        operation = input("Enter an operator from the list above which you want to use: ") 

        calculation_function = symbols[operation]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        
        if input("Enter Y to continue calculating or enter N to start a new calculation: ") =='y':
            num1 =answer
        else:
            should_continue = False
            calculator()
               
calculator()

