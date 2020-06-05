"""
@project: Leet_Code

@author: gemoy

@file: solution

Create on 2020/6/5 22:37

Contact author by e-mail: gemo-yk@outlook.com
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            elif nums[i - 1] <= 0:
                pass
            maxnum = max(maxnum, nums[i])
        return maxnum



if __name__ == '__main__':
    slution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = slution.maxSubArray(nums)
    print(res)
    print('=')