import json

'''
str_test = '{"a": "aa", "b": "bb", "c": "cc"}'
print(type(str_test))
result = json.loads(str_test)
print(result)
print(type(result))

'''


def SendJsonResponse(resultDict):
    print("Convert Python dictionary into JSON formatted String")
    developer_str = json.dumps(resultDict)
    print(developer_str)


# sample developer dict
developer_Dict = {
    "name": "admin",
    "salary": 9000,
    "skills": ["Python", "Machine Learning", "Web Development"],
    "email": "admin@webkaka.com"
}
SendJsonResponse(developer_Dict)



sampleDict = {
    "colorList": ["Red", "Green", "Blue"],
    "carTuple": ("BMW", "Audi", "range rover"),
    "sampleString": "pynative.com",
    "sampleInteger": 457,
    "sampleFloat": 225.48,
    "booleantrue": True,
    "booleanfalse": False,
    "nonevalue": None
}
print("Converting Python primitive types into JSON")
resultJSON = json.dumps(sampleDict)
print("Done converting Python primitive types into JSON")
print(resultJSON)
