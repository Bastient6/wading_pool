res = 0
print ('entrez une suite de chiffre')
number = int(input())
while (number > 0):
    res += number % 10
    number = number // 10
print (res)