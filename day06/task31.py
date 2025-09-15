def funA(s, n):
    if len(s) - n >= 0:
        return True
    return False

def funB(s, n):
    somme = 0
    for i in range (0, len(s)):
        if s[i] < "a" or s[i] > "z" or s[i] < "A" or s[i] > "Z" or s[i] < "0" or s[i] > "9":
            somme += 1
        if somme - n >= 0:
            return True
    return False

def funC(s, n):
    somme = 0
    for i in range (0, len(s)):
        if s[i] >= "0" and s[i] <= "9":
            somme += 1
    if somme - n >= 0:
            return True
    return False

print(funC("coucou...11", 2))