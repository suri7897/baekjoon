import sys

num_list = []
answer = []

while(True):
    num = sys.stdin.readline().strip()
    if num == '0 0 0':
        break
    num_list.append(num)

for num in num_list:
    case = list(map(int, num.split()))
    case.sort()
    is_pen = 'right'
    if (case[2] ** 2 != case[1] ** 2 + case[0] ** 2):
        is_pen = 'wrong'
    answer.append(is_pen)

[print(is_pen) for is_pen in answer]