a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
m=int(input("Enter Modulus:"))

print("\n---Properties of congurence ---")

#Reflexive
if (a-a)%m==0:
    print("1.Reflexive property:True")

#Symmetric
if (a-b)%m==0:
    print("2.Symmetric property:True")

#Transitive
if (a-b)%m==0 and (b-c)%m==0:
    print("3.Transitive property:True")

#Addition
if (a-b)%m==0:
    if (a+c-(b+c)%m==0):
        print("4.Addition property:True")

#Substraction
    if (a-b)%m==0:
        if (a-c-(b-c))%m==0:
            print("5.Substraction property:True")
            
#multiplication
if (a-b)%m==0:
    if (a*c-b*c)%m==0:
        print("6.Multiplication property:True")

#Power
n=int(input("Enter power n:"))

if (a-b)%m==0:
    if(a**n-b**n)%m==0:
        print("7.Power property:True")
        





































