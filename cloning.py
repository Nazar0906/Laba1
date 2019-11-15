a = str(input('Enter the word: '))
b = ""
for c in a:
    c *= 2
    b += str(c)
print(b)