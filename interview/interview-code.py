# -*- coding：utf-8 -*-

"""
将字符数组里的单词正序，位置反序
"""

Author = 'zhaoyan'
Email = 'zhaoyanz405@gmail.com'


def reverse(char_list):
    """
    将传入的字符数组反序

    char_list: list 输入的字符数组
    return: char_list  反序后的字符数组
    """
    if char_list is None:
        return None

    n = len(char_list)
    half = int(n/2)

    for i in range(half):
        char_list[i], char_list[n-i-1] = char_list[n-i-1], char_list[i]

    return char_list

def reverse_words(char_list):
    """
    将传入的字符数组单词位置反序，单词内顺序不变

    思路：将字符数组直接反序，然后将单词正序。

    char_list: list 输入的字符数组
    return： char_list 单词位置反序后的数组
    """
    if char_list is None:
        return None

    char_list = reverse(char_list)
    word_begin = 0
    for i in range(len(char_list) - 1):
        if char_list[i] == ' ':
            word_end = i
            char_list[word_begin: word_end] = reverse(char_list[word_begin: word_end])
            word_begin = i + 1

    return char_list

if __name__ == "__main__":
    data = 'I need a job!'
    print(reverse(list(data)))
    print(reverse_words(list(data)))

# output:
# ['!', 'b', 'o', 'j', ' ', 'a', ' ', 'd', 'e', 'e', 'n', ' ', 'I']
# ['j', 'o', 'b', '!', ' ', 'a', ' ', 'n', 'e', 'e', 'd', ' ', 'I']