import matplotlib.pyplot as plt

a=2
d=3
n=10

sequence=[]

for i in range(n):
    term=a+i*d
    sequence.append(term)

print("Arithmetic Sequence:")
print(sequence)

plt.plot(range(1,n+1),sequence,marker='o')
plt.xlabel("n")
plt.ylabel("a(n)")
plt.title("Arithematic Sequence")
plt.grid()
plt.show()
