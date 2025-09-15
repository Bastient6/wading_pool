def power(number, powe):
    res = number
    for i in range (1, powe):
        res *= number
    print(res)

power(42, 168)