"""
@project: Leet_Code

@author: gemoy

@file: integer_flip.py

Create on 2020/5/9 21:57

Contact author by e-mail: gemo-yk@outlook.com
"""
import random

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x > 0 else -1
        nums = []
        loss = x if x > 0 else -1*x
        while loss > 0:
            nums.append(loss%10)
            loss = loss//10
        ans = 0
        for i in nums:
            ans = 10 * ans + i
        ans = flag * ans if -1*2**31 < flag * ans < 2**31 -1 else 0
        return ans

# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         temp = abs(x)
#         y = 0
#         i = len(str(temp))
#
#         while i > 0:
#
#             y = y * 10 + temp % 10
#             temp //= 10
#
#             i -= 1
#
#         if x < 0:
#             y = -y
#
#         if y < -(2 ** 31) or y > (2 ** 31 - 1):
#             return 0
#
#         return y




if __name__ == "__main__":
    solution = Solution()
    ans = solution.reverse(12345670)
    print(ans)
