# Implementing twoSum using hashmap
# Target is subtracted from current index and the result is searched for in the hashmap.
# If index and complement = target return current index and complement

nums1 = [5, 2, 7, 10, 3, 9]
target1 = 8

def twoSum(nums, target):
    dic = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in dic:
            return [i, dic[complement]]
          
        dic[num] = i

    return [-1, -1]
    
answer = twoSum(nums1, target1)
print(answer)