def bubble_sort(A):
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp
    return A

arr = [5,2,7,1,8]
sorted_arr = bubble_sort(arr)
print(sorted_arr)
