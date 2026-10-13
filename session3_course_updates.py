# Create the original course list in a non-alphabetical order.
courses = [
    "Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I"
]

# Create an alphabetical copy without changing the original list.
sorted_courses = sorted(courses)

# Announce the available courses.
print(
    "The following courses are available for expression of interest "
    "if the students meet the prerequisites:"
)

# Print each course on a separate line.
for course in sorted_courses:
    print(course)
    
    # Save the name of the course being withdrawn.
withdrawn_course = courses[4]

# Replace Physics I with Chemistry I.
courses[4] = "Chemistry I"

# Confirm the withdrawn and replacement courses.
print(f"\n{withdrawn_course} has been withdrawn.")
print(f"{courses[4]} has been added as its replacement.")

# Display the updated courses alphabetically.
print("\nUpdated available courses:")
for course in sorted(courses):
    print(course)
    
    # Add Biology I at the beginning.
courses.insert(0, "Biology I")

# Add Microeconomics in the middle.
middle_position = len(courses) // 2
courses.insert(middle_position, "Microeconomics")

# Add Psychology I at the end.
courses.append("Psychology I")

# Display the list in its current order to show the positions.
print("\nThree new courses have been added.")
print("Available courses:")
for course in courses:
    print(course)
    
    # Announce why four courses are being withdrawn.
print("\nFour courses are unavailable due to technical and room availability issues.")

# Remove four courses, one at a time.
for count in range(4):
    withdrawn_course = courses.pop()
    print(f"{withdrawn_course} has been withdrawn and is no longer available.")

# Display the remaining available courses.
print("\nRemaining available courses:")
for course in sorted(courses):
    print(course)
    
    # Create a list of tuples containing course IDs and names.
course_tuples = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I")
]

# Create an empty list to store course IDs and names.
course_information = []

# Extract the ID and name from each tuple.
for course_id, course_name in course_tuples:
    course_information.append([course_id, course_name])

# Print the course information from the new list.
print("Course information:")
for course_id, course_name in course_information:
    print(f"Course ID: {course_id} | Course Name: {course_name}")