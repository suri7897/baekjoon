import sys

def Bsearch(num_list, target):
    low = 0
    high = len(num_list) - 1
    
    while (low <= high):
        mid = (low + high) // 2

        if (num_list[mid] == target):
            print(1)
            return
        elif (num_list[mid] > target):
            high = mid - 1
        else:
            low = mid + 1

    print(0)


if __name__ == "__main__":

    input_num = int(sys.stdin.readline())

    input_num_list = list(map(int, sys.stdin.readline().split()))

    input_num_list.sort()

    output_num = int(sys.stdin.readline())

    output_num_list = list(map(int, sys.stdin.readline().split()))

    for i in range(output_num):
        Bsearch(input_num_list, output_num_list[i])