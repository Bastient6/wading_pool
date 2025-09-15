import task31

tab_decal = [i for i in range (0, 26)]

def to_upper(string):
    new = ""
    for index in range (0, len(string)):
        if (string[index] >= 'a' and string[index] <= 'z'):
            new += chr(ord(string[index]) - 32)
        else :
            new += string[index]
    return new

def clean_str(string):
    new_str = ""
    for i in range (len(string)):
        if string[i] >= "A" and string[i] <= "Z":
            new_str += string[i]
    return new_str

def vigenere_message_and_key():
    new_string = ""
    decal = ""
    print("écris un message et un clé de dé.cryptage entre 1 et 25")
    string = input()
    i = len(string) - 1
    while string[i - 1] != " ":
        i -= 1
    for j in range(i, len(string)):
        decal += string[j]
    for j in range(0, i - 1):
        new_string += string[j]
    return decal, new_string

def vigenere_encrypt():
    new_message = ""
    groupe = 0
    index = 0
    key, message = vigenere_message_and_key()
    message = to_upper(message)
    key = to_upper(key)
    message = clean_str(message)
    for i in range(len(message)):
        if groupe == 5:
            groupe = 0
            new_message += " "
        for j in range(len(task31.alphabet)):
            if task31.alphabet[j] == key[i % len(key)]:
                for e in range(len(task31.alphabet)):
                    if message[i] == task31.alphabet[e]:
                        if e + tab_decal[j] > 25:
                            index = e + tab_decal[j] - 26
                        else :
                            index = e + tab_decal[j]
                        new_message += task31.alphabet[index]
                        break
        groupe += 1
    print(new_message)

def vigenere_decrypt():
    new_message = ""
    index = 0
    key, message = vigenere_message_and_key()
    message = to_upper(message)
    key = to_upper(key)
    message = clean_str(message)
    for i in range(len(message)):
        for j in range(len(task31.alphabet)):
            if task31.alphabet[j] == key[i % len(key)]:
                for e in range(len(task31.alphabet)):
                    if message[i] == task31.alphabet[e]:
                        if e - tab_decal[j] > 25:
                            index = e - tab_decal[j] - 26
                        else :
                            index = e - tab_decal[j]
                        new_message += task31.alphabet[index]
                        break
    print(new_message)

# vigenere_decrypt()