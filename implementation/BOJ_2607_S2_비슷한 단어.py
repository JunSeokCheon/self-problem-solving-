import sys

n = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for _ in range(n)]
result = 0
target_word = list(word_list[0])
word_list = word_list[1:]

for word in word_list:
    temp_target_word = target_word[:]
    opt_cnt = 0
    
    for mini_word in word:
        if mini_word in ''.join(temp_target_word):
            temp_target_word.remove(mini_word)
        else:
            opt_cnt += 1
    
    if opt_cnt < 2 and len(temp_target_word) < 2:
        result += 1
print(result)