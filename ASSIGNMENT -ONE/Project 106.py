# Project 106: Exam Result Summary
# Student: Callixte

import array

print("INTEGERS")
marks = [78, 85, 90, 66, 72]
total_marks = sum(marks)
average_marks = total_marks / len(marks)
min_mark = min(marks)
max_mark = max(marks)

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Minimum Mark:", min_mark)
print("Maximum Mark:", max_mark)

print("\nSTRINGS")
report = f"Total marks obtained: {total_marks}"
summary = f"Average performance: {average_marks:.2f}"
print(report)
print(summary)

print("\nBOOLEANS")
threshold = 70
status = average_marks > threshold and max_mark > 80
if status:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

print("\nLISTS")
subjects = ["Math", "English", "Biology", "History"]
subjects.append("Physics")
if "History" in subjects:
    subjects.remove("History")
subjects.sort()
print("Updated Subjects List:", subjects)

print("\nARRAYS")
project_array = array.array('i', [78, 85, 90])
array_sum = sum(project_array)
list_sum = sum(marks[:3])
print("Array Sum:", array_sum)
print("List Sum (first 3):", list_sum)
print("Array and List sums match:", array_sum == list_sum)

print("\nDICTIONARIES")
students = [
    {"id": 1, "name": "Mukiza", "value": 78},
    {"id": 2, "name": "Twagira", "value": 85},
    {"id": 3, "name": "Callixte", "value": 90}
]

# Update Callixte's score
students[2]["value"] = 95

# Delete Twagira's record
students = [s for s in students if s["name"] != "Twagira"]

# Compute total value
total_value = sum(s["value"] for s in students)
print("Updated Student Records:")
for s in students:
    print(s)
print("Total Value of Remaining Students:", total_value)