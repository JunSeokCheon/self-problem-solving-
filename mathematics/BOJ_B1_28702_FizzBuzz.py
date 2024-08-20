import sys

def judge(i):
    if i % 3 == 0 and i % 5 == 0:
        return "FizzBuzz"
    elif i % 3 == 0 and i % 5 != 0:
        return "Fizz"
    elif i % 3 != 0 and i % 5 == 0:
        return "Buzz"
    else:
        return i

for i in range(3, 0, -1):
    string = sys.stdin.readline().strip()
    if string not in ['FizzBuzz', 'Fizz', 'Buzz']:
        goal = int(string) + i

print(judge(goal))