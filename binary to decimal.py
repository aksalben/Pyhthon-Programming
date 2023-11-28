n=int(input("enter the number "))
b=1
de=0
while(n):
    d=n%10
    n=n//10
    de=de+d*b
    b=b*2
print(de)
