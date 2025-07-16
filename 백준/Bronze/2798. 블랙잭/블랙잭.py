import sys

def find_sum(n, num_list, target):
    answer = -999999
    if n == 1:
        for num in num_list:
            if num <= target and num > answer:
                answer = num
    else :
        for i, num in enumerate(num_list):
            if num > target:
                continue 
            remaining = num_list[:i] + num_list[i+1:]
            sub_result = find_sum(n - 1, remaining, target - num)
            total = num + sub_result
            if total <= target and total > answer:
                answer = total
    
    return answer

def main():
    a,b = input().split()
    num_list = list(map(int, sys.stdin.readline().split()))
    
    print(find_sum(3, num_list, int(b)))
    

if __name__ == '__main__':
    main()