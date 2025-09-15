access_granted = ["open sesame","access granted"]
access_fucking_granted = ["will you open, you goddamn !@&/°","access fucking granted"]
permission_denied = "permission denied"
tab = [access_granted, access_fucking_granted, permission_denied]

def comp_string(string, target):
    if string == target:
        return True
    return False

def ask_string():
    print("écris une phrase")
    return input()

def access():
    string = ask_string()
    for i in range (len(tab)):
        if comp_string(string, tab[i][0]):
            return print(tab[i][1])
    return print(tab[2])
    