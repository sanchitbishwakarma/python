filePath = "./file/robots.txt"

with open(filePath, "w") as file:
    # file = file.DictWrite
    file.write("Jetha Lal Gada, 50\n")
    file.write("Tarak Mehta, 81\n")
    file.write("Atma Ram Bhide, 82\n")
    file.write("Roshan Singh Sodi, 83\n")
    file.write("Dr. Hathi, 84\n")
    file.close()

with open(filePath, "r") as file:
    for line in file:
        names,marks = line.strip().split(", ")
        if int(marks) > 75:
            print(names + " -> " + marks)
            
with open(filePath, "a") as file:
    file.write("Sanchit, 91")
        