# https: // www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python
# The vowel substrings in the word codewarriors are o, e, a, i, o. The longest of these has a
# length of 2. Given a lowercase string that has alphabetic characters only(both vowels and
# consonants) and no spaces, return the length of the longest vowel substring. Vowels are
# any of aeiou.

def solve(s):
    vols = ['a', 'e', 'i', 'o', 'u']
    currentCount = 0
    bestCount = 0
    for i in range(len(s)):
        if i + 1 < len(s):
            if s[i] in vols and s[i + 1] in vols:
                currentCount += 1
            else:
                if currentCount > bestCount:
                    bestCount = currentCount
                    currentCount = 0
                else:
                    currentCount = 0
            
    return bestCount + 1





print(solve('codewarriors'))
