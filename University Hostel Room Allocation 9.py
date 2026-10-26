
print("=" * 50)
print(" UNIVERSITY HOSTEL ROOM ALLOCATION ")
print("=" * 50)

# Room details
rooms = {
    101: {"capacity": 2, "students": []},
    102: {"capacity": 2, "students": []},
    103: {"capacity": 2, "students": []}
}

# Student allocation requests
allocations = [
    ("Bhavani", 101),
    ("Sita", 101),
    ("Priya", 101),
    ("Ravi", 102),
    ("Kiran", 102),
    ("Ravi", 103),
    ("Arjun", 102)
]

allocated_students = set()
unallocated_students = []
duplicate_count = 0

print("\nALLOCATION RESULTS")

for student, room_no in allocations:

    # Check duplicate assignment first
    if student in allocated_students:
        print(
            f"Duplicate Assignment: {student} "
            "already assigned to another room."
        )
        duplicate_count += 1
        continue

    # Check room capacity
    if len(rooms[room_no]["students"]) < rooms[room_no]["capacity"]:
        rooms[room_no]["students"].append(student)
        allocated_students.add(student)
        print(f"{student} allocated to Room {room_no}")
    else:
        print(f"Room {room_no} is full. Cannot allocate {student}")
        unallocated_students.append(student)

print("\nFINAL ROOM DETAILS")

for room_no, details in rooms.items():
    students = details["students"]
    capacity = details["capacity"]
    occupied = len(students)
    available = capacity - occupied

    print(f"\nRoom {room_no}")
    print(f"Capacity: {capacity}")
    print(f"Students: {students}")
    print(f"Occupied: {occupied}")
    print(f"Available beds: {available}")

print("\nUNALLOCATED STUDENTS:", unallocated_students)
print("Unallocated Demand:", len(unallocated_students))
print("Total Duplicate Assignments Detected:", duplicate_count)
print("Total Students Allocated:", len(allocated_students))
print("=" * 50)


