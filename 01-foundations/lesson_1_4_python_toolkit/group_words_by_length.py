"""Lesson 1.4 - Warm-up 2: group a list of words by length using defaultdict."""

from collections import defaultdict


def group_by_length(words):
    """Time O(n), space O(n). Returns {length: [words...]}."""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


if __name__ == "__main__":
    words = ["cat", "dog", "bird", "fish", "ox", "tiger", "bee"]
    print(group_by_length(words))
    # {3: ['cat', 'dog', 'bee'], 4: ['bird', 'fish'], 2: ['ox'], 5: ['tiger']}
    print(group_by_length([]))
