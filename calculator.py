num1=input("first number: \n")
operator=input("operator(+,-,*,/):\n")
num2=input("second number: \n")
num1=float(num1)
num2=float(num2)
out=0
if operator=="+":
    out=num1+num2
elif operator=="-":
    out=num1-num2
elif operator=="*":
    out=num1*num2
elif operator=="/":
    out=num1/num2
print("answer:"+str(out))
