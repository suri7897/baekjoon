import sys

stack = []
answer = []

num_operation = int(sys.stdin.readline())

for i in range(num_operation):
    operation = sys.stdin.readline().strip()
    if "push" in operation:
        x = operation.split()[1]
        stack.append(x)
    elif "pop" in operation:
        if not stack :
            answer.append(-1)
        else :
            answer.append(stack[-1])
            stack.pop()
    elif "top" in operation:
        if not stack :
            answer.append(-1)
        else :
            answer.append(stack[-1])
    elif "size" in operation:
        answer.append(len(stack))
    else:
        if not stack:
            answer.append(1)
        else:
            answer.append(0)

[print(ans) for ans in answer]