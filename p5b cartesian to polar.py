import cmath
import math

x=float(input("Enter Real Part:"))
y=float(input("Enter Imaginary Part:"))

z=complex(x,y)

r,theta=cmath.polar(z)

theta_degree=math.degrees(theta)
print("\nComplex Number=",z)
print("Mudulus (r)=",r)
print("Argument (theta) in radians=",theta)
print("Argument (theta) in degrees=",theta_degree)
print("\nPolar form:")
print(f"{r:.2f}(cos({theta_degree:.2f}) + i sin({theta_degree:.2f}))")
