alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
def message_and_key():
    new_string = ""
    integer = 0
    print("écris un message et un clé de cryptage entre 1 et 25")
    string = input()
    i = len(string) - 1
    while string[i - 1] != " ":
        i -= 1
    for j in range(i, len(string)):
        integer = integer * 10
        integer += int(string[j])
    for j in range(0, i - 1):
        new_string += string[j]
    return integer, new_string

def caesar_cipher():
    new_message = ""
    index = 0
    key, message = message_and_key()
    for i in range(len(message)):
        if message[i] < "A" or message[i] > "Z":
            new_message += message[i]
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                if j + key > 25:
                    index = j + key - 26
                else :
                    index = j + key
                new_message += alphabet[index]
    print(new_message)
