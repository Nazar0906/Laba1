alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzАБВГДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїклмнопрстухфцчшщьюяабвгдеєжзиіїклмнопрстухфцчшщьюя012345678901234567890"
a = input("Введіть текст: ")
key = 1
ins = " "
for letter in a:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        ins = ins + alphabet[newPosition]
    else:
        ins = ins + letter
print("Encrypted text: ", ins)
