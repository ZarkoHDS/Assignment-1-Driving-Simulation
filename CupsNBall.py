import sys
number=["1","0","0"]
x=input(str("Insert Your Word :"))
def swapA():
    a=number.pop(1)
    b=number.pop(0)
    number.insert(0,a)
    number.insert(1,b)
def swapB():
    a=number.pop(2)
    b=number.pop(1)
    number.insert(1,a)
    number.insert(2,b)
def swapC():
    a=number.pop(2)
    b=number.pop(0)
    number.insert(0,a)
    number.insert(2,b)

for i in range(0,len(x)):
    if x[i]=="a":
        swapA()
    elif x[i]=="b":
        swapB()
    elif x[i]=="c":
        swapC()

for z in range(3):
    if number[z]=="1":
        print((z)+1)



