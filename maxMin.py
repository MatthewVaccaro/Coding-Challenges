# def solve(arr):
#     arr.sort()
#     result = []

#     turn = True
#     for i in range(len(arr)):
#         if turn == True:
#             result.append(arr[-1])
#             arr.pop(-1)
#         else:
#             result.append(arr[0])
#             arr.pop(0)
#         turn = not turn

#     return result






# print(solve([52, 77, 72, 44, 74, 76, 40]))
# # [77,40,76,44,74,52,72


def meeting(s):
    newString = s.upper()
    newArray = newString.split(";")
    result = []
    for name in newArray:
        fullname = name.split(":")
        result.append("(" + fullname[1]+"," + " " + fullname[0] + ")")
    sortedResult = sorted(result)

    return " ".join(sortedResult)


    # sortedArr = sorted(newArray)


print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))

# "(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)")
