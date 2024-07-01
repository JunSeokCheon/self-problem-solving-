import sys

vowels = ['a', 'e', 'i', 'o', 'u'] 

def check_one(password):
    if 'a' in password or 'e' in password or 'i' in password or 'o' in password or 'u' in password:
        return True
    else:
        return False
    
def check_two(password):
    for i in range(len(password)-2):
        if (password[i] not in vowels) and (password[i+1] not in vowels) and (password[i+2] not in vowels):
            return False
        if (password[i] in vowels) and (password[i+1] in vowels) and (password[i+2] in vowels):
            return False
    return True

def check_three(password):
    for i in range(len(password)-1):
        if (password[i] == password[i+1]):
            if (password[i] == 'e' or password[i] == 'o'):
                continue
            else:
                return False
    return True

while True:
    password = sys.stdin.readline().strip()
    if password == "end":
        break

    check_1 = check_one(password)
    check_2 = check_two(password)
    check_3 = check_three(password)

    if check_1 and check_2 and check_3:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")