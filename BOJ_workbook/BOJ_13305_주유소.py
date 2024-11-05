import sys

N = int(sys.stdin.readline())
road_len = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))
result = 0

result += (oil_price[0]*road_len[0])
min_oil = oil_price[0]
oil_price = oil_price[:-1]

for i in range(1, len(oil_price)):
    if oil_price[i] >= min_oil:
        result += (road_len[i]*min_oil)
    else:
        min_oil = oil_price[i]
        result += (road_len[i]*min_oil)

print(result)