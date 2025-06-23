from math import sqrt

a=int(input("Enter a number: "))
if(a==1):
    print("1 is not a prime number")
    exit()
elif(a < 1):
    print("Number should be greater than 0")
    exit()
else:
    while a > 1:
        for i in range(2, int(sqrt(a)) + 1):
            if a % i == 0:
                print(f"{a} is not a prime number")
                exit()
        print(f"{a} is a prime number")
        exit()
    print("End of program")