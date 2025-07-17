def find_gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a

import sys

if __name__ == '__main__':
    a,b = map(int, sys.stdin.readline().split())
    gcd = find_gcd(a,b)
    print(gcd)
    print(int(a*b/gcd))