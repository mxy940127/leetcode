# 实现 strStr() 函数。
#
#  给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
# 果不存在，则返回 -1 。
#
#  说明：
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。
#
#  示例 1：
# 输入：haystack = "hello", needle = "ll"
# 输出：2
#
#  示例 2：
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1

class Solution:
    """
        1.偏移表 模式串中字符在模式串中出现的最右位置到尾部的距离+1，未出现则为模式串字符长度+1
        2.循环遍历
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        lnd = len(needle)
        lnh = len(haystack)
        if lnd > lnh:
            return -1
        """计算偏移表"""
        def calOffset(srcStr: str) -> dict:
            return {v: len(srcStr) - k for k, v in enumerate(srcStr)}
        idx = 0
        dic = calOffset(needle)
        while idx + lnd <= lnh:
            if haystack[idx: idx + lnd] == needle:
                return idx
            elif idx + lnd == lnh:
                return -1
            else:
                nextc = haystack[idx + lnd]
                idx += dic.get(nextc, lnd + 1)
        return -1
