# 1. Student Identity
# student_registry: {StudentID: (Name, Major, Graduation Year)}
student_registry = {
    1001: ("Alice", "BTEE", 2029),
    1002: ("Bob", "BTRE", 2029),
    1003: ("Charlie", "BTCS", 2029)
}
# 2. Course Enrollment (Set)
# course_enrollments: {StudentID: {course_codes}}
course_enrollments = {
    1001: {"BTEE101", "MATH101"},
    1002: {"BTRE101", "PHY101"},
    1003: {"BTCS101", "MATH101"}
}


# Function to enroll student
def enroll_student(sid, course_code):
    if sid in course_enrollments:
        course_enrollments[sid].add(course_code)
    else:
        course_enrollments[sid] = {course_code}

    print("Updated Courses:", course_enrollments[sid])


# 3. Grade Tracking (List of Tuples)
# grade_books: {StudentID: [(course, grade), ...]}
grade_books = {
    1001: [("BTEE101", 85), ("MATH101", 90)],
    1002: [("BTRE101", 75), ("PHY101", 80)],
    1003: [("BTCS101", 88), ("MATH101", 92)]
}


# 1. Common Ground Finder
def common_courses(sid1, sid2):
    courses1 = course_enrollments.get(sid1, set())
    courses2 = course_enrollments.get(sid2, set())
    return courses1.intersection(courses2)


# 2. GPA Calculator (Average marks)
def calculate_gpa(sid):
    grades = grade_books.get(sid, [])
    if not grades:
        return 0
    total = sum(mark for course, mark in grades)
    return total / len(grades)


# 3. Registry Auditor
def registry_audit():
    print("\n--- Registry Report ---")
    for sid in student_registry:
        name = student_registry[sid][0]
        courses = course_enrollments.get(sid, set())
        print(f"Name: {name} | Courses: {courses}")


# Enroll student
enroll_student(1001, "AI101")  # new course
enroll_student(1001, "CS101")  # duplicate (won't repeat)

# Find common courses
print("\nCommon Courses (1001 & 1003):", common_courses(1001, 1003))

# Calculate GPA
print("\nGPA of Student 1001:", calculate_gpa(1001))

# Print audit report
registry_audit()