# import sys
# from itertools import permutations

# def generate_palindromes(s: str):
#     permute = list(permutations(list(s), len(s)))
#     result = []
#     for name in permute:
#         name = ''.join(name)
#         if name == name[::-1]:
#             result.append(name)

#     if len(result) == 0:
#         return "I'm Sorry Hansoo"
    
#     result.sort()
#     return result[0]

# # 예제 사용
# hansoo_name = sys.stdin.readline().strip()
# result = generate_palindromes(hansoo_name)
# print(result)

# 팰린드롬은 좌우가 같아야 한다 -> 각 알파벳 개수가 홀수인 알파벳이 2개 이상이면 안됨!
# 사전순 정렬 필요
# 앞쪽(개수의 반) + 홀수 알파벳 + 뒤쪽(개수의 반)
import sys
from collections import Counter

hansoo_name = sys.stdin.readline().strip()
name_type = Counter(hansoo_name)
odd_count = 0
middle_alpha = ''
result = ''

for alpha, count in name_type.items():
    if count % 2 == 1:
        odd_count += 1
        middle_alpha = alpha
        if odd_count > 1:
            print("I'm Sorry Hansoo")
            exit(0)

for alpha, count in sorted(name_type.items()):
    result += (alpha * (count//2))
print(result + middle_alpha + result[::-1])
