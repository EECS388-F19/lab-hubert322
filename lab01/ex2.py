students = ["Hubert", "Sid", "Thomas"]
students.sort()
print(students)

first_name = students[0]
first_name = first_name[:-1]
print(first_name)

maxx = 0
for student in students:
    if len(student) > maxx:
        maxx = len(student)
print(maxx)
