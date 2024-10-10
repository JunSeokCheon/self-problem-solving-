import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == 0:
        break
    length_list = [a,b,c]
    max_length = max(length_list)
    length_list.remove(max_length)
    
    if a==b==c:
        print('Equilateral')
    elif sum(length_list) <= max_length:
        print('Invalid')
    elif a==b or a==c or b==c:
        print('Isosceles')
    elif a!=b and a!=c and b!=c:
        print('Scalene')