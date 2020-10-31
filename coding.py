def mutateTheArray(n, a):

    arrayB = []
    a.append(0)
    a.insert(0, 0)

    for i in range(1, n+1):
        value = a[i-1]+ a[i] + a[i +1]
        arrayB.append(value)

    return arrayB

print(mutateTheArray(1, [9]))


def countTinyPairs(a, b, k):

    b.reverse()
    count = 0
    for i in range(len(a)):
        print(int(str(a[i]) + str(b[i])))
        if int(str(a[i]) + str(b[i])) < k:
           count += 1
    return count

print(countTinyPairs([], [], 1))

def mergeStrings(s1, s2):
    s1 = [ letter for letter in s1]
    s2 = [letter for letter in s2]
    newWord =[]

    s1Dup = 0
    s2Dup = 0

    for letter in s1:
        value = s1.count(letter)
        if value > s1Dup:
            s1Dup = value

    for letter in s2:
        value = s2.count(letter)
        if value > s2Dup:
            s2Dup = value
    
    print(s1Dup, s2Dup)

    if s1Dup < s2Dup:
        s1.extend(s2)
        return "".join(s1)
    if s1Dup > s2Dup:
        s2.extend(s1)
        return "".join(s2)

    if s2Dup == s1Dup:
        while len(s1) != 0 or len(s2)!= 0:
            if len(s1) == 0:
                newWord.extend(s2)
                s2 = []
                break
            if len(s2) == 0:
                newWord.extend(s1)
                s1 = []
                break

            if s1[0] <= s2[0]:
                newWord.append(s1[0])
                s1.pop(0)
            else:
                newWord.append(s2[0])
                s2.pop(0)

        return "".join(newWord)
            

print(mergeStrings("enbvszyppzyiydnc", "ousswsbeljamma"))

def concatenationsSum(a):
    sumArray = []
    for i in range(len(a)):
        for j in range(len(a)):
            sumArray.append(int(str(a[i]) + str(a[j])))

    return sum(sumArray)


print(concatenationsSum([1,2,3]))
