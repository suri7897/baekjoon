import sys

num_list = []
answer = []

while(True):
    num = sys.stdin.readline().strip()
    if num == '0':
        break
    num_list.append(num)

for num in num_list:
    is_pen = 'yes'
    for i in range(len(num) // 2):
        if(num[i] != num[-(i+1)]):
            is_pen = 'no'
            break
    answer.append(is_pen)

[print(is_pen) for is_pen in answer]
    