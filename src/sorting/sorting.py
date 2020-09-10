# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    arrA_idx = 0
    arrB_idx = 0

    for i in range(elements):

        if arrA_idx >= len(arrA):
            merged_arr[i] = arrB[arrB_idx]
            arrB_idx += 1

        elif arrB_idx >= len(arrB):
            merged_arr[i] = arrA[arrA_idx]
            arrA_idx += 1

        elif arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[i] = arrA[arrA_idx]
            arrA_idx += 1

        else:
            merged_arr[i] = arrB[arrB_idx]
            arrB_idx += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    else:
        # find middle of the array
        middle = len(arr) // 2

        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
