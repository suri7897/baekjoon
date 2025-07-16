import sys

num = int(sys.stdin.readline())

size_num = list(map(int, sys.stdin.readline().split(' ')))
t, p = map(int, sys.stdin.readline().split())

size_num = [x // t if x % t == 0 else x // t + 1 for x in size_num]

print(sum(size_num))

print(num // p, num % p)