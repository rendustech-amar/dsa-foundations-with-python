"""Lesson 1.4 - Warm-up 3: where should 40 be inserted in a sorted list?"""

from bisect import bisect_left


def insert_position(sorted_list, value):
    """Index where value belongs to keep the list sorted. Time O(log n)."""
    return bisect_left(sorted_list, value)


if __name__ == "__main__":
    data = [10, 20, 30, 50, 60]
    pos = insert_position(data, 40)
    print("40 goes at index", pos)          # 3

    data.insert(pos, 40)                    # insert itself is O(n), finding is O(log n)
    print("after insert:", data)            # [10, 20, 30, 40, 50, 60]

    # Edge cases
    print(insert_position([], 5))                 # 0
    print(insert_position([10, 20], 5))           # 0 (before everything)
    print(insert_position([10, 20], 99))          # 2 (after everything)
    print(insert_position([10, 20, 20, 30], 20))  # 1 (leftmost of equal values)
