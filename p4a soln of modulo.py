import math

a = int(input("Enter a:"))
b = int(input("Enter b:"))
m = int(input("Enter Modulus m:"))

solutions =[]

for x in range(m):
    if(a*x-b)%m==0:
        solutions.append(x)

if len(solutions)==0:
    print("No Solution Exists.")
else:
    print("solution Modulo",m,"are:",solutions)
