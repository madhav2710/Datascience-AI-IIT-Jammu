def pattern(n):
    c=1
    for i in range(n):
        for j in range(i+1):
            print(c, end=' ')
            c += 1
        print()

n = int(input("Enter a number: "))
pattern(n)