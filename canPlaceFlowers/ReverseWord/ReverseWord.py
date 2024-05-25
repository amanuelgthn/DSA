#!/usr/bin/env python3
"""Return a string of the words in reverse order concatenated by a single space."""


def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        return " ".join(words[::-1])