import sys

A, P = map(int, sys.stdin.readline().split())
D = [A]

while True:
    temp_value = 0

    for char_num in str(D[-1]):
        temp_value += int(char_num) ** P
    
    if temp_value in D:
        break

    D.append(temp_value)

print(len(D[:D.index(temp_value)]))