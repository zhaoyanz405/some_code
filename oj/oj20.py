#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""
rule = {'(': ')', '{': '}', '[': ']'}

def thin(s):
    n = len(s)

    if n == 0:
        return True
    if n == 1:
        return False
    try:
        if n == 2:
            a = s[0]
            b = s[1]
            if b == rule[a]:
                return True
            else:
                return False
    except KeyError:
        return False

    
    close_list = []
    

    # import pdb
    # pdb.set_trace()

    for i in range(n-1):
        a = s[i]
        b = s[i+1]
        try:
            value = rule[a]
        except :
            value = None
        if value and b == value:
            close_list += [i, i+1]

    close_list = list(set(close_list)).sort()
    print(close_list)
    for index in close_list[::-1]:
        del s[index]
    
    return thin(s)



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            return thin(list(s))
        except:
            raise
            return False
        
        
if __name__ == "__main__":
    sol = Solution()

    data = "[({(())}[()])]"
    print(sol.isValid(data))
