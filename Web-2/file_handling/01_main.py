
# file = open(r"D:\Python\database\notes.txt", "r")
# file = open("D:\\Python\\database\\notes.txt")
# file = open("D:/Python/database/notes.txt")
file = open("../../database/notes.txt")
content = file.read()
print(content, type(content))
file.close()