import cmath
import math

a=float(input("Enter Real Part:"))
b=float(input("Enter Imaginary Part:"))

n=int(input("Enter Power n:"))

z=complex(a,b)

r=abs(z)
theta=cmath.phase(z)

result=(r**n)*(math.cos(n*theta)+1j+math.sin(n*theta))

print("\nComplex number z=",z)
print("Modulus r=",r)
print("Argument theta=",math.degrees(theta),"degress")

print("\nUsing De Moivre's theorem:")
print("z^n=",result)

print("\nDirect Python calculation:")
print("z^n=",z**n)
