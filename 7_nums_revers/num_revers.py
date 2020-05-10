"""
@project: Leet_Code

@author: gemoy

@file: num_revers.py

Create on 2020/5/10 22:44

Contact author by e-mail: gemo-yk@outlook.com
"""


# class Solution(object):
#     def isPalindrome(self, x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         if x < 0:
#             return False
#         if x < 10:
#             return True
#         else:
#             nums = []
#             while x > 0:
#                 nums.append(x % 10)
#                 x = x // 10
#             for i in range(len(nums)):
#                 if nums[i] != nums[-1*i - 1]:
#                     return False
#                 if i * 2 >= len(nums):
#                     return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        revers = 0
        ori = x
        while x > 0:
            residule = x % 10
            x = x // 10
            revers = revers * 10 + residule
        if revers == ori:
            return True
        else:
            return False




if __name__ == '__main__':
    solution = Solution()
    ans = solution.isPalindrome(-123456654321)
    print(ans)
