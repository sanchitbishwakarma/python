x = 10
y = 20
z = 30
r = x if x > y else y if y > z else z # 10 = 10 > 20 = 20 & 20 = 20 > 30 = 30
# r = x if x > y and x > z else y if y > z else z
print(r)