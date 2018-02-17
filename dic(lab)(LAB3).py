import math

list = {}
ran = int(input("enter the rnage"))
for i in range(ran):
    a = int(input("enter values"))
    list[i] = math.sqrt(a)
print(list)
