x = int(input(">> Enter: "))
ASCII = 65 #97
for n in range(ASCII,ASCII+x):
  print(f"{chr(n)} " * x)