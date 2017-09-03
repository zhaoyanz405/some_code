class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        cur = 0
        start = 0
        end = 1
        length = len(s)
        while end <= length:
            cur_str = s[start:end]
            cur = end - start
            if len(cur_str) > len(set(cur_str)):
                start = start + 1
                end = start + 1
            else:
                if cur > max:
                    max = cur
                end = end + 1

                    
        return max
