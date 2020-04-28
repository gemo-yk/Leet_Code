"""
@project: Leet_Code

@author: gemoy

@file: two_nums_plus.py

Create on 2020/4/28 22:25

Contact author by e-mail: gemo-yk@outlook.com
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = 0
        for i in range(len(l1)):
            l1_num += l1[i] * 10 ** i
        l2_num = 0
        for i in range(len(l2)):
            l2_num += l2[i] * 10 ** i
        sum = str(l1_num + l2_num)[::-1]
        ans = []
        for i in range(len(sum)):
            ans.append(sum[i])
        return ans


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    solution = Solution()
    ans = solution.addTwoNumbers(l1, l2)
