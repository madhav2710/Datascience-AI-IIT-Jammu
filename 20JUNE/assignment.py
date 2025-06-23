#1) Write a code that takes any two inputs from the user.
# If both inputs are:
# • Digits: Multiply them and check if the result is divisible by both inputs.
# • Strings: Concatenate them, and check if the first letter of both inputs is the same.
# • One digit and one string: Repeat the string digit-number of times.
# Example:
# Input1 = "4", Input2 = "Hi" → Output: "HiHiHiHi"

a = input()
b = input()
s = ""

a_num = True
for i in a:
    if i<'0' or i>'9':
        a_num = False
b_num = True
for i in b:
    if i<'0' or i>'9':
        b_num = False

if a_num and b_num:
    d = int(a) * int(b)
    if d % int(a)==0 and d % int(b)==0:
        print(f"{d} is divisible by both {int(a)} and {int(b)}")
    else:
        print(f"{d} is not divisible by both {int(a)} and {int(b)}")
elif a_num:
    n = int(a)
    while n > 0:
        s = s + b
        n-=1
    print(s)
elif b_num:
    n = int(b)
    while n > 0:
        s = s + a
        n-=1
    print(s)
else:
    s = a + b
    if a[0] == b[0]:
        print(f"First element of {a} and {b} is same")
    else:
        print(f"First element of {a} and {b} is not same")


###############################################################################

#2) String functions and their manual implementations
print("1>>   capitalize()")
print("_______________________")
a = "hello world!"
print(f"{a.capitalize()}  --> using function")
print("_______________________")
b = chr(ord(a[0])-32) + a[1:]
print(b)
print("_________------_________")
print("---------______---------")
print()



print("2>>   count()")
print("_______________________")
print(f"{a.count("l")}  --> using function")
print("_______________________")
c = 0
for ch in a:
    if ch == "l":
        c+=1
print(c)
print("_________------_________")
print("---------______---------")
print()



print("3>>   isdigit()")
print("_______________________")
d = "34"
print(f"{d.isdigit()}  --> using function")
print("_______________________")
d_num = True
for i in d:
    if i<'0' or i>'9':
        d_num = False
print(d_num)
print("_________------_________")
print("---------______---------")
print()



print("4>>   isalpha()")
print("_______________________")
print(f"{a.isalpha()}  --> using function")
print("_______________________")
a_alpha = True
for ch in a:
    if (ord(ch) < 65 or (ord(ch) > 90 and ord(ch) < 97) or ord(ch) > 122):
        a_alpha = False
print(a_alpha)
print("_________------_________")
print("---------______---------")
print()



print("5>>   isalnum()")
print("_______________________")
f = "hi4hello"
print(f"{f.isalnum()}  --> using function")
print("_______________________")
f_aldigit = True
for i in f:
    if (i<'0' or i>'9') and (ord(i) < 65 or (ord(i) > 90 and ord(i) < 97) or ord(i) > 122):
        f_aldigit = False
print(f_aldigit)
print("_________------_________")
print("---------______---------")
print()



print("6>>   islower()")
print("_______________________")
print(f"{a.islower()}  --> using function")
print("_______________________")
a_low = True
for ch in a:
    if ord(ch) >= 65 and ord(ch) <= 90:
        a_low = False
print(a_low)
print("_________------_________")
print("---------______---------")
print()



print("7>>   isupper()")
print("_______________________")
g = "HELLO WORLD!"
print(f"{g.isupper()}  --> using function")
print("_______________________")
g_up = True
for ch in g:
    if ord(ch) >= 97 and ord(ch) <= 122:
        g_up = False
print(g_up)
print("_________------_________")
print("---------______---------")
print()



print("8>>   find()")
print("_______________________")
index = a.find("llo")
print(f"'llo' is at {index}  --> using function")
print("_______________________")
cnt = 0
sub_a = "llo"
succ_find = False
for i in range(0,len(a)-len(sub_a)+1,1):
    k = i
    for j in range(0,len(sub_a)+1,1):
        if a[k] != sub_a[j]:
            cnt = 0
            break
        else:
            k += 1
            cnt += 1
            if cnt == len(sub_a):
                print(i)
                succ_find = True
                break
if succ_find == False:
    print("-1")
print("_________------_________")
print("---------______---------")
print()



print("9>>   lower()")
print("_______________________")
print(f"{g.lower()}  --> using function")
print("_______________________")
h = ""
for ch in g:
    if ord(ch) >= 65 and ord(ch) <= 90:
        h = h + chr(ord(ch) + 32)
    else:
        h = h + ch
print(h)
print("_________------_________")
print("---------______---------")
print()



print("10>>   upper()")
print("_______________________")
print(f"{a.upper()}  --> using function")
print("_______________________")
h = ""
for ch in a:
    if ord(ch) >= 97 and ord(ch) <= 122:
        h = h + chr(ord(ch) - 32)
    else:
        h = h + ch
print(h)
print("_________------_________")
print("---------______---------")
print()



print("11>>   replace()")
print("_______________________")
old = "world"
new = "vishv"
print(f"{a.replace(old,new)}  --> using function")
print("_______________________")
idx = a.find(old)
i =  a[:idx] + new + a[idx + len(old) : ]
print(i)
print("_________------_________")
print("---------______---------")
print()



print("12>>   startswith()")
print("_______________________")
substr = "hell"
print(f"{a.startswith(substr)}  --> using function")
print("_______________________")
strt_with = True
for i in range(len(substr)):
    if a[i] != substr[i]:
        strt_with = False
        break
print(strt_with)
print("_________------_________")
print("---------______---------")
print()



print("13>>   endswith()")
print("_______________________")
substr = "rld!"
print(f"{a.endswith(substr)}  --> using function")
print("_______________________")
ends_with = True
for i in range(len(substr)):
    if a[len(a)-len(substr)+i] != substr[i]:
        ends_with = False
        break
print(ends_with)
print("_________------_________")
print("---------______---------")
print()