print("abcdef")
input1 = "2"
input2 = "4"


if input1.isdigit() and input2.isdigit():
    num1 = int(input1)
    num2 = int(input2)
    product = num1 * num2
    print("Multiplication Result:", product)
    
    
    if product % num1 == 0 and product % num2 == 0:
        print("The result is divisible by both inputs.")
    else:
        print("The result is NOT divisible by both inputs.")
else:
    print("One or both inputs are not digits.")



text1 = "hello"
text2 = "hi"

combined_text = text1 + text2
print("Joined Text:", combined_text)


if len(text1) > 0 and len(text2) > 0:
    if text1[0] == text2[0]:
        print("Both words start with the same letter.")
    else:
        print("The starting letters are different.")
else:
    print("One of the strings is empty.")



first = "5"
second = "fun"

if first.isdigit():
    times = int(first)
    word = second
else:
    times = int(second)
    word = first


result = word * times
print("Repeated Output:", result)

