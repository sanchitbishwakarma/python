defaultSquare = [x for x in range(1,50) if x % 4 == 0]
squaresByFour = [x**2 for x in range(1,50) if x % 4 == 0]
# squares = [x**2 for x in range(1,50) if x**2 > 200 and x**2 % 4 == 0]
squares = [sq for x in range(1, 50) if (sq := x**2) > 200 and sq % 4 == 0]

print(defaultSquare)
print(squaresByFour)
print(squares)