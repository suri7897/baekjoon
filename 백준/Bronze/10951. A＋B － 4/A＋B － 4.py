import sys

num_list = sys.stdin.read().strip().split('\n')

for i in range(len(num_list)):
    a,b = num_list[i].split()
    print(int(a)+int(b))