# https: // www.codewars.com/kata/5899dc03bc95b1bf1b0000ad
# Given a set of numbers, return the additive inverse of each. Each positive becomes
# negatives, and the negatives become positives.
# invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
# invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(arr):
    results = []
    if len(arr) == 0:
        return results
    else:
        for num in arr:
            if num < 0:
                results.append(abs(num))
            else:
                results.append(-abs(num))

    return results


print(invert([1, -2, 3, -4, 5]))
