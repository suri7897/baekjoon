import sys

num = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(num)]

num_list.sort()

for i in num_list:
    print(i)