num = int(input("Enter a number: "))

if(num>=0&num<=100):
    if(num>=90):
        print("A+")
    elif(num>=80 and num<90):
        if(num%5==0):
            print("A with bonus")
        else:
            print("A")
    elif(num>=60 and num<80):
        if(num%2==0):
            print("B")
        else:
            print("C")
    else:
        print("Fail")