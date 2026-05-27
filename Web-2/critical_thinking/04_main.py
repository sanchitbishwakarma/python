a = ["Learn", "Practice", "Improve"]
b = a
c = a[:]
print(a,b,c)
b[0] = 'Code'
c[1] = 'MCQ'
print(a,b,c)

count = 0
for c in (a,b,c):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'MCQ':
        count += 100
print(count)