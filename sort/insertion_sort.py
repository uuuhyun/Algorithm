def insertion_sort(A):
    A = [None] + A
    for i in range(2, len(A)):
        key = A[i]
        j = i-1
        while j>0 and A[j] > key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key
    return A[1:]

array = [2,5,3,1,2,6]
sorted_arr = insertion_sort(array)
print(sorted_arr)