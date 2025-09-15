import task31

def caesar_decrypt():
    new_message = ""
    index = 0
    key, message = task31.message_and_key()
    for i in range(len(message)):
        if message[i] < "A" or message[i] > "Z":
            new_message += message[i]
        for j in range(len(task31.alphabet)):
            if message[i] == task31.alphabet[j]:
                if j - key < 0:
                    index = j - key + 26
                else :
                    index = j - key
                new_message += task31.alphabet[index]
    print(new_message)    

caesar_decrypt()