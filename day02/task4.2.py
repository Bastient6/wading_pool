import math

def fonct (py, n):
    if (float("{:.6f}".format(py)) + 3 == float("{:.6f}".format(math.pi))):
        return print (float("{:.6f}".format(py)))
    n += 2
    i = n
    while (i != 0):
        py = ((2 * i - 1) ** 2 /  (6 + py))
        i -= 1
    fonct(py, n)
fonct(1, 1)