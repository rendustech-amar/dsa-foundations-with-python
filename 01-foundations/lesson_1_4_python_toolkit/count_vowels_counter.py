"""Lesson 1.4 - Warm-up 1: count the vowels in a string using Counter."""

from collections import Counter

VOWELS = "aeiou"


def count_vowels(text):
    """Time O(n), space O(1) (at most 26 distinct letters)."""
    counts = Counter(text.lower())
    return sum(counts[v] for v in VOWELS)


def vowel_breakdown(text):
    """Return how many times each vowel appears."""
    counts = Counter(text.lower())
    return {v: counts[v] for v in VOWELS if counts[v] > 0}


if __name__ == "__main__":
    for text in ["banana", "Hello World", "rhythm", "", "AEIOU aeiou"]:
        print(repr(text), "->", count_vowels(text), vowel_breakdown(text))
