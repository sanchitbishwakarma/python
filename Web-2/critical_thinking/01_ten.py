# ask the user for number and it will show in words 5 -> five. we don't know what user will enter, there is no limit of word

dataDict = {
    '0':'Zero',
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine',
}

userInput = input("Enter the number: ")
for n in userInput:
    if n in dataDict:
        print(dataDict[n])
    else:
        print("Not Found")