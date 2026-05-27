import json

studentData = {
    "name": "Sanchit Babu Bishwakarma",
    "age": 14,
    "subjects": ["Math", "Science", "English"],
}

with open("demo.json", "w") as file:
    dumpedData = json.dumps(studentData) # returns in string
    json.dump(dumpedData, fp=file, indent=2)
    print(">> Dumped Data: " + dumpedData)
    
with open("demo.json", "r") as file:
    strData = json.load(file)
    objJson = json.loads(strData)
    # ddd = json.load(objJson)
    print(">> Loaded Data: ", objJson, type(objJson))   