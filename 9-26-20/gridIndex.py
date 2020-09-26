# https: // www.codewars.com/kata/5f5802bf4c2cc4001a6f859e/train/python
# You are given an n by n(square) grid of characters, for example:
# [['m', 'y', 'e'],
#  ['x', 'a', 'm'],
#  ['p', 'l', 'e']]
# You are also given a list of integers as input, for example:
# [1, 3, 5, 8]
# You have to find the characters in these indexes of the grid if you think of the indexes as:
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]
# Remember that the indexes start from one and not zero.
# Then you output a string like this:
# "meal"
# All inputs will be valid.


def grid_index(grid, indexes):
    newList = []
    word = []
    for indexA in range(len(grid)):
        for indexB in range(len(grid)):
            newList.append(grid[indexA][indexB])

    for num in indexes:
        word.append(newList[num - 1])

    return "".join(word)


print(grid_index([['h', 'e', 'l', 'l'], ['o', 'c', 'o', 'd'], [
    'e', 'w', 'a', 'r'], ['r', 'i', 'o', 'r']], [5, 7, 9, 3, 6, 6, 8, 8, 16, 13]))
