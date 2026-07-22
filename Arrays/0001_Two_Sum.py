#LeetCode 1-Two Sum
#Difficulty: Easy
#Topic: Arrays,HashMap
#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for i in range (len(nums)):
            ans=target-nums[i]
            if ans in hashmap:
                return [hashmap[ans],i]
            hashmap[nums[i]]=i
            
