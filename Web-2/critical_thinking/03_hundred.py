# ask the user for number and it will show in words 5 -> five. we don't know what user will enter, there is no limit of word

smallNumber = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
}

tensNumber = {
    20: "Twenty",
    30: "Thirty",
    40: "Fourty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety",
}

number = int(input("Enter the number: "))
if number < 20:
    if number in smallNumber:
        print(smallNumber[number])
elif number < 100:
    if (number % 10 == 0):
        print(tensNumber[number])
    else:
        remainder = number % 10
        firstWord = tensNumber[number-remainder]
        secondWord = smallNumber[remainder]
        print(f"{firstWord} {secondWord}")
else:
    if number % 100  == 0:
        print("One Hundred")
    else: # 104 -> 4, 143 -> 43
        tensReminder = number % 100 # 4, 43
        firstHundredWord = smallNumber[int(str(number)[0])] # 143 -> '143' -> '1' -> 1 -> search
        onesReminder = (number % 100) % 10
        if tensReminder < 20:
            if tensReminder in smallNumber:
                print(f"{firstHundredWord} Hundred {smallNumber[tensReminder]}")
        else:
            onesReminder = (number % 100) % 10
            firstWord = tensNumber[tensReminder - onesReminder]
            secondWord = smallNumber[onesReminder]
            print(f"{firstHundredWord} Hundred {firstWord} {secondWord}")