# given an array of numbers thats length is always more than 1 have two user play a game
# Each user will take the a number off the array from the store going back and forth
# If the there is a duplicate number then the user will continue to pull until ther are no more duplicates
# Return the player with the most pulled from the array

def arrThing(arr):
    turn = 'p1'
    p1 = []
    p2 = []

    for i in range(len(arr)):
        if turn == 'p1':
            p1.append(arr[i])
            if i == len(arr) - 1:
                break
            if arr[i] != arr[i + 1]:
                turn = 'p2'
        else:
            p2.append(arr[i])
            if i == len(arr) - 1:
                break
            if arr[i] != arr[i + 1]:
                turn = 'p1'

    if len(p1) > len(p2):
        return 'Player 1 Won'
    else:
        return 'player 2 Won'
        


print(arrThing([1,3,3,4,4,4,5]))
