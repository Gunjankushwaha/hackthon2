
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))
if num1<num2 and num2>num3:
    print(num2," is greater")
elif num2<num3 and num3>num1:
    print(num3," is greater")
elif num1>num2 and num1>num3:
    print(num1,"it is greater")
else:
    print("it is second number")