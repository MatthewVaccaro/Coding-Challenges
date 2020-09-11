# 8 KYU
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.
# You don't have to worry with strings with less than two characters.

def remove_char(s):
    letterList = [letter for letter in s]
    letterList.pop(0)
    letterList.pop(len(letterList)-1)

    return "".join(letterList)


# 7 KYU
# Complete the function to convert an integer into a string of the Turkish name.

# input will always be an integer 0-99
# output should always be lower case.

# Forming the Turkish names for the numbers 0-99 is very straightforward:

# units(0-9) and tens(10, 20, 30, etc.) each have their own unique name
# all other numbers are simply[tens] + [unit], like twenty one in English.
# Unlike English, Turkish does not have "teen"-suffixed numbers
# e.g. 13 would be directly translated as "ten three" rather than "thirteen" in English.

namesAndNumbers = {
    "on": 10,
    "yirmi": 20,
    "otuz": 30,
    "kırk": 40,
    "elli": 50,
    "altmış": 60,
    "yetmiş": 70,
    "seksen": 80,
    "doksan": 90,
    "sıfır": 0,
    "bir": 1,
    "iki": 2,
    "üç": 3,
    "dört": 4,
    "beş": 5,
    "altı": 6,
    "yedi": 7,
    "sekiz": 8,
    "dokuz": 9,

}


def get_turkish_number(num):
    turkishNumber = []
    number = str(num)
    if num < 10 or num % 10 == 0:
        for name in namesAndNumbers:
            if num == namesAndNumbers.get(name):
                turkishNumber.append(name)
    else:
        tens = num - int(number[1])
        print(tens)
        ones = num - tens

        for name in namesAndNumbers:
            if tens == namesAndNumbers.get(name) or ones == namesAndNumbers.get(name):
                turkishNumber.append(name)

    return " ".join(turkishNumber)


# KYU 7
# Given a string "abc" and assuming that each letter in the string has a value equal to its
# position in the alphabet, our string will have a value of 1 + 2 + 3 = 6. This means that:
# a = 1, b = 2, c = 3 ....z = 26.

# You will be given a list of strings and your task will be to return the values of the strings
# as explained above multiplied by the position of that string in the list. For our purpose
# position begins with 1.

# nameValue["abc", "abc abc"] should return [6, 24] because of[6 * 1, 12 * 2]. Note how spaces
# are ignored.

# "abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is
# multiplied by 1 while the value at position 2 is multiplied by 2.

alphabet = "abcdefghijklmnopqrstuvwxyz"
listAlphabet = [letter for letter in alphabet]


def name_value(my_list):

    points = 0
    pointList = []

    for i, el in enumerate(my_list):
        for letter in el:
            if letter is not " ":
                pointValue = listAlphabet.index(letter) + 1
                points += pointValue
        pointList.append(points * (i + 1))
        points = 0
    return pointList


# KYU 6
# Given n, take the sum of the digits of n. If that value has
# more than one digit, continue reducing in this way until a single-digit
# number is produced. This is only applicable to the natural numbers.

# Example:
#     16 - -> 1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

def digital_root(n):

    if n < 10:
        return n

    sum = 0

    numList = [int(num) for num in str(n)]
    for num in numList:
        sum = sum + num

    if sum > 9:
        return digital_root(sum)
    else:
        return sum
