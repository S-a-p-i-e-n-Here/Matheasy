print("welcome to the simple calculator")
num1 = float(input("enter the first number:"))
operation = input("enter your operaton (+,-,*,/):")
num2 = float(input("enter the second number:"))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1*num2
elif operation == "/":
    if num2 != 0:
        result = num1/num2
    else:
        result =  "error ! division by 0" 
else:
    result = "invalid operation !"

print("result:", result)     




