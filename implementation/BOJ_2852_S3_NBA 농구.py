import sys

n = int(sys.stdin.readline())
win_flag = 0
one_time = 0
two_time = 0

for _ in range(n):
    team, time = sys.stdin.readline().split()
    minute, second = map(int, time.split(":"))
    if team == '1':
        if win_flag == 0:
            one_time += 48*60 - (60*minute+second)
        win_flag += 1
        if win_flag == 0:
            if two_time > 0:
                two_time = two_time - (48*60 - (60*minute+second))
    else:
        if win_flag == 0:
            two_time += 48*60 - (60*minute+second)
        win_flag -= 1
        if win_flag == 0:
            if one_time > 0:
                one_time = one_time - (48*60 - (60*minute+second))

print('{:02}:{:02}'.format(one_time//60,one_time%60))
print('{:02}:{:02}'.format(two_time//60,two_time%60))