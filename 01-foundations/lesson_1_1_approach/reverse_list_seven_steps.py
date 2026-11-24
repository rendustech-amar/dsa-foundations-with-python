"""Lesson 1.1 - Practice: the 7 steps applied to "Reverse a List"."""

# Step 1 - Understand
#   Input : a list of any values.
#   Output: the same values in reverse order.
#   Ask   : reverse in place or return a new list? Can the list be empty? (yes)

# Step 2 - Examples
#   [1, 2, 3, 4] -> [4, 3, 2, 1]
#   []           -> []            (tricky: empty)
#   [7]          -> [7]           (tricky: single element)


# Step 3 - Brute force: build a new list by reading from the back.
def reverse_brute_force(nums):
    """Time O(n), extra space O(n)."""
    result = []
    for i in range(len(nums) - 1, -1, -1):
        result.append(nums[i])
    return result


# Step 4 - Optimise: the new list is wasted memory. Swap the two ends and
#          move inwards, so we reuse the input itself (O(1) extra space).

# Step 5 - Code
def reverse_in_place(nums):
    """Two pointers. Time O(n), extra space O(1)."""
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


# Step 6 - Test (dry run with the examples and edge cases)
if __name__ == "__main__":
    tests = [
        [1, 2, 3, 4],
        [],
        [7],
        [1, 2, 3],        # odd length: middle element stays
        [5, 5, 5],        # all equal
        [-3, 0, 4],       # negatives and zero
    ]
    for nums in tests:
        expected = nums[::-1]
        assert reverse_brute_force(nums) == expected
        assert reverse_in_place(list(nums)) == expected
        print(nums, "->", expected)

# Step 7 - Analyse
#   reverse_brute_force : time O(n), space O(n)
#   reverse_in_place    : time O(n), space O(1)
