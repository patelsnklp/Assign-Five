
# Step 1: Creating a Dictionary for Students with Marks
students = {
    "Alice": 10,
    "Bob": 20,
    "Charlie": 30,
    "Diana": 40,
    "Ethan": 50
}

# Step 2: Ask the user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show 'not found' message
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
