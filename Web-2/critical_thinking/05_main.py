def func(x, list = []):
    list.append(x)
    return list

print(func(1)) # [1]
print(func(2)) # [1,2]
print(func(3, [])) # [3]