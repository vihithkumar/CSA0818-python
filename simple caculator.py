symbol = input("enter the '+' for addition '-' for subtraction '*' for multiplicstion and '/' for division")
if symbol == '+':
    num1 = int ( input("enter the 1st  number"))
    num2 = int (input ("enter the 2nd number"))
    print(num1+num2)
elif symbol == '-':
 num3 = int ( input("enter the 1st  number"))
num4 = int (input("enter the 2nd number"))
print(num1-num2)
elif symbol == '*':
         num5 = int ( input("enter the 1st  number"))
    num6 = int (input ("enter the 2nd number"))
    print(num1*num2)
elif symbol == '/':
         num7 = int ( input("enter the 1st  number"))
    num8 = int (input ("enter the 2nd number"))
    print(num1/num2)
else:
    print("please enter a valid symbol")
