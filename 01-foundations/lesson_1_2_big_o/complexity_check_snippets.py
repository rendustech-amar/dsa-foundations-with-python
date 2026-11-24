"""Lesson 1.2 - the 8 "find the complexity" snippets, runnable.

Each snippet returns the number of basic steps it performed, so you can
watch the growth yourself instead of only reading the answer.
"""


def snippet_1(n):                      # O(n)
    steps = 0
    for i in range(n):
        steps += 1
    return steps


def snippet_2(n):                      # O(n^2)
    steps = 0
    for i in range(n):
        for j in range(n):
            steps += 1
    return steps


def snippet_3(n):                      # O(n^2)  (0+1+...+(n-1) = n(n-1)/2)
    steps = 0
    for i in range(n):
        for j in range(i):
            steps += 1
    return steps


def snippet_4(n):                      # O(log n)  (i doubles each time)
    steps = 0
    i = 1
    while i < n:
        i *= 2
        steps += 1
    return steps


def snippet_5(n):                      # O(n)  (sequential loops add: n + n)
    steps = 0
    for i in range(n):
        steps += 1
    for j in range(n):
        steps += 1
    return steps


def snippet_6(n):                      # O(n)  (inner loop is fixed at 10)
    steps = 0
    for i in range(n):
        for j in range(10):
            steps += 1
    return steps


def snippet_7(n):                      # O(2^n)  (each call makes two calls)
    if n <= 1:
        return 1
    return snippet_7(n - 1) + snippet_7(n - 1)


def snippet_8(n):                      # O(n log n)  (outer n, inner log n)
    steps = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            steps += 1
    return steps


ANSWERS = {
    1: "O(n)",
    2: "O(n^2)",
    3: "O(n^2)",
    4: "O(log n)",
    5: "O(n)",
    6: "O(n)",
    7: "O(2^n)",
    8: "O(n log n)",
}

if __name__ == "__main__":
    sizes = [10, 100, 1000]
    print(f"{'snippet':<10}{'answer':<12}" + "".join(f"n={n:<10}" for n in sizes))
    for k, func in enumerate(
        [snippet_1, snippet_2, snippet_3, snippet_4,
         snippet_5, snippet_6, snippet_8], start=1
    ):
        number = k if k < 7 else 8
        row = "".join(f"{func(n):<12}" for n in sizes)
        print(f"{number:<10}{ANSWERS[number]:<12}{row}")

    print()
    print("Snippet 7 is exponential, so use small n only:")
    for n in (5, 10, 15, 20):
        print(f"  n={n:<3} -> {snippet_7(n)} leaf calls")
