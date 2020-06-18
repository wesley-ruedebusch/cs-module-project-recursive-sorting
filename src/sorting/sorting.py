# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # this fcn sorts and merges
    #counters to track our iterations
    a = 0
    b = 0
  
    for k in range(0, elements):
        # starting at the beginning of `a` and `b`
        # compare the value of each first value
        # if a is out of range, push b and iterate
        if a >= len(arrA): # we're done with a, push b
            merged_arr[k] = arrB[b]
            b += 1
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a +=1
        # if a is smaller, put in array and iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a +=1
        # if b is smaller, put in array and iterate both
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # split arr
    # base condition 
    if len(arr) > 1:
        # find middle of arr
        middle = len(arr) // 2
        # left stuff goes left
        left = merge_sort(arr[:middle])
        # right stuff goes right
        right = merge_sort(arr[middle: ])
        # call merge for left and right
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
