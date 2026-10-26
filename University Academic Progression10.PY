
print("=" * 65)
print("        UNIVERSITY ACADEMIC PROGRESSION AUDIT")
print("=" * 65)

# Student details
student = {
    "id": 101,
    "name": "Bhavani Prasad",
    "course": "B.Tech CSE AIML"
}

# Subject, Semester, Marks, Minimum Pass Marks, Attendance
subjects = [
    ["Python", 1, 75, 40, 85],
    ["Mathematics", 1, 45, 40, 90],
    ["Programming", 1, 68, 40, 80],
    ["Computer Fundamentals", 1, 55, 40, 80],
    ["Data Structures", 2, 65, 40, 88]
]

# Prerequisite completion records
prerequisites = {
    "Python": True,
    "Mathematics": True,
    "Programming": True,
    "Computer Fundamentals": True,
    "Data Structures": True
}

MIN_ATTENDANCE = 75

passed_subjects = []
failed_subjects = []
attendance_shortage = []
prerequisite_pending = []
outstanding = []

total_marks = 0
total_subjects = 0

print("\nSTUDENT DETAILS")
print("-" * 65)
print("Student ID:", student["id"])
print("Name:", student["name"])
print("Course:", student["course"])

print("\nSUBJECT-WISE ACADEMIC AUDIT")
print("-" * 65)

for subject in subjects:
    name, semester, marks, pass_marks, attendance = subject

    total_marks += marks
    total_subjects += 1

    print("\nSubject:", name)
    print("Semester:", semester)
    print("Marks:", marks)
    print("Attendance:", str(attendance) + "%")

    subject_issues = []

    # Check pass marks
    if marks < pass_marks:
        failed_subjects.append(name)
        subject_issues.append("Minimum pass marks not achieved")
    else:
        passed_subjects.append(name)

    # Check attendance
    if attendance < MIN_ATTENDANCE:
        attendance_shortage.append(name)
        subject_issues.append("Attendance below 75%")

    # Check prerequisites
    if not prerequisites.get(name, False):
        prerequisite_pending.append(name)
        subject_issues.append("Prerequisite not completed")

    if subject_issues:
        outstanding.append(name)
        print("Status: REQUIREMENTS PENDING")
        for issue in subject_issues:
            print("-", issue)
    else:
        print("Status: CLEARED")

# Semester-wise summary
semester_marks = {}

for subject in subjects:
    name, semester, marks, pass_marks, attendance = subject

    if semester not in semester_marks:
        semester_marks[semester] = []

    semester_marks[semester].append(marks)

print("\n" + "=" * 65)
print("SEMESTER-WISE SUMMARY")
print("=" * 65)

for semester, marks_list in sorted(semester_marks.items()):
    average = sum(marks_list) / len(marks_list)

    print("\nSemester:", semester)
    print("Subjects:", len(marks_list))
    print("Total Marks:", sum(marks_list))
    print("Average Marks:", round(average, 2))

# Final academic audit
print("\n" + "=" * 65)
print("FINAL ACADEMIC PROGRESSION AUDIT")
print("=" * 65)

print("Total Subjects:", total_subjects)
print("Passed Subjects:", len(passed_subjects))
print("Failed Subjects:", len(failed_subjects))
print("Attendance Shortages:", len(attendance_shortage))
print("Pending Prerequisites:", len(prerequisite_pending))
print("Outstanding Subjects:", len(set(outstanding)))
print("Overall Average:", round(total_marks / total_subjects, 2))

print("\nFAILED SUBJECTS:", failed_subjects)
print("ATTENDANCE SHORTAGE:", attendance_shortage)
print("PREREQUISITES PENDING:", prerequisite_pending)

# Progression eligibility decision
if (
    len(failed_subjects) == 0
    and len(attendance_shortage) == 0
    and len(prerequisite_pending) == 0
):
    print("\nPROGRESSION STATUS: ELIGIBLE")
    print("All academic requirements are completed.")
else:
    print("\nPROGRESSION STATUS: NOT ELIGIBLE")
    print("Outstanding requirements must be completed.")

    if failed_subjects:
        print("- Clear failed subjects.")

    if attendance_shortage:
        print("- Resolve attendance requirements.")

    if prerequisite_pending:
        print("- Complete pending prerequisites.")

print("\nAudit completed successfully.")
print("=" * 65)
