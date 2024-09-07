#!/usr/bin/python3
def length_of_longest_substring(s: str) -> int:
    char_index: dict[str, int] = {}
    left = 0
    max_length: int = 0
    for right in range(len(s)):
        if s[right] in char_index:
            left = max(left, char_index[s[right]] + 1)
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    return max_length

# Example test cases


print(length_of_longest_substring("abcabcbb"))  # Output: 3 ("abc")
print(length_of_longest_substring("bbbbaba"))     # Output: 1 ("b")
print(length_of_longest_substring("pwwkew"))    # Output: 3 ("wke")
