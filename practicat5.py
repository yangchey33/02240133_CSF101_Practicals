
#Modify the linear search function to return all indices where the target appears, not just the first one

def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[1] == target:
            indices.append(i)
        return indices
    
test_list= [5, 2, 6, 9, 1, 3, 7, 6, 8, 1, 4]
print("All indices of 6:", linear_search(test_list,6))

#Implement a function that uses binary search to find the insertion point for a target value in a sorted list.

def binary_search_insertion_point(arr, target):
    left, right =0, len(arr)
    while right > left:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            return left 
        
sorted_list = [1, 3, 4, 5, 6]
print("insertion point for 3:", binary_search_insertion_point(sorted_list, 3))
print("insertion point for 4:", binary_search_insertion_point(sorted_list, 4))

#Create a function that counts the number of comparisons made in each search algorithm.

def linear_search_comparisons(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search_comparisons(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

arr = list(range(1000))
target = 888

lin_result, lin_comp = linear_search_comparisons(arr, target)
bin_result, bin_comp = binary_search_comparisons(arr, target)

print(f"Linear: index={lin_result}, comparisons={lin_comp}")
print(f"Binary: index={bin_result}, comparisons={bin_comp}")

#Implement a jump search algorithm and compare its performance with linear and binary search.
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0

    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    for i in range(prev, min(step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

    return -1, comparisons

# Compare performance
arr = list(range(10000))
target = 8888

_, lin_comp = linear_search_comparisons(arr, target)
_, bin_comp = binary_search_comparisons(arr, target)
_, jump_comp = jump_search(arr, target)

print(f"Comparisons:\nLinear: {lin_comp}\nBinary: {bin_comp}\nJump: {jump_comp}")