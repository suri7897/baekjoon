import sys

queue = []
answer = []

num_operation = int(sys.stdin.readline())

for i in range(num_operation):
    operation = sys.stdin.readline().strip()
    if "push" in operation:
        x = operation.split()[1]
        queue.append(x)
    elif "pop" in operation:
        if not queue :
            answer.append(-1)
        else :
            answer.append(queue[0])
            queue.remove(queue[0])
    elif "front" in operation:
        if not queue :
            answer.append(-1)
        else :
            answer.append(queue[0])
    elif "back" in operation:
        if not queue :
            answer.append(-1)
        else :
            answer.append(queue[-1])
    elif "size" in operation:
        answer.append(len(queue))
    else:
        if not queue:
            answer.append(1)
        else:
            answer.append(0)

[print(ans) for ans in answer]