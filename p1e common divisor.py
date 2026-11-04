a = int(input("Enter first integer:"))
b = int(input("Enter second integer:"))

print("Common Divisors are:")

for i in range(1, min(abs(a),abs(b))+1):
    if a%1==0 and b%i==0:
        print(i, end=" ")
