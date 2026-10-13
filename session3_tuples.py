# Store course IDs and names as tuples.
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I")
]

# Create an empty list.
course_information = []

# Extract each ID and name and add them to the new list.
for course_id, course_name in course_tuples:
    course_information.append([course_id, course_name])

# Display the information from the new list.
print("Course information:")
for course_id, course_name in course_information:
    print(f"Course ID: {course_id} | Course Name: {course_name}")