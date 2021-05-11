def function_one():

    return "One" 

def add(First, Second):

    result = First + Second

    return result

def minus(First, Second):

    result = First - Second

    return result

endnumber_var = int(input("Enter the last number"))

run = True

number = 1

while run:

    if (number <= endnumber_var):

        print(number)

    else:

        run = False

    

    number = number + 1

print("----")

for num in range(1, endnumber_var + 1):

    print(num)

print("----")

list = {1, 2, 3, 4, "Five", 6, 7, 8, "Nine"}

for num in list:

    print(num)