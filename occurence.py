b=[]
n=int(input('Enter number of names:'))
for i in range(n):
    name=(input('Enter the first name:'))
    b.append(name)
print(b)
a=str(b)
count=0   
for i in a:
    if i=='a':
        count=count+1
        
print("the total count is",count)
