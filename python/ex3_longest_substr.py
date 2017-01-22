"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start_pos = 0
        end_pos = 1
        maxlen_substr = 0
        while(end_pos <= len(s)):
            substr = s[start_pos:end_pos]
            curlen_substr = len(substr)
            if curlen_substr == len(set(substr)):
                maxlen_substr = max(curlen_substr, maxlen_substr)
            else:
                start_pos += 1
            end_pos += 1

        return maxlen_substr

# a naive implementation
# this may seem to have the time complexity of O(n), but it's kind of cheating
# when using the built-in `set()` function for string
