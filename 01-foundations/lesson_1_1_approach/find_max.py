"""Lesson 1.1 - Example A: find the maximum in a list."""


def find_max_brute_force(nums):
    """Compare every element with every other element.

    Time O(n^2), space O(1).
    """
    if not nums:
        raise ValueError("list is empty")
    for i in range(len(nums)):
        is_biggest = True
        for j in range(len(nums)):
            if nums[j] > nums[i]:
                is_biggest = False
                break
        if is_biggest:
            return nums[i]


def find_max(nums):
    """Keep a running maximum and scan once.

    Time O(n), space O(1).
    """
    if not nums:
        raise ValueError("list is empty")
    best = nums[0]
    for x in nums:
        if x > best:
            best = x
    return best


if __name__ == "__main__":
    tests = [
        [3, 9, 2],          # normal
        [-5, -1, -8],       # all negative
        [7],                # single element
        [4, 4, 4],          # all equal
        [1, 2, 3, 4, 5],    # already sorted
        [5, 4, 3, 2, 1],    # reverse sorted
    ]
    for nums in tests:
        assert find_max(nums) == find_max_brute_force(nums) == max(nums)
        print(nums, "->", find_max(nums))

    try:
        find_max([])
    except ValueError as err:
        print("[] ->", err)
