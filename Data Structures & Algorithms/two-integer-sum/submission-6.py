class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            count[i] = nums[i]
        for keys in count:
            second_pair_val = target - count.get(keys, 0)
            for j in count:
                if keys != j and count.get(j, 0) == second_pair_val:
                    return [keys, j]