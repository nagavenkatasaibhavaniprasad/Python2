
# Multi-Stage Scholarship Shortlisting

students = [
    ("Ravi", 90, 95, 100000),
    ("Bhavani", 85, 90, 150000),
    ("Kiran", 78, 80, 200000),
    ("Priya", 92, 96, 120000),
    ("Arjun", 70, 85, 180000),
    ("Sita", 88, 75, 90000)
]

minimum_marks = 75
minimum_attendance = 75
maximum_income = 200000
quota = 3

eligible = []

print("SCHOLARSHIP SHORTLISTING")
print("------------------------")

# Stage 1: Check eligibility
for student in students:
    name, marks, attendance, income = student

    if (marks >= minimum_marks and
        attendance >= minimum_attendance and
        income <= maximum_income):

        eligible.append(student)

        print(name, "- Eligible")
    else:
        print(name, "- Not Eligible")

# Stage 2: Rank eligible students by marks
eligible.sort(key=lambda student: student[1], reverse=True)

# Stage 3: Select candidates within quota
selected = eligible[:quota]

print("\n------------------------")
print("FINAL SCHOLARSHIP LIST")

rank = 1
for student in selected:
    name, marks, attendance, income = student

    print("Rank:", rank)
    print("Name:", name)
    print("Marks:", marks)
    print("Attendance:", attendance, "%")
    print("Family Income: Rs.", income)
    print("------------------------")

    rank += 1

print("Total Selected:", len(selected))
print("Scholarship Quota:", quota)
