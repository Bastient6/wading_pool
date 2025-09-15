import task33
import task31

tab_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tab_index = [0 for x in range (26)]

def message_and_key_vigenere():
    new_string = ""
    integer = 0
    print("écris un message crypté et la taille de la clé")
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

def count_letter(string):
    for index in range (0, len(string)):
        for i in range (0, len(tab_letter)):
            if string[index] == tab_letter[i]:
                tab_index[i] += 1
    return tab_index

def index_to_letter(tab):
    max = 0
    index_max = 0
    new_tab_letter = [""]
    index_new_tab = 0
    for i in range (0, len(tab_letter)):
        for j in range (0, len(tab_letter)):
            if float(tab_index[j]) != 0 and float(tab_index[j]) > float(max):
                max = tab_index[j]
                index_max = j
        if new_tab_letter[index_new_tab - 1] != tab_letter[index_max]:
            new_tab_letter[index_new_tab] = tab_letter[index_max]
            index_new_tab += 1
            new_tab_letter += tab_letter[j]
            tab_index[index_max] = -1
            max = 0
    new_tab_letter.pop()
    return(new_tab_letter)
        
def vigenere_decrypt_without_key(key, message):
    new_message = ""
    index = 0
    message = task33.to_upper(message)
    key = task33.to_upper(key)
    message = task33.clean_str(message)
    for i in range(len(message)):
        for j in range(len(task31.alphabet)):
            if task31.alphabet[j] == key[i % len(key)]:
                for e in range(len(task31.alphabet)):
                    if message[i] == task31.alphabet[e]:
                        if e - task33.tab_decal[j] > 25:
                            index = e - task33.tab_decal[j] - 26
                        else :
                            index = e - task33.tab_decal[j]
                        new_message += task31.alphabet[index]
                        break
    print(new_message)

def find_key(tab):
    key = ""
    for i in range(len(tab)):
        key += tab[i][0]
    return key

def decrypt_vigenere_without_key():
    key, message = message_and_key_vigenere()
    message = task33.clean_str(task33.to_upper(message))
    tab_message = [[] for i in range(key)]
    tab= [[] for i in range(key)] 
    tab_bis= [[] for i in range(key)] 
    for i in range(key):
        for j in range(i, len(message), key):
            tab_message[i] += message[j]
    for i in range(key):
        tab[i] = count_letter(tab_message[i])
        tab[i] = index_to_letter(tab[i])
    for i in range(len(tab)):
        if chr(ord(tab[i][0]) - 4) < "A":
            tab[i][0] = chr(ord(tab[i][0]) - 4 + 26)
        else :
            tab[i][0] = chr(ord(tab[i][0]) - 4)
        print(tab[i])
    key = find_key(tab)
    vigenere_decrypt_without_key(key, message)

decrypt_vigenere_without_key()