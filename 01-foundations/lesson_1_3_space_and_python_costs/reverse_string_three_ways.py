"""Lesson 1.3 - Three ways to reverse a string.

All three take O(n) time. Strings are immutable, so any method that returns
a string needs O(n) space. The two-pointer idea works in O(1) extra space
beyond the list of characters it swaps inside.
"""


def reverse_slicing(s):
    """Python builds a reversed copy. Extra space O(n)."""
    return s[::-1]


def reverse_join(s):
    """Iterate backwards and join. Extra space O(n)."""
    return "".join(reversed(s))


def reverse_two_pointers(s):
    """Swap from both ends on a list of characters. O(1) beyond that list."""
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)


if __name__ == "__main__":
    tests = ["hello", "", "a", "ab", "racecar", "Python 3"]
    for s in tests:
        a = reverse_slicing(s)
        b = reverse_join(s)
        c = reverse_two_pointers(s)
        assert a == b == c == s[::-1]
        print(repr(s), "->", repr(a))
