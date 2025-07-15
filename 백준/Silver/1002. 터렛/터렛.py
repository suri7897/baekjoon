import math

num_T = int(input())

def possible(x1,y1,x2,y2,r1,r2):
    dist = math.sqrt((x1-x2) ** 2 + (y1 - y2) ** 2)

    if dist == 0 and r1 == r2:
        return -1
    elif dist == abs(r1 - r2):
        return 1 
    elif dist == r1 + r2:
        return 1 
    elif abs(r1 - r2) < dist < r1 + r2:
        return 2 
    else:
        return 0
    
if __name__ == "__main__" :
    answer = []
    for i in range(num_T):
        x1, y1, r1, x2, y2, r2 = input().split(' ',6)
        answer.append(possible(int(x1),int(y1),int(x2),int(y2),int(r1),int(r2)))
    
    for i in range(num_T):
        print(answer[i])