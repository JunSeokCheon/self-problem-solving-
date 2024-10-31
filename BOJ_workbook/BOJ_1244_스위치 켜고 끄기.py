import sys

n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
std = int(sys.stdin.readline())
for _ in range(std):
    gender, switch_num = map(int, sys.stdin.readline().split())
    if gender == 1:
        for i in range(switch_num-1, len(switch), switch_num):
            switch[i] = abs(switch[i]-1)
    else:
        switch[switch_num-1] = abs(switch[switch_num-1]-1)
        
        for i in range(1, n//2):
            if switch_num-1-i < 0 or switch_num-1+i >= n:
                break
            
            if switch[switch_num-1-i] == switch[switch_num-1+i]:
                switch[switch_num-1-i] = abs(switch[switch_num-1-i]-1)
                switch[switch_num-1+i] = abs(switch[switch_num-1+i]-1)
            else:
                break
for swit in range(len(switch)//20+1):
    print(*switch[20*swit:20*(swit+1)])