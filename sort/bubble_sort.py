import time
import random

# 10,000개 랜덤 정수 배열 생성
arr = [random.randint(1, 10000) for _ in range(10000)]

def bubble_sort(A):
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

# arr = [5,2,7,1,8]
start = time.time()
sorted_arr = bubble_sort(arr)
print(sorted_arr)
end = time.time()
print(f"기본 버블 정렬 시간: {end - start:.6f}초")


def bubble_sort_early_exit(A):
    for i in range(len(A)-1,0,-1):
        sort = True
        for j in range(i):
            if A[j] > A[j+1]:
                sort = False
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
        if sort == True: return A
    return A

start = time.time()
sorted_arr = bubble_sort_early_exit(arr)
print(sorted_arr)
end = time.time()
print(f"개선된 버블 정렬 시간: {end - start:.6f}초")