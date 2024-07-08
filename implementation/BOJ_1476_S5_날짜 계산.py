import sys

e, s, m = map(int, sys.stdin.readline().split())
compare_e, compare_s, compare_m = 1, 1, 1
result = 1

while True:
    if e == compare_e and s == compare_s and m == compare_m:
        print(result)
        exit(0)
    compare_e += 1
    compare_s += 1
    compare_m += 1
    
    if compare_e >= 16:
        compare_e = 1
    if compare_s >= 29:
        compare_s = 1
    if compare_m >= 20:
        compare_m = 1
    result += 1