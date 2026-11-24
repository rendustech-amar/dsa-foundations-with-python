"""Lesson 1.2 - Practice sheet: find the complexity of 8 more snippets.

Read each function, write your answer on paper, THEN scroll to ANSWERS.
a and b are the sizes of two different inputs; n is the size of one input.
"""


def practice_1(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count


def practice_2(n):
    count = 0
    for i in range(0, n, 2):
        count += 1
    return count


def practice_3(n):
    count = 0
    while n > 1:
        n //= 2
        count += 1
    return count


def practice_4(list_a, list_b):
    count = 0
    for x in list_a:
        count += 1
    for y in list_b:
        count += 1
    return count


def practice_5(list_a, list_b):
    count = 0
    for x in list_a:
        for y in list_b:
            count += 1
    return count


def practice_6(nums):
    seen = []
    for x in nums:
        if x in seen:          # hidden loop: "in" on a list
            return True
        seen.append(x)
    return False


def practice_7(nums):
    nums = sorted(nums)        # hidden cost of sorted()
    total = 0
    for x in nums:
        total += x
    return total


def practice_8(nums):
    return nums[0] + nums[-1]


ANSWERS = {
    1: ("O(n^3)", "Three nested loops, each n."),
    2: ("O(n)", "Step of 2 is still a constant factor: n/2 -> n."),
    3: ("O(log n)", "n is halved each time."),
    4: ("O(a + b)", "Sequential loops add; different inputs, different letters."),
    5: ("O(a * b)", "Nested loops multiply."),
    6: ("O(n^2)", "Loop of n, and 'x in seen' scans up to n items each time."),
    7: ("O(n log n)", "sorted() is n log n; the loop is only n, so sorting wins."),
    8: ("O(1)", "Two index lookups, no loop."),
}

if __name__ == "__main__":
    print("Sanity run (the functions do work):")
    print("practice_1(10)      =", practice_1(10))
    print("practice_2(10)      =", practice_2(10))
    print("practice_3(1000)    =", practice_3(1000))
    print("practice_4(3, 4 items) =", practice_4([1, 2, 3], [1, 2, 3, 4]))
    print("practice_5(3, 4 items) =", practice_5([1, 2, 3], [1, 2, 3, 4]))
    print("practice_6([1,2,3,1]) =", practice_6([1, 2, 3, 1]))
    print("practice_7([3,1,2]) =", practice_7([3, 1, 2]))
    print("practice_8([5,6,7]) =", practice_8([5, 6, 7]))
    print()
    print("Answers:")
    for k, (big_o, why) in ANSWERS.items():
        print(f"  {k}. {big_o:<11} {why}")
