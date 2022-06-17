import numpy as np
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = np.array(nums)
        for i in range(original.shape[0]):
            goal= target - original[i]
            if goal in original[i+1:]:
                return [i,np.argwhere(original==goal)[-1][0]]
        return 0
