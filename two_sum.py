class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)): #have index of first num
            search = target - nums[i] 
            if search in nums[i+1:]: #means there's two nums inside that add up to 
                return [i, nums.index(search, i+1)] #need to search beyond i so don't use duplicate elems
        #beats 1/3 of solns, 100% accuracy