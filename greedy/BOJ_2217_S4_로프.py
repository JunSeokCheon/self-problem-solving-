import sys

rope_count = int(sys.stdin.readline())
rope_list = [int(sys.stdin.readline()) for _ in range(rope_count)]
rope_list.sort(reverse=True)

result = []
for i in range(1, rope_count+1):
    result.append(i*rope_list[i-1])
print(result)