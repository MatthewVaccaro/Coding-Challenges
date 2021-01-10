def sort_array(arr):
    odd = [ num for num in arr if num % 2 != 0]
    odd.sort()
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            arr[i] = odd[0]
            odd.pop(0)

    return arr
      
print(sort_array([5, 3, 2, 8, 1, 4]))

