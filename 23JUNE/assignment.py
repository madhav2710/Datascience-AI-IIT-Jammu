
a=eval(input("Enter a list: "))
# a=[1,3,2,'Hzllo','Hello','hey']
b=[]
c=[]

def bubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

for i in a:
    if isinstance(i, int):
        print(f"{i} is a digit")
        b.append(i)
    if isinstance(i, str):
        print(f"{i} is an alphabet")
        c.append(i)

bubbleSort(b)
bubbleSort(c)
b.extend(c)
print(b)
print(c)