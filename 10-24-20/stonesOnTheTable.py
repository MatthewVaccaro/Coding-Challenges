# /https: // www.codewars.com/kata/5f70e4cce10f9e0001c8995a
# There are some stones on Bob's table in a row, and each of them can be red,
# green or blue, indicated by the characters R, G, and B.

# Help Bob find the minimum number of stones he needs to remove from the table
# so that the stones in each pair of adjacent stones have different colours.

def solution(stones):
    count = 0
    length = len(stones) - 1
    for n in range(length):
        if length > n:
            if stones[n] == stones[n + 1]:
                count += 1

    return count



print(solution("RGBRGBRGGB"))
