A= input("Enter a INPUT: ")
B= input("Enter a INPUT: ")

if A.isdigit() and B.isdigit():
    A = int(A)
    B = int(B)
    if(A and B > 0 and A < 1000 and B < 1000):
        mul= A * B
        if mul % A == 0 and mul % B == 0:
            print("The product is divisible by both inputs.")
        else:
            print("The product is not divisible by both inputs.")
    else:
        print("Inputs are not in range 0-1000")
elif A.isalpha() and B.isalpha():
   con= A + B
   if(A[0]==B[0]):
       print("both inputs are same")
elif A.isalnum() and B.isalnum():
    if(A.isdigit() and B.isalpha()):
        for i in range(int(A)):
            print(B)
    elif(A.isalpha() and B.isdigit()):
        for i in range(int(B)):
            print(A)
else:
    print("Inputs are not ")

print("End of program")


a="madhav123"
print(a.isdigit())
print(a.isalpha())
print(a.isalnum())
print(a.capitalize())
print(a.upper())
print(a.isspace())
print(a.islower())
print(a.isupper())
print(a.isnumeric())
print(a.isdecimal())
print(a.isidentifier())
print(a.isprintable())
