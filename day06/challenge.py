import time
def power(number, powe):
    res = number
    for i in range (1, powe):
        res *= number
    print(res)

def func():
    start = time.time()
    power(42, 168)
    print(time.time() - start)

func()