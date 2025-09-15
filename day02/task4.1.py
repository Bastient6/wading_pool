import math
py = 0
i = 1
while (float("{:.6f}".format(py * 4)) != float("{:.6f}".format(math.pi))):
    py += 1/i
    py -= 1/(i+2)
    print ("{:.6f}".format(py * 4))
    i += 4
print(i)