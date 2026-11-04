a=int(input("Enter first integer:"))
b=int(input("Enter second integer:"))

if b!=0:
    if a%b==0:
        print(a,"is divisible by" ,b)
    else:
        print(a,"is not divisible by",b)
else:
    print("Division by zero is not allowed")
