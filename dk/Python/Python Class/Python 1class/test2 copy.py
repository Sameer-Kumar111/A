# Dictionary of 3 students with name as key and marks as value
students = {
    "Alice": 85,
    "Bob": 65,
    "Charlie": 90
}

# Print students who scored more than 70
for name, marks in students.items():
    if marks > 70:
        print(f"{name} scored {marks}")
