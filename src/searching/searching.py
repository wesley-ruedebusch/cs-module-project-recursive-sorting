# TO-DO: Implement a recursive implementation of binary search
"""
# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low+high)//2
        if target < arr[middle]:
            high = middle-1 # eliminate RHS
        elif target > arr[middle]:
            low = middle+1 # eliminate LHS
        else:
            return middle
    return -1 #not found
"""

def binary_search(arr, target, start, end):
    # base case?
    # low <= high recurse
    if start <= end:
    # rules to move towards base case?
        middle = (start+end)//2
        if arr[middle] == target:
            return middle
        elif target < arr[middle]:
            end = middle-1 # eliminate RHS
            return binary_search(arr, target, start, end)

        # elif target > arr[middle]:
        else:
            start = middle+1 # eliminate LHS
            return binary_search(arr, target, start, end)

    else:
        # target not found
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
