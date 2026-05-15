x = 10
y = 20
z = 30
# r = x if x > y else y if y > z else z
r = x if x > y and x > z else y if y > z else z
print(r)