a=int(input("Enter first number"))
b=int(input("Enter the second number"))
op=input("Enter the operator")
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

if op=="+":
    add(a,b)
if op=="-":
    sub(a,b)
if op=="*":
    mul(a,b)
if op=="/":
    div(a,b)
