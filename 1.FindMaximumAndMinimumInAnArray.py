# 1. Find Maximum & Minimum in an Array

def find_max_min(arr):
    max_val = min_val = arr[0]

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

arr = list(map(int, input("Enter the array elements separated by space: ").split()))

max_value, min_value = find_max_min(arr)
print("Max:", max_value)
print("Min:", min_value)
