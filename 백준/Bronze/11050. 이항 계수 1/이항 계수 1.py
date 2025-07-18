import sys

def factorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else :
        return n * factorial(n-1)


if __name__=="__main__":

    a,b = map(int, sys.stdin.readline().split())

    print(int(factorial(a) / (factorial(b)* factorial(a-b))))
