def to_lowercase(string):
    new = ""
    for index in range (0, len(string)):
        if (string[index] >= 'A' and string[index] <= 'Z'):
            new += chr(ord(string[index]) + 32)
        else :
            new += string[index]
    return new
