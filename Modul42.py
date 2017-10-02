number=[]
for i in range(10):
    number.append(int(input())%42)
print(number)
print(set(number))
print(len(set(number)))
