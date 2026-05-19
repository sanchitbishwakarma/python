n = eval(input("How many student numbers you want to add: "))

studentDict = {}

for i in range(n):
    roll,mark = input("Write the name & mark: ").split(" ")
    studentDict[roll] = int(mark)


total = 0
for value in list(studentDict.values()):
    total += value
average = total/n
print(studentDict)
print(average)