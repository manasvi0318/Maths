a = int(input("Enter first integer:"))
b = int(input("Enter second integer:"))

while b!=0:
    reminder=a%b
    a=b
    b=reminder
print("GCD=",abs(a))

