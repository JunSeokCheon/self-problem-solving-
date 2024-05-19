import sys

n = int(sys.stdin.readline())
distance_list = list(map(int, sys.stdin.readline().split()))
price_list = list(map(int, sys.stdin.readline().split()))
result = distance_list[0] * price_list[0]
price_list = price_list[:-1]
min_price = price_list[0]

for i in range(1, len(price_list)):
    if price_list[i] > min_price:
        result += (distance_list[i] * min_price)
    else:
        min_price = price_list[i]
        result += (distance_list[i] * price_list[i])

print(result)



