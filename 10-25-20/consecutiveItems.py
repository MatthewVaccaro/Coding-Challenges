# You are given a list of unique integers arr, and two integers a
# and b. Your task is to find out whether or not a and b appear
# consecutively in arr, and return a boolean value(True if a and b
# are consecutive, False otherwise). It is guaranteed that a and b
# are both present in arr.

# def consecutive(arr, a, b):
#     result = False
#     for n in range(len(arr) - 1):
#         if arr[n] == a:
#             if arr[n + 1] == b:
#                 result = True
#                 break
                
#         if arr[n] == b:
#             if arr[n + 1] == a:
#                 result = True
#                 break
#     return result


# print(consecutive([1, 3, 7, 5], 3, 7))

def consecutive(arr, a, b):
    A = arr.index(a)
    B = arr.index(b)
    if A - B == 1:
        return True
    else:
        return False


print(consecutive([1, 3, 7, 5], 3, 7))
