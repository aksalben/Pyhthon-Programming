print("Enter the mark of 5 subjects")
sum=0
for i in range(1,6):
     print("mark",i)
     i=float(input())
     sum+=i
print("sum =",sum)
avg=sum/5
print("avg =",avg)
