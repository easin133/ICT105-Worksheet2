# Create a list of courses in their original table order.
courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I"
]

# Print the original list.
print(courses)

# Print the courses alphabetically without changing the original list.
print("\nAlphabetical order:")
print(sorted(courses))

# Print the courses in reverse alphabetical order.
print("\nReverse alphabetical order:")
print(sorted(courses, reverse=True))

# Show that the original list is unchanged.
print("\nOriginal list unchanged:")
print(courses)
# Print the courses alphabetically without changing the original list.
print("\nAlphabetical order:")
print(sorted(courses))

# Print the courses in reverse alphabetical order.
print("\nReverse alphabetical order:")
print(sorted(courses, reverse=True))

# Show that the original list is unchanged.
print("\nOriginal list unchanged:")
print(courses)

# Reverse the current list order.
courses.reverse()
print("\nReversed list:")
print(courses)

# Reverse again to restore the original order.
courses.reverse()
print("\nOriginal order restored:")
print(courses)

# Change the list to alphabetical order.
courses.sort()
print("\nList after sort():")
print(courses)

# Change the list to reverse alphabetical order.
courses.sort(reverse=True)
print("\nList after sort(reverse=True):")
print(courses)