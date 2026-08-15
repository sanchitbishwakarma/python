def calculateBill(units):
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return bill

unitsConsumed = float(input("Enter the units: "))
total_bill = calculateBill(unitsConsumed)
print(total_bill)

