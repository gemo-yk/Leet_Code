"""
@project: Leet_Code

@author: gemoy

@file: the_squuare_root_of_X.py

Create on 2020/5/9 20:23

Contact author by e-mail: gemo-yk@outlook.com
"""


# class Solution(object):
#     """
#     # Violent solution
#     """
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         ans = pow(x, 0.5)
#         return int(ans)


class Solution(object):
    """
    dichotomy method my method
    """
    def mySqrt(self, x):
        """
        :param x:
        :return:
        """
        left_value = 0
        right_value = x // 2 + 1
        while left_value < right_value:
            attempt = (left_value + right_value + 1) >> 1
            if attempt ** 2 > x:
                right_value = attempt - 1
            else:
                left_value = attempt
        return left_value

# class Solution:
#     def mySqrt(self, x):
#         # 为了照顾到 0 把左边界设置为 0
#         left = 0
#         # 为了照顾到 1 把右边界设置为 x // 2 + 1
#         right = x // 2 + 1
#         while left < right:
#             # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
#             # mid = left + (right - left + 1) // 2
#             mid = (left + right + 1) >> 1
#             square = mid * mid
#
#             if square > x:
#                 right = mid - 1
#             else:
#                 left = mid
#         # 因为一定存在，因此无需后处理
#         return left







if __name__ == "__main__":
    solution = Solution()
    ans = solution.mySqrt(4)
    print(ans)
