def max_number(n):
    result = []
    numArr = [int(num) for num in str(n)]
    print(numArr)
    for i in range(len(numArr)):
        result.append(str(max(numArr)))
        numArr.remove(max(numArr))


    return int("".join(result))

print(max_number(7389))
