import sys

num = int(sys.stdin.readline().strip())

num_two = 0
num_five = 0

i = 1
while(i <= num):
    num_two += num // (2 ** i)
    num_five += num // (5 ** i)
    i += 1

print(min(num_two, num_five))