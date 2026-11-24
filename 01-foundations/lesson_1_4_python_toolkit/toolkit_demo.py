"""Lesson 1.4 - one short demo of each tool in the Python toolkit."""

import heapq
from bisect import bisect_left
from collections import Counter, defaultdict, deque

# 1. Counter: how many times does each item appear?
count = Counter("banana")
print("Counter          :", dict(count))              # {'b': 1, 'a': 3, 'n': 2}
print("most_common(1)   :", count.most_common(1))    # [('a', 3)]

# 2. defaultdict: grouping without checking if the key exists
groups = defaultdict(list)
for word in ["cat", "dog", "bird", "fish", "ox"]:
    groups[len(word)].append(word)
print("defaultdict      :", dict(groups))

# 3. deque: O(1) at both ends
q = deque([1, 2, 3])
q.append(4)
first = q.popleft()
print("deque            :", first, list(q))

# 4. heapq: a min heap, push and pop are O(log n)
h = []
for x in [5, 1, 8, 3]:
    heapq.heappush(h, x)
print("heap pops        :", [heapq.heappop(h) for _ in range(len(h))])

# 5. bisect: binary search on a sorted list, O(log n)
print("bisect_left      :", bisect_left([1, 3, 5, 7], 5))      # 2

# 6. sorted with key: sort by any rule you define
students = [("Asha", 82), ("Ravi", 90), ("Meena", 75)]
print("sorted by marks  :", sorted(students, key=lambda s: s[1], reverse=True))

# Small features that save time
for index, value in enumerate(["a", "b", "c"]):
    print("enumerate        :", index, value)
for x, y in zip([1, 2, 3], ["one", "two", "three"]):
    print("zip              :", x, y)
a, b = 1, 2
a, b = b, a
print("swap             :", a, b)
smallest = float("inf")
for x in [7, 3, 9]:
    smallest = min(smallest, x)
print("float('inf') min :", smallest)
point = (4, 5)
px, py = point
print("tuple unpacking  :", px, py)
