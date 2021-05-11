run_var = True 
while run_var:

    first_var = int(input ("What is the first number?"))
    third_var = input ("what calculation do you want??")
    second_var = int(input ("What is the second number?"))


    def PLUS(FirstNumber, SecondNumber):
        result = FirstNumber + SecondNumber
        return result

    def SUBTRACT(FirstNumber, SecondNumber):
        result = FirstNumber - SecondNumber
        return result

    def Multiply(FirstNumber, SecondNumber):
        result = FirstNumber * SecondNumber
        return result

    def Divide(FirstNumber, SecondNumber):
        result = FirstNumber / SecondNumber
        return result

    if (third_var == "+"):
        result_var = PLUS(first_var, second_var)

    elif (third_var == "-"):
        result_var = SUBTRACT(first_var, second_var)

    elif (third_var == "*"):
        result_var = Multiply(first_var, second_var)

    elif (third_var == "/"):
        result_var = Divide(first_var, second_var)

    print (result_var)   

    fourth_var = input ("Run Again???")
    if (fourth_var != "y"):
        run_var = False

