import sys

def first_rule(word):
    cnt = 0
    for mini_word in word:
        if mini_word in vowel:
            cnt += 1
    if cnt == 0:
        return False
    else:
        return True

def second_rule(word):
    if len(word) <= 2:
        return True
    
    for i in range(len(word)-2):
        if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel:
            return False
        
        if word[i] not in vowel and word[i+1] not in vowel and word[i+2] not in vowel:
            return False
        
    return True

def third_rule(word):
    for i in range(len(word)-1):
        if (word[i] == word[i+1]) and (word[i] != 'e') and (word[i] != 'o'):
            return False
    return True
            
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    word = sys.stdin.readline().strip()
    if word == 'end':
        break
    
    if first_rule(word) and second_rule(word) and third_rule(word):
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')