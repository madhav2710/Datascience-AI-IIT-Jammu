num =int(input("Enter a number: "))
num_digits = len(str(abs(num)))
if num>0&num<1000:
    if((num % 2 == 0)&(num_digits==2)):
        print("even double digit")
    elif((num % 3 == 0)&(num_digits==3)):
        print("odd triple digit")
    elif(num<9& num==2 or num==3 or num==5 or num==7 ):
        print("One digit prime") 
    else:
        print("number desont match")
else:
    print("number desont match")