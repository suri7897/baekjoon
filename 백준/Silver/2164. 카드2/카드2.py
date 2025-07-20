import sys

num = int(sys.stdin.readline().strip())

two_factor = 2

while (two_factor < num):
    two_factor *= 2

if (num == 1 or num == 2):
    print(num)
else:
    print((num - (two_factor // 2)) * 2)