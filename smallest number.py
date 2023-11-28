a=int(input("Enter the first number"))
b=int(input("Enter the second number"))
c=int(input("enter the third number"))
smallest=0
if a<b and a<c:
    smallest=a
elif b<a and b<c:
    smallest = b
else:
    smallest= c
    
print(smallest)
