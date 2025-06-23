a=[1,3,2,'Hzllo','Hello','hey']
b=[]
c=[]


for i in a:
    if isinstance(i, int):
        print(f"{i} is a digit")
        b.append(i)
    elif isinstance(i, str) and i.isalpha():
        print(f"{i} is an alphabet")
        c.append(i)

b.sort()
c.sort()
b.extend(c)
print(b)
