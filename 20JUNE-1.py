a =int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))

s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The semi-perimeter of the triangle is:", s)
print("The area of the triangle is:", area)