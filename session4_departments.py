# Store each course ID and its department in a list.
departments = [
    [1, "Computer Science"],
    [2, "Mathematics"],
    [3, "Computer Science"],
    [4, "Mathematics"],
    [5, "Physics"],
    [6, "Chemistry"],
    [7, "Biology"],
    [8, "Economics"],
    [9, "Economics"],
    [10, "Psychology"],
    [11, "History"],
    [12, "English"],
    [13, "Philosophy"],
    [14, "Mathematics"],
    [15, "Computer Science"]
]

# Display the records to check the list.
print("Course IDs and departments:")
for course_id, department in departments:
    print(f"{course_id}: {department}")
    
    # Keep asking for a course ID until the user exits.
while True:
    user_input = input("\nEnter a course ID (1–15), or 0/quit to exit: ").strip()

    if user_input.lower() == "quit" or user_input == "0":
        print(f"The value {user_input} has been used to exit.")
        break

    elif user_input.isdigit():
        requested_id = int(user_input)

        if 1 <= requested_id <= 15:
            found = False

            # Search the list for the matching course ID.
            for course_id, department in departments:
                if course_id == requested_id:
                    print(
                        f"Course ID {requested_id} is in the "
                        f"{department} department."
                    )
                    found = True
                    break

            if not found:
                print("Course ID not found.")

        else:
            print("Course ID is out of range (1–15), try again.")

    else:
        print("Please enter a whole number from 1–15, or 0/quit.")
        
        # Each inner list stores:
# Course ID, Course Name, Department, Prerequisites.
courses = [
    [1, "Introduction to Programming", "Computer Science", "None"],
    [2, "Calculus I", "Mathematics", "None"],
    [3, "Data Structures and Algorithms", "Computer Science",
     "Introduction to Programming"],
    [4, "Linear Algebra", "Mathematics", "None"],
    [5, "Physics I", "Physics", "None"],
    [6, "Chemistry I", "Chemistry", "None"],
    [7, "Biology I", "Biology", "None"],
    [8, "Microeconomics", "Economics", "None"],
    [9, "Macroeconomics", "Economics", "Microeconomics"],
    [10, "Psychology I", "Psychology", "None"],
    [11, "History I", "History", "None"],
    [12, "English Composition I", "English", "None"],
    [13, "Introduction to Philosophy", "Philosophy", "None"],
    [14, "Calculus II", "Mathematics", "Calculus I"],
    [15, "Discrete Mathematics", "Computer Science",
     "Introduction to Programming"]
]

# Check that all 15 course records are stored.
print(f"Total courses stored: {len(courses)}")
print("Example course record:")
print(courses[13])

# Ask the user for a course ID.
user_input = input("\nEnter a course ID (1–15): ").strip()

try:
    # Convert the input to an integer.
    requested_id = int(user_input)
    found_course = None

    # Search for a matching course ID.
    for course in courses:
        if course[0] == requested_id:
            found_course = course
            break

    # Display the matching course or an error message.
    if found_course is not None:
        print("\nCourse Information")
        print(f"Course ID: {found_course[0]}")
        print(f"Course Name: {found_course[1]}")
        print(f"Department: {found_course[2]}")
        print(f"Prerequisites: {found_course[3]}")
    else:
        print(f"Course ID {requested_id} was not found.")

except ValueError:
    print("Invalid input. Please enter a whole number.")
    