num1 = input('please enter a whole number')
num2=input('now enter another number')

print('input is made up of  ',type(num1) , type(num2))

total = num1 + num2
print('total is ', total, type(total))

total = int(num1) + int(num2)
print('total is ', total, type(total))

total = float(num1) + float(num2)
print('total is ', str(total), type(total))
