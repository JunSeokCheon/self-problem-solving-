# 실패 : 2 \n AB \N AB -> 케이스 불만족
# import sys
# from collections import defaultdict

# n = int(sys.stdin.readline())
# n_list = []
# digit_dic = defaultdict(list)
# conversion_dic = defaultdict(str)
# init_value = 9
# result_list = []

# for _ in range(n):
#     n_list.append(sys.stdin.readline().strip())

# n_list = sorted(n_list, key= lambda x : -len(x))

# for word in n_list:
#     for char_idx in range(len(word), 0, -1):
#         digit_dic[char_idx] += word[len(word)-char_idx]

# for digit, values in digit_dic.items():
#     for value in values:
#         if value not in conversion_dic.keys():
#             conversion_dic[value] = str(init_value)
#             init_value -= 1

# for word in n_list:
#     result = ''
#     for char in word:
#         result += conversion_dic[char]
#     result_list.append(int(result))

# print(sum(result_list))

import sys

n = int(sys.stdin.readline())
result = 0
n_list = []
word_digit_dic = {}

for _ in range(n):
    n_list.append(sys.stdin.readline().strip())

for word in n_list:
    digit = len(word)-1
    for char in word:
        if char in word_digit_dic:
            word_digit_dic[char] += 10**digit
        else:
            word_digit_dic[char] = 10**digit
        digit -= 1

word_digit_dic = sorted(word_digit_dic.values(), reverse=True)

num = 9
for value in word_digit_dic:
    result += num * value
    num -= 1

print(result)