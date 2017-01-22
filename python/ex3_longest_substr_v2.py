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
        end_pos = 0
        maxlen_substr = 0
        substr_unique_set = set()
        substr = ''

        while(end_pos < len(s)):
            if s[end_pos] in substr_unique_set:
                i = substr.index(s[end_pos])
                substr_unique_set -= set(substr[0:i + 1])
                start_pos = start_pos + i + 1
            else:
                substr_unique_set.add(s[end_pos])

            end_pos += 1

            substr = s[start_pos:end_pos]
            substr_unique_set.add(substr[-1])  # add the last char

            maxlen_substr = max(end_pos - start_pos, maxlen_substr)

        return maxlen_substr


# a slightly improved implementation using the `set` feature of membership
# check, but still inefficient
