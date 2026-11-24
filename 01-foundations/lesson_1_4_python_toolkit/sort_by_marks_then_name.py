"""Lesson 1.4 - Warm-up 4: sort (name, marks) pairs by marks descending,
then by name ascending when the marks are equal."""


def sort_by_marks_then_name(students):
    """Time O(n log n). The key is a tuple: (-marks, name)."""
    return sorted(students, key=lambda s: (-s[1], s[0]))


if __name__ == "__main__":
    students = [
        ("Ravi", 90),
        ("Asha", 82),
        ("Meena", 90),
        ("Kiran", 82),
        ("Zoya", 75),
    ]
    for name, marks in sort_by_marks_then_name(students):
        print(f"{name:<8}{marks}")
    # Meena and Ravi tie on 90 -> Meena first (name ascending)
    # Asha and Kiran tie on 82 -> Asha first
