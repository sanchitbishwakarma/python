file = open("students.txt", "r")

passed_students_names = []

for line in file:
    # Figure out how the name and mark are separated
    parts = line.split()
    name = parts[0]
    marks = int(parts[1])
    if marks >= 45:
        passed_students_names.append(name)
file.close()

new_file = open("passed_students.txt", "w")

# for name in passed_students_names:
#     new_file.write(name + "\n")
# new_file.close()

# more short way
new_file.writelines(name + "\n" for name in passed_students_names)
new_file.close()
