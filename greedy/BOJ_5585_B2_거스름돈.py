import sys

money= int(sys.stdin.readline())
money_list = [500, 100, 50, 10, 5, 1]
restmoney = 1000-money
result = 0

for ml in money_list:
    result += restmoney//ml
    restmoney = restmoney%ml

print(result)