def min_max_search(arr):
    arr_len = len(arr)

    if arr_len == 0:
        return (None, None)
    
    if arr_len == 1:
        value = arr[0]
        return (value, value)
    
    if arr_len == 2:
        return (min(arr), max(arr))
    
    if arr_len > 2:
        mid = len(arr) // 2
        min_value1,max_value1 = min_max_search(arr[:mid])
        min_value2,max_value2 = min_max_search(arr[mid:])
        min_value = min(min_value1, min_value2)
        max_value = max(max_value1, max_value2)
        return (min_value, max_value)
    
def quick_select(arr, k):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    left_len = len(left)

    if left_len > k:
        return quick_select(left, k)    
    if left_len + 1 < k:
        return quick_select(right, k-left_len-1)
    if left_len == k:
        return max(left)
    if left_len + 1 == k:
        return middle[0]