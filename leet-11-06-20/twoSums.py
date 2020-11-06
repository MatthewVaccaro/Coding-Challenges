# def twoSum(nums, target):
#     for i in range(len(nums)):
#         if target - nums[i] in nums:
#             findIndex = nums.index(target - nums[i])
#             if findIndex != i:
#                 return [i,findIndex ]
        
#     # return findIndex


# print(twoSum([3, 3]
#              ,6))


# def myAtoi(s):
#     newNum = []
#     splitting = [char for char in s]
#     for el in splitting:
#         if el.isnumeric() == True or el == '-':
#             newNum.append(el)
#     backToString = "".join(newNum)
#     return int(backToString)


# print(type (myAtoi(
#     "   -42")))

def lengthOfLongestSubstring(s):
    window = 0
    queue = []
    max = 0

    if len(s) == 1:
        return 1


    while window < len(s):
        for i in range(window, len(s)):
            if s[i] not in queue:
                queue.append(s[i])
            else:
                if max < len(queue):
                    max = len(queue)
                queue = []
                break
        window += 1
    
    return max


print(lengthOfLongestSubstring("jbpnbwwd"))
   
