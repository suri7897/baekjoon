import math

num_nationals = int(input())
num_list = input().split()

answer = 0

for i in range(num_nationals):
    is_prime = True
    num = int(num_list[i])
    if num == 1:
        continue
    for i in range(2, int(math.sqrt(num))+1):
        if(num % i == 0):
            is_prime = False
            continue
    if is_prime :
        answer += 1

print(answer)