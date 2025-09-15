print ('entrez un nombre')
number = input()
i = number.index('.') + 1
while (i < len(number)):
    print(number[i], end="")
    i += 1
print ("")