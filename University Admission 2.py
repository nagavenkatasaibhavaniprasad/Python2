
# University Admission Decision Engine

print("=" * 50)
print(" UNIVERSITY ADMISSION DECISION ENGINE ")
print("=" * 50)

# Course eligibility requirements stored as tuples
courses = [
    ("CSE", 75, 70),
    ("AI & ML", 70, 65),
    ("ECE", 65, 60)
]

# Each course tuple: course name, minimum aggregate, minimum subject mark

# Applicant details stored in a nested list
applicants = []

n = int(input("Enter number of applicants: "))

if n <= 0:
    print("Number of applicants must be positive.")

else:
    for i in range(n):
        print("\nApplicant", i + 1)

        name = input("Enter applicant name: ").strip()
        maths = float(input("Enter Mathematics marks: "))
        physics = float(input("Enter Physics marks: "))
        subject = float(input("Enter Computer Science marks: "))
        aggregate = float(input("Enter aggregate percentage: "))
        course = input("Enter course (CSE / AI & ML / ECE): ").upper().strip()

        # Validate marks
        if (not name or maths < 0 or maths > 100
                or physics < 0 or physics > 100
                or subject < 0 or subject > 100
                or aggregate < 0 or aggregate > 100):
            print("Invalid applicant details. Applicant rejected.")
            continue

        # Store applicant details
        applicants.append([
            name, maths, physics, subject, aggregate, course
        ])

    eligible = []

    # Evaluate each applicant
    for applicant in applicants:
        name, maths, physics, subject, aggregate, course = applicant

        found = False

        for requirement in courses:
            course_name, min_aggregate, min_subject = requirement

            if course == course_name:
                found = True

                if (maths >= 50 and physics >= 50
                        and subject >= min_subject
                        and aggregate >= min_aggregate):

                    eligible.append([
                        name, course, aggregate, maths
                    ])

                break

        if not found:
            print("Unknown course for", name)

    # Rank by aggregate, then Mathematics marks,
    # then applicant name alphabetically
    for i in range(len(eligible)):
        for j in range(i + 1, len(eligible)):
            first = eligible[i]
            second = eligible[j]

            if (second[2] > first[2]
                    or (second[2] == first[2]
                        and second[3] > first[3])
                    or (second[2] == first[2]
                        and second[3] == first[3]
                        and second[0].lower() < first[0].lower())):

                eligible[i], eligible[j] = eligible[j], eligible[i]

    # Display ranked list
    print("\n" + "=" * 50)
    print("        ELIGIBLE ADMISSION RANK LIST")
    print("=" * 50)

    if len(eligible) == 0:
        print("No eligible applicants found.")

    else:
        print("Rank | Name | Course | Aggregate | Maths")
        print("-" * 50)

        rank = 1

        for applicant in eligible:
            name, course, aggregate, maths = applicant

            print(rank, "|", name, "|", course, "|",
                  aggregate, "|", maths)

            rank += 1

    print("=" * 50)
    print("Total applicants:", n)
    print("Valid applicants:", len(applicants))
    print("Eligible applicants:", len(eligible))
    print("Admission evaluation completed.")
