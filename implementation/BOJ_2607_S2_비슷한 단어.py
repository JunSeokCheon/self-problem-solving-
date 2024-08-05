import sys, copy

n = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for _ in range(n)]
result = 0
target_word = word_list[0]
words = word_list[1:]

for word in words:
    temp_target_word = copy.deepcopy(target_word)
    change_cnt = 0
    
    for mini_w in word:
        if mini_w in temp_target_word:
            temp_target_word = temp_target_word.replace(mini_w, '', 1)
        else:
            change_cnt += 1
            
    if change_cnt < 2 and len(temp_target_word) < 2:
        result += 1

print(result)