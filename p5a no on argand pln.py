import matplotlib.pyplot as plt

x=float(input("Enter Real Part:"))
y=float(input("Enter Imaginary Part:"))

plt.axhline(0)
plt.axvline(0)

plt.scatter(x,y)
plt.plot([0,x],[0,y],linestyle="--")

plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.title("Complex Number on Argand Plane")
plt.grid()
plt.show()
