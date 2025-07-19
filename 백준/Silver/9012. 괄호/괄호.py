import sys

def is_vps(ps):
    stack = []
    for c in ps:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

if __name__ == "__main__" :
    answer = []
    num = int(sys.stdin.readline().strip())
    for i in range(num):
        ps = sys.stdin.readline()
        answer.append(is_vps(ps))

    [print(ans) for ans in answer]