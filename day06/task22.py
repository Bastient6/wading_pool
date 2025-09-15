def clean_str(string):
    string = string.lower()
    new_string = ""
    for i in range(0, len(string)):
        if string[i] >= 'a' and string[i] <= 'z':
            new_string += string[i]
    return new_string

def palindrome(string, index):
    if index == len(string) // 2:
        print("True")
        return
    if string[index] == string[len(string) - index - 1]:
        palindrome(string, index + 1)
        return
    print("False")

palindrome(clean_str("A Snta Lived As a Devil at NASA"), 0)