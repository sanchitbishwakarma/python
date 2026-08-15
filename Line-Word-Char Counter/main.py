FILE = "students.txt"

line_count = 0
word_count = 0
char_count = 0

with open(FILE, "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)


print(f"line: {line_count}")
print(f"word: {word_count}")
print(f"char: {char_count}")
