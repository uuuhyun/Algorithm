def selection_sort(A):
    for i in range(len(A)-1,0,-1):
        k = largest(A[:i])
        temp = A[i]
        A[i] = A[k]
        A[k] = temp
    return A

def largest(A):
    k = 0
    for i in range(len(A)):
        if A[i] > A[k]:
            k = i
    return k

array = [5,7,8,2,4]
sorted_arr = selection_sort(array)
print(sorted_arr)